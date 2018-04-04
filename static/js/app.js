function geolocate() {
	if ("geolocation" in navigator) {
		navigator.geolocation.getCurrentPosition(function(pos) {
			$("#address").attr("placeholder","My Location");
			$("#lat").attr("value", pos.coords.latitude);
			$("#lng").attr("value", pos.coords.longitude);
		});
	} else {
		// Geolocation not supported
	}
	return;
}

$(geolocate());