'use strict';
const assert = require('assert');

function solution(a, b) {
    const DAYS = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    const date = new Date(2016, a-1, b);
    const day_index = date.getDay();
    return DAYS[day_index];
}

const my_answer =  solution(5, 24);
const answer = 'TUE';
assert(my_answer == answer);
