#!/usr/bin/node
/*  class Square that defines a square and inherits from Square of 5-square.js */
const Square = require('./5-square');

class SquareTwo extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let str = '';
    for (let x = 0; x < this.height; x++) {
      str = '';
      for (let y = 0; y < this.width; y++) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = SquareTwo;
