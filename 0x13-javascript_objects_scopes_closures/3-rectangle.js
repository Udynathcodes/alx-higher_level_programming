#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.create(null);
    }
  }

  print () {
    let x;
    let y;
    let str = '';
    for (x = 0; x < this.height; x++) {
      str = '';
      for (y = 0; y < this.width; y++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;
