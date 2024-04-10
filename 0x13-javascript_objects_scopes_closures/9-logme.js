#!/usr/bin/node
/* function that prints the number of arguments already printed */
let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};
