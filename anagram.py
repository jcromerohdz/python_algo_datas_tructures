'''
Given two strings s1 and s2,
check if they are anagramas.
Two strings are anagrams if they are made of the same
characters with the  same frequencies.

iput:
s1="danger"
s2="garden"

output: true
'''
#Solution 1
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    
    return True
    
s1 = "danger"
s2 = "garden"

print(are_anagrams(s1, s2))

from collections import Counter

#Solution 2
def are_anagramas_2(s1, s2):
    if len(s1) != len(s2):
        return False
    print(Counter(s1))
    print(Counter(s2))
    return Counter(s1) == Counter(s2)

print(are_anagramas_2(s1, s2))

# Solution 3
def are_anagramas_3(s1, s2):
    if len(s1) != len(s2):
        return False
    print(sorted(s1))
    print(sorted(s2))
    return sorted(s1) == sorted(s2)

print(are_anagramas_3(s1, s2))