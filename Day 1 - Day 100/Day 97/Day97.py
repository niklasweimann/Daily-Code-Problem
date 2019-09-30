class timeMap():
    def __init__(self):
        self.data = {}

    def set(self, key, value, time):
        if self.data.get(key) is None:
            timeDict = {}
            timeDict[time] = value
            self.data[key] = timeDict
            return
        keyNode: dict = self.data.get(key)
        if keyNode.get(time) is None:
            keyNode[time] = value
            return
        keyNode[time] = value

    def get(self, key, time):
        key: dict = self.data.get(key)
        if key is None:
            return None

        if key.get(time) is None:
            closest = max(item for item in key.keys() if item < time)
            return key[closest]
        return key[time]


d = timeMap()
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 2)  # set key 1 to value 2 at time 2
print(d.get(1, 1))  # get key 1 at time 1 should be 1
print(d.get(1, 3))  # get key 1 at time 3 should be 2

d.set(1, 1, 5)  # set key 1 to value 1 at time 5
print(d.get(1, 0))  # get key 1 at time 0 should be 1
print(d.get(1, 10))  # get key 1 at time 10 should be 1

d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 0)  # set key 1 to value 2 at time 0
print(d.get(1, 0))  # get key 1 at time 0 should be 2
