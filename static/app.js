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


// -----------------------------------------------------------------
// Horizontal Index Scrollbar Beginning

// duration of scroll animation
var scrollDuration = 1200;
// paddles
var leftPaddle = document.getElementsByClassName('left-paddle');
var rightPaddle = document.getElementsByClassName('right-paddle');
// get items dimensions
var itemsLength = $('.index-item').length;
var itemSize = $('.index-item').outerWidth(true);
// get some relevant size for the paddle triggering point
var paddleMargin = 0;

// get wrapper width
var getMenuWrapperSize = function() {
	return $('.index-menu-wrapper').outerWidth();
}
var menuWrapperSize = getMenuWrapperSize();
// the wrapper is responsive
$(window).on('resize', function() {
	menuWrapperSize = getMenuWrapperSize();
});
// size of the visible part of the menu is equal as the wrapper size
var menuVisibleSize = menuWrapperSize;

// get total width of all menu items
var getMenuSize = function() {
	return itemsLength * itemSize;
};
var menuSize = getMenuSize();
// get how much of menu is invisible
var menuInvisibleSize = menuSize - menuWrapperSize;

// get how much have we scrolled to the left
var getMenuPosition = function() {
	return $('.index-menu').scrollLeft();
};

// finally, what happens when we are actually scrolling the menu
$('.index-menu').on('scroll', function() {

	// get how much of menu is invisible
	menuInvisibleSize = menuSize - menuWrapperSize;
	// get how much have we scrolled so far
	var menuPosition = getMenuPosition();

	var menuEndOffset = menuInvisibleSize - paddleMargin;

	// show & hide the paddles
	// depending on scroll position
	if (menuPosition <= paddleMargin) {
		$(leftPaddle).addClass('hidden');
		$(rightPaddle).removeClass('hidden');
	} else if (menuPosition < menuEndOffset) {
		// show both paddles in the middle
		$(leftPaddle).removeClass('hidden');
		$(rightPaddle).removeClass('hidden');
	} else if (menuPosition >= menuEndOffset) {
		$(leftPaddle).removeClass('hidden');
		$(rightPaddle).addClass('hidden');
}

});

// scroll to left
$(rightPaddle).on('click', function() {
	$('.index-menu').animate( { scrollLeft: menuInvisibleSize}, scrollDuration);
});

// scroll to right
$(leftPaddle).on('click', function() {
	$('.index-menu').animate( { scrollLeft: '0' }, scrollDuration);
});

// Horizontal Index Scrollbar Ending
// -----------------------------------------------------------------
