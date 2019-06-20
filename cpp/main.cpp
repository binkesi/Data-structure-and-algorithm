#include <iostream>
#include "Array.h"
#include "Array.cpp"

int main() {
	Array<int> a(5, 0);
	std::cout << a[3] << std::endl;
	Array<int> b(a);
	b[2] = 8;
	std::cout << b[2] << std::endl;
	Array<int> c(1);
	c = b;
	std::cout << c[2] << std::endl;
	return 0;
}