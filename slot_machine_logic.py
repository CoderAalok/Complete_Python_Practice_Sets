class RandomGenerator:
    # Seed: Initial or stating value
    def __init__(self, seed=1):
        self.X = seed    # X -> State 
    
    def next(self):
        a = 1112233 # multiplier
        c = 1123 # Increment
        m = 2**31 # module
        
        self.X = (a * self.X + c) % m
        return self.X

class Biased(RandomGenerator):
    def random_biased(self):
        probabilities = (
            [1]*1 +
            [2]*2 +
            [3]*5 +
            [4]*2 +
            [5]*1 + 
            [6]*5
        )
        
        index = self.next() % len(probabilities)
        return probabilities[index]


rng = Biased(seed=123)
for _ in range(20):
    print(rng.random_biased())
    
from numpy import *
print(random.randint(low=1, high=6, size=20))