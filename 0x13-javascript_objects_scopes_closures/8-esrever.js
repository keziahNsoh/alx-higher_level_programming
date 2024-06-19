#!/usr/bin/node

exports.esrever = function(list) {
  let reversedList = [];
  // Iterate backwards through the original list and push elements to reversedList
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
