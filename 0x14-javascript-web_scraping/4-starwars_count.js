#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided
const apiUrl = process.argv[2];
if (!apiUrl) {
  console.error('Usage: ./101-starwars_characters.js <api_url>');
  process.exit(1);
}

// Define the character ID for Wedge Antilles
const wedgeId = 18;

// Function to count films featuring Wedge Antilles
function countFilmsFeaturingCharacter (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error('Failed to retrieve data. Status code:', response.statusCode);
      process.exit(1);
    }

    try {
      const films = JSON.parse(body).results;
      const idSubstring = `/${wedgeId}/`;
      const count = films.reduce((acc, film) => (
        acc + (film.characters.some(characterUrl => characterUrl.includes(idSubstring)) ? 1 : 0)
      ), 0);
      console.log(count);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
      process.exit(1);
    }
  });
}

// Invoke the function
countFilmsFeaturingCharacter(apiUrl);
