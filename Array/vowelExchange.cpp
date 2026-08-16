#include <iostream>
#include <algorithm>
using namespace std;

// Helper method to check if the selected character is a vowel
bool isVowel(char c) {
    switch(tolower(static_cast<unsigned char>(c))) {
        case 'a' : case 'e' : case 'i' : case 'o' : case 'u':
            return true;
        default:
            return false;
    }
}


string vowelExchange(string s) {
    // Initialize two pointers
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        // Check if the character you are on is a vowel first
        if (!isVowel(s[left])) { left++; continue; }          // Won't stop until it hits a vowel
        if (!isVowel(s[right])) { right--; continue; }        // Same

        // If vowel detected for both pointers
        swap(s[left], s[right]);
        left++;
        right--;
    }
    
    return s;
}