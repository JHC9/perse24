valid = 0
for i in range(12):
  x = int(input())
  if int(str(x[0])) - int(str(x[1])) == 1 or int(str(x[0])) - int(str(x[1])) == -1:
    valid += 1

print(valid)
