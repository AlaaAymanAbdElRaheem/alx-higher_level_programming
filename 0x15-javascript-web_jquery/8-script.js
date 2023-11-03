#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    for (const movie of data.results) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    }
  }
});
