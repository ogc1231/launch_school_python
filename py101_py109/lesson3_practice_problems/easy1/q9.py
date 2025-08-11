advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

new_advice = advice[0:advice.index('house')]
new_advice2 = advice.split("house")[0]

print(new_advice)
print(new_advice2)