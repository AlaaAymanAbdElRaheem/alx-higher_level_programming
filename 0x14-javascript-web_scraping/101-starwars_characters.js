#!/usr/bin/node

const { resolve } = require('path');
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, async function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, function (err, response, body) {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
