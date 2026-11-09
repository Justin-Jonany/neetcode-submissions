class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderedDict = OrderedDict()

    def get(self, key: int) -> int:
        if self.orderedDict.get(key, None):
            self.orderedDict.move_to_end(key)
        return self.orderedDict.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self.orderedDict[key] = value
        self.orderedDict.move_to_end(key)
        if len(self.orderedDict) > self.capacity:
            self.orderedDict.popitem(last=False)


