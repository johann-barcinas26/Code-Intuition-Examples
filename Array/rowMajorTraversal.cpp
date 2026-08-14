#include <iostream>
#include <vector>
using namespace std;

vector<int> rowMajorTraversal(vector<vector<int>> &matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    vector<int> result;
        
    if (matrix.empty()) {
         return vector<int>();
    }

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++ )
        result.push_back(matrix[row][col]);
    }
        
    return result;
}

int main() {
    
    return 0;
}