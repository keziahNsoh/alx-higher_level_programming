#!/usr/bin/node

const { dict } = require('./101-data');

let occurrencesDict = {};

for (let userId in dict) {
  let occurrences = dict[userId];

  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [];
  }

  occurrencesDict[occurrences].push(userId);
}

console.log(occurrencesDict);
