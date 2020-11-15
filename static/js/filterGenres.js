$(document).on('click', ".genres", function () {
    var genre = $(this).data('genre');
    var genreLink = genre.genre;

   $(".genrelink").empty();
   $(".genrelink").attr("src", "/genresBody/" + genreLink);
   $(".genrelink").click(function() {
    window.location.reload();
    });
});
