#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episodeId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
