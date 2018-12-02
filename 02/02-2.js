#!/usr/bin/node

const fs = require('fs');

const lines = fs.readFileSync('input.txt', 'utf8').split('\n').map((line) => line.split(''));

for (let i = 0; i < lines.length; i++) {
  const line1 = lines[i];
  for (let j = 0; j < i; j++) {
    const line2 = lines[j];
    // The map() call here is a zip function
    const matches = line1.map((c, k) => [c, line2[k]]).filter(pair => pair[0] == pair[1]);
    if (matches.length == line1.length - 1) {
      console.log(matches.map((pair) => pair[0]).join(''));
    }
  }
}
