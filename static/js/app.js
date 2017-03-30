$(function() {

  $('.favorite').click(function() {
    var fav = $(this);
    var id = fav.data("id");
    $.get("/talk/favorite/"+id, function(data) {
      fav.find("i").toggleClass("red");
    });
  });

  $('.upvote').click(function() {
    var upvote = $(this);
    var id = upvote.data("id");
    $.get("/talk/upvote/"+id, function(data) {
      upvote.find(".counter").html(data.votes);
      upvote.prop("disabled",true);
    });
  });

});
