#!/usr/bin/node

const fs = require('fs');

contents = fs.readFileSync('input.txt', 'utf8');
lines = contents.split('\n');

for (let i = 0; i < lines.length; i++) {
  chars1 = lines[i].split('');
  for (let j = 0; j < i; j++) {
    chars2 = lines[j].split('');
    // The map() call here is a zip function
    matches = chars1.map((c, i) => [c, chars2[i]]).filter(pair => pair[0] == pair[1]);
    if (matches.length == chars1.length - 1) {
      console.log(matches.map((pair) => pair[0]).join(''));
    }
  }
}
