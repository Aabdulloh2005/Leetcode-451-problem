def reverse(x: int) -> int:
    a = str(x)[::-1]
    if x < 0:
        a = "-" + a[:-1]
    
    
    return int(a)
    

print(reverse(int(input())))