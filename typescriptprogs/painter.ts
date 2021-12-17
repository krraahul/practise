import {readFileSync} from 'fs';

const problem = {
    T: 0,
    tests: []
}

const input_data = readFileSync(0, 'utf-8').trim().split('\n');

let count = 0;
input_data.forEach((line) => {
  if(problem.T === 0) {
      problem.T = parseInt(line)
  }else {
      if(count%2 === 0) {
          problem.tests.push(line.split(''));
      }
  }
  count++;
});

console.log(problem.tests)