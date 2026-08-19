class Solution:
    def reverseWord(self, arr, left, right):
        # Travese through array and swap elements
        while (left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def find_wordEnd(self, arr, start):
        wordEnd = start

        # Iterate until a space is encountered
        while wordEnd < len(arr) and arr[wordEnd] != " ":
            wordEnd += 1
        
        return wordEnd - 1    # -1 To align it to last char, otherwise index error
    
    def reverse_word_order(self, s: str) -> str:
        # Reverses the string - setup for later
        # ex. pasta -> atsap
        s = s[::-1]

        # Splits the string, and then makes it into a new list of chars so it can be mutated
        modifiedString = list(" ".join(s.split()))

        # Words are in correct place, but letters are backwards
        # Reverse the words themselves
        wordStart = 0

        while wordStart < len(modifiedString):
            # Look for start of word (if not first word, then its after space)
            if modifiedString[wordStart] == " ":
                wordStart += 1
                continue
            
            # Look for end of word
            wordEnd = self.find_wordEnd(modifiedString, wordStart)

            # Look for reverseWord in this class
            self.reverseWord(modifiedString, wordStart, wordEnd)

            # Move start to next word (skips the space check - more optimized)
            wordStart = wordEnd + 1                

        return "".join(modifiedString)      # Revert back to a string