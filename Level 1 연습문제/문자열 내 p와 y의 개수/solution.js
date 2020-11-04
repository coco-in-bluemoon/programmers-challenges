'use strict';
const assert = require('assert');

function solution(s) {
    let counter_p = 0;
    let counter_y = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i].toLowerCase() == 'p') {
            counter_p += 1;
        } else if (s[i].toLowerCase() == 'y') {
            counter_y += 1;
        }
    }

    return counter_p === counter_y;

}

let s = 'pPoooyY';
let my_answer = solution(s);
assert(my_answer);
