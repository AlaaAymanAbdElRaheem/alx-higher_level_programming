#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  const completed = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 0;
      }
      completed[task.userId] += 1;
    }
  }
  console.log(completed);
});
