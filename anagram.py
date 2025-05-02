def anagram(s, t):

    return sorted(s) == sorted(t)


print(anagram("rat", "car"))