#!/usr/bin/node

const fs = require('fs');
const path = require('path');

// Check if all three arguments are provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

try {
  // Read contents of fileA and fileB
  const contentA = fs.readFileSync(fileA, 'utf8');
  const contentB = fs.readFileSync(fileB, 'utf8');

  // Concatenate contents of fileA and fileB
  const concatenatedContent = contentA + '\n' + contentB; // Adding a newline between contents

  // Write concatenated content to fileC
  fs.writeFileSync(fileC, concatenatedContent);

  console.log(`Concatenation successful! ${fileA} and ${fileB} were concatenated and saved to ${fileC}`);
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}
