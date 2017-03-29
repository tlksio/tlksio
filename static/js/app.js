$(function() {

  $('.favorite').click(function() {
    var fav = $(this);
    var id = fav.data("id");
    $.get("/talk/favorite/"+id, function(data) {
      fav.find("i").toggleClass("red");
    });
  });

});
