/**
 * Created by greg on 11/14/15.
 */
$(document).ready(function(){
    $('a').click(function(){
        $('html, body').animate({
            scrollTop: $( $.attr(this, 'href') ).offset().top
        }, 500);
        return false;
    });
    $("#scouts").css({
            "padding-bottom": ".5%",
            "border-bottom-right-radius": "0%",
            "border-bottom-left-radius": "0%"
        });
    $("#scouts_info").show();


    $(".tab").click(function(){
        $(".info").hide();
        $(".tab").css({
            "padding-bottom": "0%",
            "border-bottom-right-radius": "3%",
            "border-bottom-left-radius": "3%"
        });
        $(this).css({
            "padding-bottom": ".5%",
            "border-bottom-right-radius": "0%",
            "border-bottom-left-radius": "0%"
        });
        var selec = "#" + $(this).attr("id") + "_info";
        $(selec).show();
    })
});
