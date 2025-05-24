class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def showing_count(cls):
        print(f"Total objects created: {cls.count}")

if __name__ == "__main__":
    object1 = Counter()
    object2 = Counter()
    object3 = Counter()
    Counter.showing_count()