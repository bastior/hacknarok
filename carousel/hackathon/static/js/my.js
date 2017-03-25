/**
 * Created by plizonczyk on 25.03.17.
 */
$(document).ready(function() {
    $("#accept-btn").click(function () {
        if ($(".offer-item.active").data("last") === "True") {
            $.ajax({method: "GET", url: "accept", data: {id: $(".offer-item.active").data("id")}});
            $(".carousel-inner").html("<h2>No new offers! Come back later.</h2>");
            $("#foooooter").hide()
        } else {
            $.ajax({method: "GET", url: "accept", data: {id: $(".offer-item.active").data("id")}});
        }
    });
    $("#reject-btn").click(function () {
        if ($(".offer-item.active").data("last") === "True") {
            $.ajax({method: "GET", url: "reject", data: {id: $(".offer-item.active").data("id")}});
            $(".carousel-inner").html("<h2>No new offers! Come back later.</h2>");
            $("#foooooter").hide()
        } else {
            $.ajax({method: "GET", url: "reject", data: {id: $(".offer-item.active").data("id")}});
        }
    });
    $("#accept-recruit").click(function () {
        $("#myModal").modal().toggle();
        $("#myModalLabel").html('Get in touch with ' + $('#recruit-name').html());
    });
});
