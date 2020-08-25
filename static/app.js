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


// Copy Address
function myFunction() {
 var tempInput = document.createElement("input");
    tempInput.style = "position: absolute; left: -1000px; top: -1000px";
    tempInput.value = document.getElementById("myInput").value;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);
}

function outFunc(){
    $('#popoverData').popover();
    $('#popoverOption').popover({ trigger: "hover" });
}
