#!/usr/bin/node

const args = process.argv.slice(2);
const integers = args.map(Number);

integers.sort((a, b) => b - a);

if (integers.length <= 1){
	console.log(0);
}else{
	let secondBiggest = integers[1];
	console.log(secondBiggest);
}
