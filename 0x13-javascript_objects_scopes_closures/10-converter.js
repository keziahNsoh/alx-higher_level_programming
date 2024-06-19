#!/usr/bin/node

exports.converter = function(base) {
  // Recursive function to convert number to specified base
  function convert(num) {
    if (num >= base) {
      convert((num / base) | 0);
    }
    process.stdout.write((num % base).toString());
  }

  return convert;
};
