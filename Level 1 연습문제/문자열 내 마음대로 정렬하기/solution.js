'use strict';
const assert = require('assert');

function solution(strings, n) {
    strings.sort(
        function (a, b) {
            const char_a = a[n];
            const char_b = b[n];

            if (char_a == char_b) {
                return (a > b) - (a < b);
            } else {
                return (char_a > char_b) - (char_a < char_b);
            }
        }
    );
    return strings;
}

let strings = ['sun', 'bed', 'car'];
let n = 1;
let my_answer = solution(strings, n);
let answer = ['car', 'bed', 'sun'];
assert(JSON.stringify(my_answer) == JSON.stringify(answer));
