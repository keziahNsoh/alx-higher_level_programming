#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeId = 18;
    const count = films.reduce((acc, film) => {
      return acc + (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`) ? 1 : 0);
    }, 0);
    console.log(count);
  }
});
