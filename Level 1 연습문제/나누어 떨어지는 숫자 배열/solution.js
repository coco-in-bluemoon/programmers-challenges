'use strict';
const assert = require('assert');

function solution(arr, divisor) {
    let answer = new Array();

    for (let i = 0; i < arr.length; i++) {
        if(arr[i] % divisor == 0) {
            answer.push(arr[i]);
        }
    }

    if (answer.length > 0) {
        answer = answer.sort(function (a, b) {return a - b;});
    } else {
        answer.push(-1);
    }
    return answer
}

let arr = [5, 9, 7, 10];
let divisor = 5
let my_answer = solution(arr, divisor);
let answer = [5, 10]
assert(JSON.stringify(my_answer) == JSON.stringify(answer));

arr = [2, 36, 1, 3];
divisor = 1;
my_answer = solution(arr, divisor);
answer = [1, 2, 3, 36];
assert(JSON.stringify(my_answer) == JSON.stringify(answer));

arr = [3, 2, 6];
divisor = 10;
my_answer = solution(arr, divisor);
answer = [-1];
assert(JSON.stringify(my_answer) == JSON.stringify(answer));
