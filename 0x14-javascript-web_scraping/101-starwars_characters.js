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

// Define the character ID to look for
const targetId = '18'; // Example ID for Wedge Antilles; replace with the actual ID if needed

// Function to get character names from the movie
function getCharacterNames (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie details:', error);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error('Failed to retrieve movie details. Status code:', response.statusCode);
      process.exit(1);
    }

    try {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      // Fetch and print details for each character
      characters.forEach(characterUrl => {
        // Extract the character ID from the URL
        const characterId = characterUrl.split('/').slice(-2, -1)[0]; // Extract ID from URL

        if (characterId.includes(targetId)) {
          request(characterUrl, (error, response, body) => {
            if (error) {
              console.error('Error fetching character details:', error);
              process.exit(1);
            }

            if (response.statusCode !== 200) {
              console.error('Failed to retrieve character details. Status code:', response.statusCode);
              process.exit(1);
            }

            try {
              const characterData = JSON.parse(body);
              console.log(characterData.name);
            } catch (parseError) {
              console.error('Error parsing character JSON:', parseError);
              process.exit(1);
            }
          });
        }
      });
    } catch (parseError) {
      console.error('Error parsing movie JSON:', parseError);
      process.exit(1);
    }
  });
}

// Fetch movie details
getCharacterNames(movieUrl);
