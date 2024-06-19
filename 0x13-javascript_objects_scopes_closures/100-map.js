#!/usr/bin/node

const { list } = require('./100-data');

// Compute a new list where each value is multiplied by its index
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
