class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0 :
            raise ValueError
        self.size += n


    def withdraw(self, n):
        if n < 0 :
            raise ValueError
        if self.size < n:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if 0 > capacity or 12 < capacity :
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if 0 > size or size > self.capacity :
            raise ValueError
        self._size = size

def main():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    print(jar) # 결과 확인용 추가
    print(f"Capacity: {jar.capacity}")
    print(f"Size: {jar.size}")

if __name__ == "__main__":
    main()
