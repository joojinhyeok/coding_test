def solution(ineq, eq, n, m):
    if ineq == '>':
        if eq == '!':
            if n > m:
                return 1
            else:
                return 0
        if eq == '=':
            if n >= m:
                return 1
            else: 
                return 0
    if ineq == '<':
        if eq == '!':
            if n < m:
                return 1
            else:
                return 0
        if eq == '=':
            if n <= m:
                return 1
            else: 
                return 0