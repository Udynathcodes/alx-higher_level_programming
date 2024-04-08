#!/usr/bin/node

const myVar = process.argv.slice(2);

if (myVar.length > 0){
	const firstArg = parseInt(myVar[0]);
	if (!isNaN(firstArg)){
		console.log(`My number: ${firstArg}`);
	}else{
		console.log('Not a number');
	}
}else{
	console.log('No arguments provided');
}
