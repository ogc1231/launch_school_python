import math

nan_value = float("nan")

print(nan_value == float("nan")) # False
print(math.isnan(nan_value)) # True