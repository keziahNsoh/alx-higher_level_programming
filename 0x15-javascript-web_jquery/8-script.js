$(document).ready(function() {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movies = data.results;
    const $listMovies = $('#list_movies');
    
    // Clear existing content
    $listMovies.empty();
    
    // Iterate over the movies and append each title
    movies.forEach(function(movie) {
      $listMovies.append('<li>' + movie.title + '</li>');
    });
  });
});

