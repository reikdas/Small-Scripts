#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
int main()
{
    std::vector<std::vector<double>> arr;
    std::string str;
    std::ifstream in; in.open("april.txt");
    while(std::getline(in, str))
    {
        std::stringstream ss(str);
        int index=0;double n;
        std::vector<double> arr1;
        while(ss>>n)
            arr1.emplace_back(n);
        arr.emplace_back(arr1);
    }
    in.close();
    for(auto& i:arr)
    {
        for(auto& j:i)
            std::cout<<j<<" ";
        std::cout<<"\n";
    }
}