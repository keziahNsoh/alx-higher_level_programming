#!/usr/bin/node

const request = require('request');

// Check if Movie ID is provided
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

// URL to get movie details from Star Wars API
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to get movie details
function getMovieDetails (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie details:', error);
      process.exit(1);
    }
    if (response.statusCode !== 200) {
      console.error('Failed to retrieve movie details. Status code:', response.statusCode);
      process.exit(1);
    }

    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Fetch and print details for each character
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character details:', error);
          process.exit(1);
        }
        if (response.statusCode !== 200) {
          console.error('Failed to retrieve character details. Status code:', response.statusCode);
          process.exit(1);
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

// Fetch movie details
getMovieDetails(movieUrl);
