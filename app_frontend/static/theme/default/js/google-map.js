
function initialize() {
    var styles = {
        'classify': [{
                "featureType": "administrative",
                "stylers": [
                    {"visibility": "on"}
                ]
            },
            {
                "featureType": "road",
                "stylers": [
                    {"visibility": "on"},
                    {"hue": "#6990cb"}
                ]
            },
            {
                "stylers": [
                    {"visibility": "on"},
                    {"hue": "#6990cb"},
                    {"saturation": -50}
                ]
            }
        ]};

    var myLatlng = new google.maps.LatLng(-34.397, 150.644);
    var myOptions = {
        zoom: 10,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        //disableDefaultUI: true,
        mapTypeId: 'classify',
                draggable: true,
        scrollwheel: false,
    }
    var map = new google.maps.Map(document.getElementById("map_classify"), myOptions);
    var styledMapType = new google.maps.StyledMapType(styles['classify'], {name: 'classify'});
    map.mapTypes.set('classify', styledMapType);

    var marker = new google.maps.Marker({
        position: myLatlng,
        map: map,
        title: ""
    });
    }

google.maps.event.addDomListener(window, 'load', initialize);
google.maps.event.addDomListener(window, 'resize', initialize);

