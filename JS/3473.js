var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function main(){
    const num = parseInt(lines.shift());
    console.log(num+1);
}

main();