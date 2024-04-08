#!/usr/bin/node
function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }

  return num * factorial(num - 1);
}

let x;
const [, , firstArg] = process.argv;

if (firstArg) {
  x = parseInt(firstArg, 10);
  console.log(factorial(x));
} else {
  console.log(1);
}
