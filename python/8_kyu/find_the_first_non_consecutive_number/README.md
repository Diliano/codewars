# First non-consecutive number

## Kata Link

[First non-consecutive number on Codewars](https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python)

## Challenge/Instructions

Your task is to find the first element of an array that is not consecutive.

By not consecutive, we mean not exactly 1 larger than the previous element of the array.

E.g., If we have an array `[1,2,3,4,6,7,8]`, then `1`, `2`, `3`, and `4` are all consecutive, but `6` is not, so that's the first non-consecutive number.

If the whole array is consecutive, then return `None`.

The array will always have at least 2 elements and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative, and the first non-consecutive could be either too!

Can you write a solution that will return `None` for both `[]` and `[ x ]` though? (This is an empty array and one with a single number and is not tested for, but you can write your own example test. )

**Examples (Input --> Output):**

```python
[1,2,3,4,6,7,8] --> 6
[1,2,3,4,5,6,7,8] --> None
```