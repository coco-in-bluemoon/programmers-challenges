'use strict';
const assert = require('assert');

function solution(s) {
    let s_list = Array.from(s);
    s_list.sort(function (a, b) {
        return (a < b) - (a > b);
    });
    const answer = s_list.join('');
    return answer;
}

let s = 'Zbcdefg';
let my_answer = solution(s);
let answer = 'gfedcbZ';
assert(my_answer == answer);
