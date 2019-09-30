class OrderLog:
    def __init__(self, psize):
        self.size = psize
        self.log = []

    def record(self, order_id):
        if (len(self.log) == self.size):
            self.log.pop(0)
        self.log.append(order_id)

    def get_last(self, i):
        print(self.log)
        return self.log[-(i+1)]


x = OrderLog(3)
x.record(1)
x.record(2)
x.record(3)
x.record(4)
print(x.get_last(1))
