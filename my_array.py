# insertion, deletion and random access of array.

class MyArray:
    def __init__(self, capasity: int):
        self._data = []
        self._capasity = capasity
        
    def __getitem__(self, position: int) -> object:
        return self._data[position]
        
    def __setitem__(self, index: int, value:int ):
        self._data[index] = value
        
    def __len__(self) -> int:
        return len(self.data)
        
    def __iter__(self):
        for item in self._data:
            yield item
            
    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None
            
    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False
            
    def insert(self, index: int, value: int) -> bool:
        if len(self._data) >= self._capasity:
            return False
        else:
            return self._data.insert(index, value)
            
    def print_all(self):
        for item in self._data:
            print(item)
            
def test_myarray():
    array = MyArray(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_myarray()            