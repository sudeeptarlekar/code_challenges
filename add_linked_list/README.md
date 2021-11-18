[![](https://img.shields.io/badge/difficulty-easy-brightgreen.svg)]()

# Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

### Example 1

3 -> 4 -> 5

7 -> 8 -> 2
_____________
0 -> 3 -> 8

```
Input: List1 = [3, 4, 5], List2 = [7, 8, 2]
Output: 0 -> 3 -> 8
explanation: 543 + 287 = 830
```

### Example 2

0
0
_________
0

```
Input: List1 = [0], List2 = [0]
Output: 0
Explanation: 0 + 0
```

### Example 3

9 -> 9 -> 9 -> 9 -> 9

9 -> 9 -> 9
_______________________
8 -> 9 -> 9 -> 0 -> 0 -> 1

```
Input: List1 = [9, 9, 9, 9, 9], List2 = [9, 9, 9]
Output: [8, 9, 9, 0, 0, 1]
Explanation: 99999 + 999 = 100998
```
