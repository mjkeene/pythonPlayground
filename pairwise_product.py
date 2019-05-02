"""Data Structures & Algorithms - find maximum pairwise product in an array"""

import random
import time

start = time.time()

n = 10000
print("Number of elements in array:", n)

nums = [random.randint(0, 1000000) for i in range(n)] 

# Efficient approach
nums = list(set(nums))
nums_sorted = sorted(nums)
largest = nums_sorted[-1]
sec_largest = nums_sorted[-2]

max_product = largest * sec_largest
print("The max product is:", max_product)

end = time.time()
duration = end - start
print("Efficient Duration:", duration)

# Naive approach - this has order n**2 performance
# Extremely slow for n > 10,000
start = time.time()

products = [(x*y) for x in nums for y in nums if x != y]
print("The max product is:", max(products))

end = time.time()
duration = end - start
print("Naive Duration:", duration)
