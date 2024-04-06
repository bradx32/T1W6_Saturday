# Factorial

# 6! = 1 * 2 * 3 * 4 * 5 * 6
# 2 
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
# 120 * 6 = 720

num = 6

fact_result = 1

for i in range(1, num + 1): # 1, 2, 3, 4, 5, 6
    fact_result *= i # 1 * 1 = 1, 1 * 2 = 2, 2 * 3 = 6, 6 * 4 = 24, ....

print(fact_result)