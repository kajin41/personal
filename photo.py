from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import config
import boto3, botocore

photo_app = Flask(__name__)

photo_app.config['MAIL_SERVER'] = config.MAIL_SERVER
photo_app.config['MAIL_PORT'] = 465
photo_app.config['MAIL_USE_TLS'] = False
photo_app.config['MAIL_USE_SSL'] = True
photo_app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
photo_app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD

mail = Mail(photo_app)

s3 = boto3.resource('s3')
s3client = boto3.client(
    's3',
    aws_access_key_id=config.AWS_PHOTO_KEY,
    aws_secret_access_key=config.AWS_PHOTO_SECRET
)


@photo_app.route('/')
def index():
    nav_items = ['about']
    categories = {}
    resp = s3client.list_buckets()
    # for bucket in resp["Buckets"]:
    #     print(bucket['Name'])
    # paginator = s3client.get_paginator('list_objects')
    # result = paginator.paginate(Bucket='photo-gregorymercado', Delimiter='/')
    # for prefix in result.search('CommonPrefixes'):
    #     print(prefix.get('Prefix'))

    for key in s3client.list_objects(Bucket='photo-gregorymercado')['Contents']:
        layers = key['Key'].split('/')
        if len(layers) == 2:
            if layers[0] not in categories:
                categories[layers[0]] = {}
                nav_items.append(layers[0])
        elif len(layers) == 3:
            if layers[1] not in categories[layers[0]]:
                categories[layers[0]][layers[1]] = []
            if layers[2] != '':
                categories[layers[0]][layers[1]].append(layers[2])

        print(key['Key'])

    return render_template("photo/photo.html", title="Gregory Mercado - Photography", nav_items=nav_items, categories=categories)


if __name__ == '__main__':
    photo_app.run()
