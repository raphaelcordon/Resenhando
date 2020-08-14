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

    $(".initiallyHidden").hide(20);
    $("#formArtist").toggle(400);
  });
});

// Album
$(document).ready(function(){
  $("#buttonAlbum").click(function(){

    $(".initiallyHidden").hide(20);
    $("#formAlbum").toggle(400);
  });
});

// Track
$(document).ready(function(){
  $("#buttonTrack").click(function(){

    $(".initiallyHidden").hide(20);
    $("#formTrack").toggle(400);
  });
});

// Playlist
$(document).ready(function(){
  $("#buttonPlaylist").click(function(){

    $(".initiallyHidden").hide(20);
    $("#formPlaylist").toggle(400);
  });
});
