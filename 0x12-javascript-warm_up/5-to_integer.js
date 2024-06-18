#!/usr/bin/node

const arg = process.argv[2];

// Try's to convert the argument to an integer
const num = parseInt(arg);

// Check if the conversion was successful and if it's a valid number
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
