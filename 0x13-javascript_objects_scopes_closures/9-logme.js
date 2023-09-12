#!/usr/bin/node

let id = 0;
exports.logMe = function (item) {
  console.log(id + ': ' + item);
  id += 1;
};
