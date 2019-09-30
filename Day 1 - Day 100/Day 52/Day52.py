class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return "<Key = {0}; Value = {1};> ".format(self.key, self.value)


class LRU:
    def __init__(self, cache_size):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = cache_size
        self.data = dict()

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        prev_node = self.tail.prev
        node.next = self.tail
        node.prev = prev_node
        prev_node.next = node
        self.tail.prev = node

    def set(self, key, value):
        if key in self.data:
            node = self.data[key]
            self._remove(node)
        new_node = Node(key, value)
        self._add(new_node)
        self.data[key] = new_node
        if self.size < len(self.data):
            node_to_delete = self.head.next
            self._remove(node_to_delete)
            del self.data[node_to_delete.key]

    def get(self, key):
        if key in self.data:
            node = self.data[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None

    def display(self):
        res = ""
        for i in self.data:
            res += "<{0}>".format(i)
        return res

    def display_extended(self):
        c_node = self.head
        res = ""
        for i in range(0, self.size):
            c_node = c_node.next
            res += c_node.__repr__()
        return res


cache = LRU(3)
cache.set("a", 1)
cache.set("b", 2)
cache.set("c", 3)
cache.set("d", 4)
cache.set("e", 5)
print(cache.display())
print(cache.display_extended())
print(cache.get("a"))  # None
print(cache.get("e"))  # 5
print(cache.get("d"))  # 4
print(cache.get("c"))  # 3
print(cache.get("b"))  # None
