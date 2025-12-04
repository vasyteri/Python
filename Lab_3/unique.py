class Unique(object):

    def __init__(self, items, **kwargs):

        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            item = next(self.items)
            

            if self.ignore_case and isinstance(item, str):
                check_item = item.lower()
            else:
                check_item = item
            

            if check_item not in self.seen:
                self.seen.add(check_item)
                return item



if __name__ == "__main__":
    print("Test 1 - числа:")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data):
        print(item, end=" ")
    
    print("\n\nTest 2 - строки без ignore_case:")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data):
        print(item, end=" ")
    
    print("\n\nTest 3 - строки с ignore_case=True:")
    for item in Unique(data, ignore_case=True):
        print(item, end=" ")
    print()