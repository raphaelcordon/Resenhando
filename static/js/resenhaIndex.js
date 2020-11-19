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
$(function () {
  $('#linkComments').bind('click', function () {
    $.getJSON('/commentRead',
      function (data) {
        //do nothing
      });
    return false;
  });
});

// Update Likes as read in Notifications
$(function () {
  $('#linkLikes').bind('click', function () {
    $.getJSON('/likeRead',
      function (data) {
        //do nothing
      });
    return false;
  });
});


$(document).on('click', ".listAlbumModal", function () {

  var album = $(this).data('album');
  var albumId = album.id;
  var albumName = album.name;
  var albumImage = album.image;
  var albumArtistName = album.artist_name;
  var albumReleaseDate = album.release_date;
  var albumTotalTracks = album.totalTracks;
  var albumRadio = album.radio;
  var albumGenres = album.genres;

  //clean up the modal
  $("#albumId").empty();
  $("#albumName").empty();
  $("#albumImage").empty();
  $("#albumArtistName").empty();
  $("#albumReleaseDate").empty();
  $("#albumTotalTracks").empty();
  $("#albumRadio").empty();
  $("#albumGenres").empty();
  $("#linkResenha").empty();
  $("#linkResenha2").empty();

  // fill up data
  $(".modal-body #albumId").val(albumId);
  $("#albumName").append("<h4>" + albumName + "</h4>");
  $("#albumImage").append("<img src=' " + albumImage + "'><br>");
  $("#albumArtistName").append("<b>Artista:</b> " + albumArtistName + ". &nbsp; Álbum lançado em " + albumReleaseDate + ", com " + albumTotalTracks + " faixas.");
  $("#albumRadio").append("<iframe src='" + albumRadio + "' width='280' height='300' frameborder='0' allowtransparency='true' allow='encrypted-media'></iframe>");
  $("#linkResenha").attr("href", "/resenhaNewAlbum/" + albumId);
  $("#linkResenha").append("<h6 class='linkColor text-center'><i class='fas fa-compact-disc fa-lg'> Resenhar esse Álbum</i></h6>");
  $("#linkResenha2").attr("href", "/resenhaNewAlbum/" + albumId);
  $("#linkResenha2").append("<h6 class='linkColor text-center'><i class='fas fa-compact-disc fa-lg'> Resenhar esse Álbum</i></h6>");
  $("#albumGenres").append("<b>Gênero(s):</b> " + albumGenres);
});
