#include <iostream>
#include "Array.h"
#include <algorithm>

template <class T>
Array<T>::Array(const int& init_size)
	:size(init_size), ptr(new T[init_size]()) {}

template <class T>
Array<T>::Array(const int& init_size, const T& init_value)
	: size(init_size), ptr(new T[init_size]) {
	for (int i = 0; i < size; ++i) {
		ptr[i] = init_value;
	}
}

template <class T>
Array<T>::~Array() {
	delete[]ptr;
}

template <class T>
T & Array<T>::operator[](size_t index)
{
	return ptr[index];
}

template <class T>
Array<T>::Array(const Array& rhs) {
	size = rhs.size;
	ptr = new T[size];
	for (int i = 0; i < size; ++i) {
		ptr[i] = rhs.ptr[i];
	}
}

template <class T>
Array<T>& Array<T>::operator= (const Array& rhs) {
	Array copy(rhs);
	std::swap(ptr, copy.ptr);
	std::swap(size, copy.size);
	return copy;
}