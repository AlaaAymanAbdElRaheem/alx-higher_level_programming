#!/usr/bin/node

const baseSquare = require('./5-square.js');

module.exports = class Square extends baseSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
