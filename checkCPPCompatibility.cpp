// know the cpp compiler compatibility
// Execute this code

// While compiling write following syntax
// g++ -o <executable file name> <filename>.cpp -std=c++<version you need> && ./<executable file name>
 
// -o flag writes the object file in the mentioned desired file.


// Example : 
 
// g++ -o main cppCompatibility.cpp -std=c++11 && ./main ==> If this compiles and executes then ur compiler supports c++11 standard
// g++ -o exeFile cppCompatibility.cpp -std=c++17 && ./exeFile
// g++ -o main cppCompatibility.cpp -std=c++20 && ./main

#include<iostream>
using namespace std;

int main() {
	cout << __cplusplus;
	return 0;
}
