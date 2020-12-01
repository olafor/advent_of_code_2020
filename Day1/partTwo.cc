#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    std::vector<int> allNums; 
    int newNum;

    while (1) {
        if (!std::cin)
            break;

        std::cin >> newNum;
        allNums.push_back(newNum); 
    }

    for (int i{0}; i < allNums.size(); ++i) {
        for (int j{1}; j < allNums.size() - 1; ++j) {
            for (int k{1}; k < allNums.size() - 1; ++k) {
                if (allNums[i] + allNums[j] + allNums[k] == 2020) {
                    std::cout << allNums[i] << " + " << allNums[j] << " + " 
                        << allNums[k] << std::endl;
                    std::cout << allNums[i] * allNums[j] * allNums[k] << std::endl; 
                    return 0;
                } 
            }
        }  
    }
}
