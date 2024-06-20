#!/usr/bin/node

const args = process.argv.slice(2);
let max = 0;
let secondMax = 0;

if (!(args.length === 1) || !(args.length === 0)) {
  for (let i = 0; i < args.length; i++) {
    const x = parseInt(args[i]);
    if (x > max) {
      secondMax = max;
      max = args[i];
    } else if (x > secondMax) {
      secondMax = x;
    }
  }
}

console.log(secondMax);
