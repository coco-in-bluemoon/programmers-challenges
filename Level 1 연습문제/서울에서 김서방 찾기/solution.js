'use strict';
const assert = require('assert');


function solution(seoul) {
    for (let i = 0; i < seoul.length; i++) {
        if (seoul[i] === 'Kim') {
            return `김서방은 ${i}에 있다`;
        }
    }
}


let seoul = ['Jane', 'Kim'];
let my_answer = solution(seoul);
let answer = '김서방은 1에 있다';
assert(my_answer == answer);
