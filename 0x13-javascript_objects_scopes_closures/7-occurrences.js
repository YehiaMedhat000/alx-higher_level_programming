#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  if (!(list === undefined) || !isNaN(searchElement)) {
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) {
        n++;
      }
    }
  }
  return n;
};
