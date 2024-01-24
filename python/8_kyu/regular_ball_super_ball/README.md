# Regular Ball Super Ball

## Kata Link

[Regular Ball Super Ball on Codewars](https://www.codewars.com/kata/53f0f358b9cb376eca001079/train/python)

## Challenge/Instructions

Create a class `Ball`. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular".

```python
ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"