def is_anagram(word1,word2):
    if sorted(word1) == sorted(word2):
        print(word1, "and" , word2, "are anagrams")
    else:print(word1, "and" , word2, "are not anagrams")

is_anagram("moon", "noom")

