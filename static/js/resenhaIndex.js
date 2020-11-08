// Artist
$(document).ready(function () {
  $("#buttonArtist").click(function () {

    $(".initiallyHidden").hide(20);
    $("#formArtist").toggle(400);
  });
});

// Album
$(document).ready(function () {
  $("#buttonAlbum").click(function () {

    $(".initiallyHidden").hide(20);
    $("#formAlbum").toggle(400);
  });
});

// Track
$(document).ready(function () {
  $("#buttonTrack").click(function () {

    $(".initiallyHidden").hide(20);
    $("#formTrack").toggle(400);
  });
});

// Playlist
$(document).ready(function () {
  $("#buttonPlaylist").click(function () {

    $(".initiallyHidden").hide(20);
    $("#formPlaylist").toggle(400);
  });
});


// Copy URL
$(document).ready(function () {

  $("#btnCopyLink").click(function () {
    var tempInput = document.createElement("input");
    tempInput.style = "position: absolute; left: -1000px; top: -1000px";
    tempInput.value = $("#myInput").val();
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);
    $("#myTooltip").html("Link copiado");
  });

  $("#btnCopyLink").mouseover(function () {
    $("#myTooltip").html("Copiar Link");
  });

});

// Update Comments as read in Notifications
$(function() {
  $('#linkComments').bind('click', function() {
    $.getJSON('/commentRead',
        function(data) {
      //do nothing
    });
    return false;
  });
});

// Update Likes as read in Notifications
$(function() {
  $('#linkLikes').bind('click', function() {
    $.getJSON('/likeRead',
        function(data) {
      //do nothing
    });
    return false;
  });
});


$(document).on('shown.bs.modal', function () {
    var albumId =           $('#albumData').data('album').id;
    var albumName =         $('#albumData').data('album').name;
    var albumImage =        $('#albumData').data('album').image;
    var albumArtistName =   $('#albumData').data('album').artist_name;
    var albumReleaseDate =  $('#albumData').data('album').release_date;
    var albumTotalTracks =  $('#albumData').data('album').totalTracks;
    var albumRadio =        $('#albumData').data('album').radio;
    var albumGenres =       $('#albumData').data('album').genres;


    //clean up the modal
    $("#albumId").empty();
    $("#albumName").empty();
    $("#albumImage").empty();
    $("#albumArtistName").empty();
    $("#albumReleaseDate").empty();
    $("#albumTotalTracks").empty();
    $("#albumRadio").empty();
    $("#albumGenres").empty();

    // fill up data
    $(".modal-body #albumId").val( albumId );
    $("#albumName").append("<h4>" + albumName + "</h4>");
    $("#albumImage").append("<img src=' " + albumImage + "'><br>");
    $("#albumArtistName").after("<b>Artista:</b> " + albumArtistName + ". &nbsp; Álbum lançado em " + albumReleaseDate + ", com " + albumTotalTracks + " faixas.<br>");
    $("#albumRadio").append("<br> &nbsp;<iframe src='" + albumRadio + "' width='300' height='300' frameborder='0' allowtransparency='true' allow='encrypted-media'></iframe>");
    $("#linkResenha").append("{{ url_for('res.resenhaNewAlbum', albumId= " + album.id + ") }}");
    $("#albumGenres").after("<b>Gênero(s):</b> " + albumGenres + "<br>");
});
