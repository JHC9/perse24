x = int(input())
days = x//5
interactions = 0
for i in range(days+1):
  interactions += (i+1) * 5
  
print(interactions-5 + x%5)
