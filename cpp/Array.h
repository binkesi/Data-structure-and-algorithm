#pragma once
#include <iostream>

template <class T>
class Array {
public:
	explicit Array(const int&);
	Array(const int&, const T&);
	~Array();
	Array(const Array&);
	Array& operator= (const Array&);
	T& operator[] (size_t);

private:
	int size;
	T* ptr;
};
