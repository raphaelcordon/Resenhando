
// --------------------------------------------------------------------------------------------------------------------
// Common functions
// --------------------------------------------------------------------------------------------------------------------

var paddleMargin = 20;
var scrollDuration = 1200;

var getMenuWrapperSize = function (id) {
	return $(id).outerWidth();
}

var getMenuPosition = function (id) {
	return $(id).scrollLeft();
};

var getItemsLength = function (id) {
	return $(id).length;
};

var getItemsSize = function (id) {
	return $(id).outerWidth(true);
};

var showHidePaddles = function (leftPaddle, rightPaddle, menuPosition, menuEndOffset) {
	if (menuPosition <= paddleMargin) {
		leftPaddle.addClass('hidden');
		rightPaddle.removeClass('hidden');
	} else if (menuPosition < menuEndOffset) {
		leftPaddle.removeClass('hidden');
		rightPaddle.removeClass('hidden');
	} else if (menuPosition >= menuEndOffset) {
		leftPaddle.removeClass('hidden');
		rightPaddle.addClass('hidden');
	}
};

// --------------------------------------------------------------------------------------------------------------------
// Artists
// --------------------------------------------------------------------------------------------------------------------

var getArtistMenuSize = function () {
	return getItemsLength('li[id=artist-index-item]') * getItemsSize('li[id=artist-index-item]');
};
var artist_menu = $('#artist-index-menu');
var artist_leftPaddle = $('#artist-left-paddle');
var artist_rightPaddle = $('#artist-right-paddle');
var artist_menuWrapperSize = getMenuWrapperSize('#artist-index-menu-wrapper');
var artist_menuInvisibleSize = getArtistMenuSize() - artist_menuWrapperSize;

artist_menu.on('scroll', function () {
	artist_menuInvisibleSize = getArtistMenuSize() - artist_menuWrapperSize;
	var menuEndOffset = artist_menuInvisibleSize - paddleMargin;
	showHidePaddles(artist_leftPaddle, artist_rightPaddle, getMenuPosition(this), menuEndOffset);
});

artist_leftPaddle.on('click', function () {
	artist_menu.animate({ scrollLeft: '0' }, scrollDuration);
});

artist_rightPaddle.on('click', function () {
	artist_menu.animate({ scrollLeft: artist_menuInvisibleSize }, scrollDuration);
});

if (getItemsLength('li[id=artist-index-item]') <= 4) {
	artist_leftPaddle.addClass('hidden');
	artist_rightPaddle.addClass('hidden');
}

// --------------------------------------------------------------------------------------------------------------------
// Albums
// --------------------------------------------------------------------------------------------------------------------

var getAlbumMenuSize = function () {
	return getItemsLength('li[id=album-index-item]') * getItemsSize('li[id=album-index-item]');
};
var album_menu = $('#album-index-menu');
var album_leftPaddle = $('#album-left-paddle');
var album_rightPaddle = $('#album-right-paddle');
var album_menuWrapperSize = getMenuWrapperSize('#album-index-menu-wrapper');
var album_menuInvisibleSize = getAlbumMenuSize() - album_menuWrapperSize;

album_menu.on('scroll', function () {
	album_menuInvisibleSize = getAlbumMenuSize() - album_menuWrapperSize;
	var menuEndOffset = album_menuInvisibleSize - paddleMargin;
	showHidePaddles(album_leftPaddle, album_rightPaddle, getMenuPosition(this), menuEndOffset);
});

album_leftPaddle.on('click', function () {
	album_menu.animate({ scrollLeft: '0' }, scrollDuration);
});

album_rightPaddle.on('click', function () {
	album_menu.animate({ scrollLeft: album_menuInvisibleSize }, scrollDuration);
});

if (getItemsLength('li[id=album-index-item]') <= 4) {
	album_leftPaddle.addClass('hidden');
	album_rightPaddle.addClass('hidden');
}

// --------------------------------------------------------------------------------------------------------------------
// Tracks
// --------------------------------------------------------------------------------------------------------------------

var getTrackMenuSize = function () {
	return getItemsLength('li[id=track-index-item]') * getItemsSize('li[id=track-index-item]');
};
var track_menu = $('#track-index-menu');
var track_leftPaddle = $('#track-left-paddle');
var track_rightPaddle = $('#track-right-paddle');
var track_menuWrapperSize = getMenuWrapperSize('#track-index-menu-wrapper');
var track_menuInvisibleSize = getTrackMenuSize() - track_menuWrapperSize;

track_menu.on('scroll', function () {
	track_menuInvisibleSize = getTrackMenuSize() - track_menuWrapperSize;
	var menuEndOffset = track_menuInvisibleSize - paddleMargin;
	showHidePaddles(track_leftPaddle, track_rightPaddle, getMenuPosition(this), menuEndOffset);
});

track_leftPaddle.on('click', function () {
	track_menu.animate({ scrollLeft: '0' }, scrollDuration);
});

track_rightPaddle.on('click', function () {
	track_menu.animate({ scrollLeft: track_menuInvisibleSize }, scrollDuration);
});

if (getItemsLength('li[id=track-index-item]') <= 4) {
	track_leftPaddle.addClass('hidden');
	track_rightPaddle.addClass('hidden');
}

// --------------------------------------------------------------------------------------------------------------------
// Playlist
// --------------------------------------------------------------------------------------------------------------------

var getPlaylistMenuSize = function () {
	return getItemsLength('li[id=playlist-index-item]') * getItemsSize('li[id=playlist-index-item]');
};
var playlist_menu = $('#playlist-index-menu');
var playlist_leftPaddle = $('#playlist-left-paddle');
var playlist_rightPaddle = $('#playlist-right-paddle');
var playlist_menuWrapperSize = getMenuWrapperSize('#playlist-index-menu-wrapper');
var playlist_menuInvisibleSize = getPlaylistMenuSize() - playlist_menuWrapperSize;

playlist_menu.on('scroll', function () {
	playlist_menuInvisibleSize = getPlaylistMenuSize() - playlist_menuWrapperSize;
	var menuEndOffset = playlist_menuInvisibleSize - paddleMargin;
	showHidePaddles(playlist_leftPaddle, playlist_rightPaddle, getMenuPosition(this), menuEndOffset);
});

playlist_leftPaddle.on('click', function () {
	playlist_menu.animate({ scrollLeft: '0' }, scrollDuration);
});

playlist_rightPaddle.on('click', function () {
	playlist_menu.animate({ scrollLeft: playlist_menuInvisibleSize }, scrollDuration);
});

if (getItemsLength('li[id=playlist-index-item]') <= 4) {
	playlist_leftPaddle.addClass('hidden');
	playlist_rightPaddle.addClass('hidden');
}

// --------------------------------------------------------------------------------------------------------------------
// On Resize 
// --------------------------------------------------------------------------------------------------------------------

$(window).on('resize', function () {
	artist_menuWrapperSize = getMenuWrapperSize('#artist-index-menu-wrapper');
	album_menuWrapperSize = getMenuWrapperSize('#album-index-menu-wrapper');
	track_menuWrapperSize = getMenuWrapperSize('#track-index-menu-wrapper');
	playlist_menuWrapperSize = getMenuWrapperSize('#playlist-index-menu-wrapper');
});