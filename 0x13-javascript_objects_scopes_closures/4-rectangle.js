#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
      if (w > 0 && h > 0) {
	  this.width = w;
	  this.height = h; }
  }
  print (char = 'X') {
    for (let i = 0; i < this.height; ++i) {
      let j = 0;

      for (; j < this.width; ++j) {
        process.stdout.write(char);
      }

      if (j === this.width) {
        console.log('');
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
