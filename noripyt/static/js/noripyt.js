//
// Tooltips
//

$('[title]').tooltip({container: 'body'});

//
// Map
//

var center = new google.maps.LatLng(49.428555, 1.065921);
var mapOptions = {
  zoom: 7,
  center: center,
  styles: [
  {
    featureType: 'poi',
    elementType: 'label',
    stylers: [{visibility: 'off'}]
  },
  {
    featureType: 'road',
    elementType: 'geometry',
    stylers: [
      {lightness: 100},
      {visibility: 'simplified'}
    ]
  },
  {
    featureType: 'road',
    elementType: 'labels',
    stylers: [
      {visibility: 'off'}
    ]
  },
  {
    featureType: 'transit',
    elementType: 'geometry',
    stylers: [
      {visibility: 'off'},
      {lightness: 700}
    ]
  },
  {
    featureType: 'water',
    elementType: 'all',
    stylers: [
      {color: '#B3DAFF'}
    ]
  }
]};
var mapElement = document.getElementById('map');
var map = new google.maps.Map(mapElement, mapOptions);
new google.maps.Marker({
  position: center,
  map: map,
  icon: 'https://maps.gstatic.com/mapfiles/ms2/micons/red.png'
});

//
// Cards
//

// FIXME: We have to do this because stupid jQuery
//        can’t return floats when using `.height()`… -_-
function getHeight($element) {
  return $element[0].getBoundingClientRect().height;
}

function updateCard($card) {
  var height = getHeight($card);
  var $caption = $card.find('.caption');
  var headerHeight = getHeight($caption.find('.header'));
  var $description = $caption.find('.description');
  $description.height('auto');
  var descriptionVerticalMargin = ($description.outerHeight(true)
                                   - $description.innerHeight());
  var descriptionHeight = height - headerHeight - descriptionVerticalMargin;
  if (descriptionHeight > $description.height()) {
    descriptionHeight = $description.height();
  }
  $description.height(descriptionHeight);
  var top = height - headerHeight;
  if ($card.hasClass('active')) {
    top -= descriptionHeight + descriptionVerticalMargin;
    $description.css('visibility', 'visible');
  }
  $caption.css('top', top);
  $caption.one('transitionend webkitTransitionEnd oTransitionEnd', function () {
    if (!$card.hasClass('active')) {
      $description.css('visibility', '');
    }
  });
}

function updateCards($cards) {
  $cards.each(function () { updateCard($(this)); });
}

function updateCardsWithoutTransition($cards) {
  var $transitioned = $cards.find('.caption');
  if ($transitioned.length == 0) {
    return;
  }
  $transitioned.addClass('no-transition');
  updateCards($cards);
  $transitioned[0].offsetHeight; // Trigger a reflow, flushing the CSS changes.
  $transitioned.removeClass('no-transition');
}

$(function () {
  $('.card.collapsible').find('img, .collapse-indicator, .header').click(function (e) {
    e.preventDefault();
    var $card = $(this).parents('.card');
    $card.toggleClass('active');
    $card.find('.collapse-indicator .fa').toggleClass('fa-flip-vertical');
    updateCard($card);
  });
  var $cards = $('.card');
  $cards.find('img').each(function () {
    var $card = $(this).parents('.card');
    if (this.complete) {
      updateCardsWithoutTransition($card);
    } else {
      $(this).load(function () {
        updateCardsWithoutTransition($card);
      });
    }
  });
  $(window).resize(function () { updateCardsWithoutTransition($cards) });
});

//
// Google Analytics
//

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-44531910-3', 'auto');
ga('send', 'pageview');
