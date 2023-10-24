#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response) {
  if (err) {
    return console.log('code: 404');
  }
  console.log('code: ' + response.statusCode);
});
