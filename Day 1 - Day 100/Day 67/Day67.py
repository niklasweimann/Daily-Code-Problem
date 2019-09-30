class Node:
    def __init__(self, value: str):
        self.value = value
        self.frq = 0

    def __repr__(self):
        return "<Frequency = {0}; Value = {1};> ".format(self.frq, self.value)


class LRU:
    def __init__(self, cache_size):
        self.data = []
        self.size = cache_size
        self.use_size = 0
        self.pos = dict()

    def set(self, value: str):
        new_Node = Node(value)
        if self.size <= self.use_size:
            self.pos.pop(self.data[len(self.data) - 1].value)
            del (self.data[len(self.data) - 1])
            self.data.append(new_Node)
            self.pos[value] = len(self.data) - 1
            return
        self.data.append(new_Node)
        self.pos[value] = len(self.data) - 1
        self.use_size += 1
        pass

    def get(self, value: str):
        if self.pos[value] is None:
            return None
        current_data: Node = self.data[self.pos[value]]
        current_node_pos = self.pos.get(current_data.value)
        if current_data:
            current_data.frq += 1
            if current_node_pos > 0 and current_data.frq >= self.data[current_node_pos-1].frq:
                cur = self.data[self.pos[value]]
                self.data[self.pos[value]] = self.data[current_node_pos-1]
                self.data[current_node_pos-1] = cur
                swaped_index = self.pos[value]
                self.pos.pop(self.data[self.pos[value]].value)
                self.pos.pop(self.data[current_node_pos-1].value)
                self.pos[self.data[current_node_pos -
                                   1].value] = current_node_pos-1
                self.pos[self.data[swaped_index].value] = 1
        return current_data

    def display(self):
        res = ""
        for i in self.data:
            res += "<{0}>".format(i)
        return res


cache = LRU(3)
cache.set("a")
cache.set("b")
cache.set("c")
cache.set("d")
cache.set("e")
print(cache.display())
print(cache.get("a"))
print(cache.get("a"))
print(cache.get("a"))
print(cache.get("b"))
print(cache.get("b"))
print(cache.display())
cache.set("h")  # e should be replaced since its least recently used
print(cache.display())
cache.get("h")
cache.get("h")
cache.get("h")
cache.get("h")
print(cache.display())  # h should be in pos 1 in cache
