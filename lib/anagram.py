class Anagram:

    def __init__(self, word="word"):
        self.word = word

    def match(self, anagram_list):
        anagrams = []
        for anagram in anagram_list:
            if sorted(self.word) == sorted(anagram):
                anagrams.append(anagram)
        return anagrams