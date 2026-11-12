class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        if self.count > 0:
            self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count


counter = Counter()

counter.increment()
counter.increment()
counter.increment()

counter.decrement()

print(counter.get_count())

counter.reset()

counter.decrement()

print(counter.get_count())
