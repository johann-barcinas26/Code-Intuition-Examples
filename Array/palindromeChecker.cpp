#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool palindromeChecker(string s) {

    // Convert letters to lowercase
    for (char &c : s) {
        c = tolower(static_cast<unsigned char>(c));
    }

    // Remove non-alphanumeric characters (Erase-remove idiom)
    s.erase(remove_if(s.begin(), s.end(), [](unsigned char c) {
        return !isalnum(c);
    }), s.end());

    // Use two pointers to compare the string (now converted to proper format)
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;

}

int main() {
    return 0;
}