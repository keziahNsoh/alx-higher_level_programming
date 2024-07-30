#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.reduce((acc, task) => {
      if (task.completed) {
        if (!acc[task.userId]) {
          acc[task.userId] = 0;
        }
        acc[task.userId]++;
      }
      return acc;
    }, {});
    console.log(completedTasks);
  }
});
