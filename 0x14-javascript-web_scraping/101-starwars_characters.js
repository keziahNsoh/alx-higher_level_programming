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

// Function to fetch and print character names from the movie
function getCharacterNames (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie details:', error);
      process.exit(1);
    }

    let movieData;
    try {
      movieData = JSON.parse(body);
    } catch (parseError) {
      console.error('Error parsing movie details:', parseError);
      process.exit(1);
    }

    const characters = movieData.characters;

    // Function to fetch character data sequentially
    const fetchSequential = (urls, index = 0) => {
      if (index >= urls.length) {
        return;
      }

      request(urls[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character details:', charError);
          process.exit(1);
        }

        let characterData;
        try {
          characterData = JSON.parse(charBody);
        } catch (charParseError) {
          console.error('Error parsing character details:', charParseError);
          process.exit(1);
        }

        console.log(characterData.name);
        // Fetch the next character
        fetchSequential(urls, index + 1);
      });
    };

    // Start fetching characters sequentially
    fetchSequential(characters);
  });
}

// Fetch movie details
getCharacterNames(movieUrl);
