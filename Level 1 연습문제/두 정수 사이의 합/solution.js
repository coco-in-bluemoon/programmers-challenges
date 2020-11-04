'use strict';
const assert = require('assert');


function solution(a, b) {
    let from = Math.min(a, b);
    let to = Math.max(a, b);

    let answer = 0;
    for(let number = from; number <= to; number++) {
        answer += number;
    }
    return answer;
}


let a = 3;
let b = 5;
let my_answer = solution(a, b);
let answer = 12;
assert(my_answer == answer);
