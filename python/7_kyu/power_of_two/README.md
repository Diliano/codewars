# Power of two
 
**Kata Link:** 

[Power of two on Codewars](https://www.codewars.com/kata/534d0a229345375d520006a0/train/python)

**Challenge/Instructions:**

Complete the function `power_of_two` that determines if a given non-negative integer is a [power of two](https://en.wikipedia.org/wiki/Power_of_twohttps://en.wikipedia.org/wiki/Power_of_two). From the corresponding Wikipedia entry:

	a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent.

You may assume the input is always valid.

**Examples:**

```python
power_of_two(1024) ==> True
power_of_two(4096) ==> True
power_of_two(333)  ==> False
```

Beware of certain edge cases - for example, `1` is a power of `2` since `2^0 = 1` and `0` is not a power of `2`.