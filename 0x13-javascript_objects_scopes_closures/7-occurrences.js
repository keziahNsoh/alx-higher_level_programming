#!/usr/bin/node

exports.nbOccurences = function(list, searchElement) {
  let count = 0;
  // Loop through the list to count occurrences of searchElement
  for (let element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
