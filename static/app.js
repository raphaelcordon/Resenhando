$('.delete').click(function () {
  var url = this.dataset.url;
  bootbox.confirm({
    size: "small",
    message: "Confirma delete?",
    callback: function (result) {
      if (result) {
        window.location.href = url;
      }
    }
  })
});

// Artist
$(document).ready(function(){
  $("#buttonArtist").click(function(){

    $("#formAlbum").hide(10);
    $("#formTrack").hide(10);
    $("#formPlaylist").hide(10);
    $("#formArtist").toggle(200);
  });
});

// Album
$(document).ready(function(){
  $("#buttonAlbum").click(function(){

      $("#formArtist").hide(10);
      $("#formTrack").hide(10);
      $("#formPlaylist").hide(10);
    $("#formAlbum").toggle(200);
  });
});

// Track
$(document).ready(function(){
  $("#buttonTrack").click(function(){

    $("#formArtist").hide(10);
    $("#formAlbum").hide(10);
    $("#formPlaylist").hide(10);
    $("#formTrack").toggle(200);
  });
});

// Playlist
$(document).ready(function(){
  $("#buttonPlaylist").click(function(){

    $("#formArtist").hide(10);
    $("#formAlbum").hide(10);
    $("#formTrack").hide(10);
    $("#formPlaylist").toggle(200);
  });
});
