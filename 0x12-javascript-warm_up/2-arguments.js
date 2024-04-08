#!/usr/bin/node
/*  script that prints a message depending of the number of arguments passed */
const numArgs = process.argv.lenght;

if (numArgs === 2){
	console.log('No argument');
}else if (numArgs === 3){
	console.log('Argument found');
}else{
	console.log('Arguments found');
}
