#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  let data;

  try {
    data = JSON.parse(body);
  } catch (err) {
    console.error('Error parsing movie data:', err);
    return;
  }

  const characterUrls = data.characters;

  if (!characterUrls || characterUrls.length === 0) {
    console.log('No characters found for the given movie ID');
    return;
  }

  let completedRequests = 0;

  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.error('Error fetching character data:', err);
      } else {
        let character;
        try {
          character = JSON.parse(body);
          console.log(character.name);
        } catch (parseErr) {
          console.error('Error parsing character data:', parseErr);
        }
      }
      completedRequests++;

      // Exit process when all requests are completed
      if (completedRequests === characterUrls.length) {
        process.exit(0);
      }
    });
  });
});
