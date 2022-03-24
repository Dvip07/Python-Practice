# Picking Things at Random
# 3.11.1
import random
values = [1, 2, 3, 4, 5, 6]
random.choice(values)
random.choice(values)
random.choice(values)
random.choice(values)

# 3.11.2
random.sample(values, 2)
random.sample(values, 2)
random.sample(values, 3)
random.sample(values, 3)

# 3.11.3
random.shuffle(values)
values
random.shuffle(values)
values

random.randint(0, 10)
random.randint(0, 10)
random.randint(0, 10)
random.randint(0, 10)
random.randint(0, 10)
random.randint(0, 10)

# 3.11.4
random.random()
random.random()
random.random()

# 3.11.5
random.getrandbits(200)

# Discussion
random.seed()
random.seed(12345)
random.seed(b'bytedata')

