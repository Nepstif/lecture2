class CyclicIterator:

    def __init__(self, container):
        self.container = container
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        element = self.container[self.current % len(self.container)]
        self.current += 1
        return element


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
