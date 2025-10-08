def solution(spell, dic):
    spell.sort()

    for w in dic:
        if len(w) != len(spell):
            continue

        if sorted(list(w)) == spell:
            return 1

    return 2