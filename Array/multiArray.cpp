#include <iostream>
using namespace std;


int main() {
    
    /* Showing multidimensional array construction */
    // Declare 2D array of size 2x3 
    int numbers2d[2][3];

    // Declare 3D Array of size 2x3x3
    int numbers3d[2][3][2];

    // Initialize a 2D array
    int numbers2d_init[2][3] = {
        {1,2,3},
        {4,5,6}
    };

    // Initialize a 3D array
    int numbers3d_init[2][3][2] = {
        { {1, 2}, {3, 4}, {5, 6} },
        { {7, 8}, {9, 10}, {10, 11} }
    };

    // Dynamic 2D array using pointers
    int rows = 2, cols = 3;
    int** dynamic2d = new int*[rows];   // Row of pointers which is why its int*
    for (int i = 0; i < rows; i++) {
        dynamic2d[i] = new int[cols];   // col of the actual int being pointed to
    }

    // Deallocate dynamic 2D array
    for (int i = 0; i < rows; i++) {
        delete[] dynamic2d[i];          // Deletes the arrays inside the array
    }
    delete[] dynamic2d;              // Deletes the array itself

    /* Accessing elements in multi-dimensional array */
    int funNumbers[2][3][2] = {
        { {1, 2}, {3, 4}, {5, 6} },
        { {7, 8}, {9, 10}, {10, 11} }
    };

    cout << "Element at (0,1,1) is " << funNumbers[0][1][1] << endl;

    // Modify elements
    funNumbers[0][1][1] = 10;
    cout << "New Element at (0,1,1) is " << funNumbers[0][1][1] << endl;


    /* Traversing multi-dimensional arrays */

    // Index based
    /* cout << "2D array traversal (index-based):" << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << numbers2d[i][j] << " ";
        }
        cout << endl;
    } */

    // Range based
    cout << "3D array traversal:" << endl;
    for (auto& row : funNumbers) {
        for (auto& subRow : row) {
            for (int value : subRow) {
                cout << value << " ";
            }
            cout << "| ";
        }
        cout << endl;
    }

    return 0;
}