using namespace std;
#include <iostream>
#include <string>

class Solution {
public:
    string reverseWords(string sentence) {
        int length = sentence.length();
        int cursor = 0;
        
        while (cursor < length) {
            // Check for spaces
            if (sentence[cursor] == ' ') {
                cursor++;
                continue;
            }

            // Pointers to find the start and end of word
            int startWord = cursor;
            int endWord = cursor;

            // Finds the end of the word
            while (endWord < length && sentence[endWord] != ' ') {
                endWord++;
            }

            // Reverse word
            int left = startWord;
            int right = endWord - 1;
            while (left < right) {
                swap(sentence[left], sentence[right]);
                left++;
                right--;
            }

            // Move cursor up to next word
            cursor = endWord;
        }

        return sentence;
    }
};
