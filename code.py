class RandomNumberGenerator:
    def __init__(self, seed=12345):
        self.seed = seed
        self.a = 1103515245  
        self.c = 12345       
        self.m = 2**31       
    
    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def generate(self, min_value, max_value):
        range_size = max_value - min_value + 1
        return min_value + self.next() % range_size

rng = RandomNumberGenerator(seed=6789)  
for _ in range(5):
    print(rng.generate(1, 100))  
