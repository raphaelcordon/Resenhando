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

    $("#formAlbum").hide(1000);
    $("#formTrack").hide(1000);
    $("#formPlaylist").hide(1000);
    $("#formArtist").toggle(1000);
  });
});

// Album
$(document).ready(function(){
  $("#buttonAlbum").click(function(){

      $("#formArtist").hide(1000);
      $("#formTrack").hide(1000);
      $("#formPlaylist").hide(1000);
    $("#formAlbum").toggle(1000);
  });
});

// Track
$(document).ready(function(){
  $("#buttonTrack").click(function(){

    $("#formArtist").hide(1000);
    $("#formAlbum").hide(1000);
    $("#formPlaylist").hide(1000);
    $("#formTrack").toggle(1000);
  });
});

// Playlist
$(document).ready(function(){
  $("#buttonPlaylist").click(function(){

    $("#formArtist").hide(1000);
    $("#formAlbum").hide(1000);
    $("#formTrack").hide(1000);
    $("#formPlaylist").toggle(1000);
  });
});
