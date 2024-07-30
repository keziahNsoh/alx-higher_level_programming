#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2]; // File path from the command-line arguments

fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.error(err); // Print the error object
  } else {
    console.log(data); // Print the file content
  }
});
