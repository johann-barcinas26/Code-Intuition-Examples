#include <iostream>
using namespace std;

int main() {

    // Declaring array of fixed size 3 (unitialized)
    int numbers[3];

    // Declare array and initialize values
    int nums2[] = {1, 3, 5, 1, 6};

    // Declare and initialize with fixed size
    int nums3[3] = {5, 6, 7};

    // Partial initialization
    int nums4[4] = {1, 2};

    // Create array dynamically using new (heap allocation)
    int size_nums = 5;
    int *nums5 = new int[size_nums];

    // Creating and intializing a dynamic array
    int *nums6 = new int[5]{1, 2, 3, 4, 5};

    // Dynamically allocated arrays MUST be deleted
    // -> Memory managment: Do not want a leak
    delete[] nums5;
    delete[] nums6;


    /* Array Functions: Accessing, modifying*/

    int nums7[] = {1, 2, 3, 4, 5, 1};

    // Accessing an element
    cout << "Here is the last element: " << nums7[5] << endl;

    // Modifying an element
    nums7[5] = 6;
    cout << "Here is the updated change: " << nums7[5] << endl;


    /* Array Traversal */
    int traverseThis[] = {9, 5, 2, 7, 7};
    int size_a = 5;

    // Traversal with index-based for loop
    for (int i = 0; i < size_a;  i++) {
        cout << traverseThis[i] << " ";
    }
    cout << endl;

    // Traversal with range-based for loop
    for (int value : traverseThis) {
        cout << value << " ";
    }
    cout << endl;

    // Traversal with pointer arithmetic
    for (int *ptr = traverseThis; ptr < traverseThis + size_a; ptr++) {
        cout << *ptr << " ";
    }
    cout << endl;

    // Reverse Traversal
    for (int index = size_a - 1; index >= 0; index--) {
        cout << traverseThis[index] << " ";
    }
    cout << endl;


    return 0;
}