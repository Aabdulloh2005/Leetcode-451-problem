class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)[::-1]
        if x < 0:
            a = "-" + a[:-1]
        a = int(a)
        return a if -2147483648<a<2147483647 else 0