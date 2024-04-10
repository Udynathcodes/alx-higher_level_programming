#!/usr/bin/node
/* script that imports an array and computes a new array */
const mylist = require('./100-data').list;

const newList = mylist.map((num, index) => num * index);

console.log(mylist);
console.log(newList);
