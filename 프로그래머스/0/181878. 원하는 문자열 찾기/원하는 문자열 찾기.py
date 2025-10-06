def solution(myString, pat):
    lower_myString = myString.lower()
    lower_pat = pat.lower()

    if lower_pat in lower_myString:
        return 1
    else:
        return 0