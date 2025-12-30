def solution(n):
    fib = [0, 1]
    
    for i in range(2, n + 1):
        val = (fib[i-1] + fib[i-2]) % 1234567
        fib.append(val)
        
    return fib[n]