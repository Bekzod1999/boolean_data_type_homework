from math import sqrt

def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    y=sqrt(a)
    return y % 1 == 0
x=main(16)
print(x)