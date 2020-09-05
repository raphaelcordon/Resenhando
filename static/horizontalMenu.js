// -----------------------------------------------------------------
// Horizontal Index Scrollbar Beginning

// duration of scroll animation
var scrollDuration = 1200;
// paddles ARTIST
var artistLeftPaddle = document.getElementById('artistLeftPaddle');
var artistRightPaddle = document.getElementById('artistRightPaddle');

// paddles ALBUM
var albumLeftPaddle = document.getElementById('albumLeftPaddle');
var albumRightPaddle = document.getElementById('albumRightPaddle');

// paddles TRACK
var trackLeftPaddle = document.getElementById('trackLeftPaddle');
var trackRightPaddle = document.getElementById('trackRightPaddle');

// paddles PLAYLIST
var playlistLeftPaddle = document.getElementById('playlistLeftPaddle');
var playlistRightPaddle = document.getElementById('playlistRightPaddle');


// get items dimensions
var itemsLength = $('.index-item').length;
var itemSize = $('.index-item').outerWidth(true);
// get some relevant size for the paddle triggering point
var paddleMargin = 20;

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



// ----- ARTIST -----
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
		$(artistLeftPaddle).addClass('hidden');
		$(artistRightPaddle).removeClass('hidden');
	} else if (menuPosition < menuEndOffset) {
		// show both paddles in the middle
		$(artistLeftPaddle).removeClass('hidden');
		$(artistRightPaddle).removeClass('hidden');
	} else if (menuPosition >= menuEndOffset) {
		$(artistLeftPaddle).removeClass('hidden');
		$(artistRightPaddle).addClass('hidden');
}

});

// scroll to left
$(artistRightPaddle).on('click', function() {
    $('#artist-index-menu').animate( { scrollLeft: menuInvisibleSize}, scrollDuration);
});

// scroll to right
$(artistLeftPaddle).on('click', function() {
	$('#artist-index-menu').animate( { scrollLeft: '0' }, scrollDuration);
});


// ----- ALBUM -----
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
		$(albumLeftPaddle).addClass('hidden');
		$(albumRightPaddle).removeClass('hidden');
	} else if (menuPosition < menuEndOffset) {
		// show both paddles in the middle
		$(albumLeftPaddle).removeClass('hidden');
		$(albumRightPaddle).removeClass('hidden');
	} else if (menuPosition >= menuEndOffset) {
		$(albumLeftPaddle).removeClass('hidden');
		$(albumRightPaddle).addClass('hidden');
}

});


// scroll to left
$(albumRightPaddle).on('click', function() {
    $('#album-index-menu').animate( { scrollLeft: menuInvisibleSize}, scrollDuration);
});

// scroll to right
$(albumLeftPaddle).on('click', function() {
	$('#album-index-menu').animate( { scrollLeft: '0' }, scrollDuration);
});


// ----- TRACK -----
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
		$(trackLeftPaddle).addClass('hidden');
		$(trackRightPaddle).removeClass('hidden');
	} else if (menuPosition < menuEndOffset) {
		// show both paddles in the middle
		$(trackLeftPaddle).removeClass('hidden');
		$(trackRightPaddle).removeClass('hidden');
	} else if (menuPosition >= menuEndOffset) {
		$(trackLeftPaddle).removeClass('hidden');
		$(trackRightPaddle).addClass('hidden');
}

});


// scroll to left
$(trackRightPaddle).on('click', function() {
    $('#track-index-menu').animate( { scrollLeft: menuInvisibleSize}, scrollDuration);
});

// scroll to right
$(trackLeftPaddle).on('click', function() {
	$('#track-index-menu').animate( { scrollLeft: '0' }, scrollDuration);
});


// ----- PLAYLIST -----
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
		$(playlistLeftPaddle).addClass('hidden');
		$(playlistRightPaddle).removeClass('hidden');
	} else if (menuPosition < menuEndOffset) {
		// show both paddles in the middle
		$(playlistLeftPaddle).removeClass('hidden');
		$(playlistRightPaddle).removeClass('hidden');
	} else if (menuPosition >= menuEndOffset) {
		$(playlistLeftPaddle).removeClass('hidden');
		$(playlistRightPaddle).addClass('hidden');
}

});


// scroll to left
$(playlistRightPaddle).on('click', function() {
    $('#playlist-index-menu').animate( { scrollLeft: menuInvisibleSize}, scrollDuration);
});

// scroll to right
$(playlistLeftPaddle).on('click', function() {
	$('#playlist-index-menu').animate( { scrollLeft: '0' }, scrollDuration);
});