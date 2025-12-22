def solution(s):
    s_split = s.split(" ")
    
    new_list = []
    
    for word in s_split:
        new_word = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        new_list.append(new_word)

    return " ".join(new_list)