#!/usr/bin/node
/* function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let x = 0;
  let occurrencesCount = 0;

  while (x < len) {
    if (list[x] === searchElement) {
      occurrencesCount++;
    }
    x++;
  }
  return occurrencesCount;
};
