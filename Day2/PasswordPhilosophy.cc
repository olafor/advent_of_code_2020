#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>

int sumValidPasswords{0};

int main(int argc, char** argv) {

    while (!std::cin.eof()) {

        int i = std::cin.peek();
        if (!std::isdigit(i))
            break;

        std::string line;
        std::string range;
        std::string password;

        int divider;
        int min;
        int max;

        std::getline(std::cin, line);

        std::stringstream ss{line};
        
        ss >> range;

        divider = range.find('-');

        min = std::stoi(range.substr(0, divider));
        max = std::stoi(range.substr(divider + 1, range.size() - divider));

        std::string str;
        ss >> str;

        char letter;
        letter = str[0];

        ss >> password; 

        int occurences = std::count(password.begin(), password.end(), letter);

        if (occurences >= min && occurences <= max)
            sumValidPasswords++;
    }
    std::cout << sumValidPasswords << std::endl;
}
