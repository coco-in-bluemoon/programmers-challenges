'use strict';

const assert = require('assert');

function solution(s) {
    const length = s.length;
    let middle_index = length / 2;
    let answer = s.charAt(middle_index);
    if (length % 2 == 0) {
        answer = s.charAt(middle_index - 1) + answer
    }
    return answer
}

let my_answer = solution('abcde');
let answer = 'c'
assert(my_answer == answer)

my_answer = solution('qwer')
answer = 'we'
assert(my_answer == answer)
