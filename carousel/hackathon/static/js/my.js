/**
 * Created by plizonczyk on 25.03.17.
 */
$(document).ready(function() {
    $("#accept-btn").click(function () {
        $.ajax({method: "GET", url: "accept", data: {id: $(".offer-item.active").data("id")}});
    });
});

$(document).ready(function() {
    $("#reject-btn").click(function () {
        $.ajax({method: "GET", url: "reject", data: {id: $(".offer-item.active").data("id")}});
    });
});
