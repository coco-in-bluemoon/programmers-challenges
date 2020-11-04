'use strict';
let assert = require('assert');

function solution(arr) {
    let answer = new Array();
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] != arr[i+1]) {
            answer.push(arr[i]);
        }
    }

    return answer;
}

let arr = [1, 1, 3, 3, 0, 1, 1];
let my_answer = solution(arr);
let answer = [1, 3, 0, 1];
assert(JSON.stringify(my_answer) == JSON.stringify(answer));

arr = [4, 4, 4, 3, 3];
my_answer = solution(arr);
answer = [4, 3];
assert(JSON.stringify(my_answer) == JSON.stringify(answer));
