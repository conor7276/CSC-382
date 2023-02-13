#Leetcode 49

#Optimal Solution O(n*log(n))
#  because of built in sorting algorithm 85.18% runtime 56% memory

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # key:str value: List[Str]
        for word in strs: # sort each word so they match the key Ex: eat -> aet, ate -> aet
            sorted_word = ''.join(sorted(word)) # append each word to list per key
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word].append(word)
        #print(anagrams)

        res = anagrams.values() # return values only
        return res
        