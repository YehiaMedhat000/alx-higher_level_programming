#!/usr/bin/node

exports.esrever = function (list) {
  let ret = [];
  if (!(list === undefined)) {
    for (let i = list.length; i > 0; i--) {
      ret[list.length - i] = list[i - 1];
    }
  }
  return ret;
};
