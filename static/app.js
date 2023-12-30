"use strict";


const street = document.getElementById('street').innerText;
const state = document.getElementById('state').innerText;
//FIXME: street/state should probably come from the server rather than scraping

/** using google maps example code from developers.google.com */
/**
 * @license
 * Copyright 2019 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */
// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
let map;
let service;
let infowindow;

function initMap() {
  //FIXME: Should center on users current location initially, not hard coded
  const oakland = new google.maps.LatLng(37.8077184, -122.2115328);

  infowindow = new google.maps.InfoWindow();
  map = new google.maps.Map(document.getElementById("map"), {
    center: oakland,
    zoom: 15,
  });

  let request = {
    //query: "Museum of Contemporary Art Australia",
    //query: `${street} ${state}`,
    query: `${street} ${state}`,
    fields: ["name", "geometry"],
  };

  service = new google.maps.places.PlacesService(map);
  service.findPlaceFromQuery(request, (results, status) => {
    if (status === google.maps.places.PlacesServiceStatus.OK && results) {
      for (let i = 0; i < results.length; i++) {
        createMarker(results[i]);
      }

      map.setCenter(results[0].geometry.location);
    }
  });
}

function createMarker(place) {
  if (!place.geometry || !place.geometry.location) return;

  const marker = new google.maps.Marker({
    map,
    position: place.geometry.location,
  });

  google.maps.event.addListener(marker, "click", () => {
    infowindow.setContent(place.name || "");
    infowindow.open(map);
  });
}

window.initMap = initMap;

/**end google code */

