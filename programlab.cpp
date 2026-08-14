// programlab.cpp

#include <iostream>

void enterNumber() {
    std::cout << "Enter a number: "; 
    int x {};
    std::cin >> x;
    std::cout << "You entered " << x << '\n' << std::endl;  // This line makes a new line -> big gap though
    std::cout << "Thank you for entering your number.";     // Best practice to outline a newline whenever a new line is complete
    std::cout << "\n Your work is appreciated \n";
}

void enterTwoNumbers() {
    std::cout << "Enter two numbers: ";

    int z{};
    int y{};
    std::cin >> z >> y;         // get two numbers and store then x and y respectively
    std::cout << "The numbers are "<< z << " and "<< y << "\n";
}

void enterTwoLetters() {
    std::cout << "Enter two letters: ";
    
    char let1{};
    std::cin >> let1;

    char let2{};
    std::cout << "Okay now the second letter: ";
    std::cin >> let2;

    std::cout << "The two letters are "<< let1 << " and " << let2 << "\n";
}

// Apart of the quiz on learncpp
void enterThreeNumbers() {
    std::cout << "Enter three numbers: ";
    
    int first{};
    std::cin >> first;
    std::cout << "Now the second: ";

    int second{};
    std::cin >> second;
    std::cout << "Now the third: ";

    int third{};
    std::cin >> third;
    std::cout << "You entered: " << first << ", " << second << ", and " << third;
}

int main() {

    //enterNumber();
    //std::cout << std::endl;

    //enterTwoNumbers();
    //std::cout << std::endl;
    
    //enterTwoLetters();
    
    enterThreeNumbers();

    return 0;
}
