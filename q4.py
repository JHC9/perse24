first = input()
second = input()
third = input()

if second != first and third != first:
  print("BOTH MISMATCH")
elif second != first and third == first:
  print("ENTRY 2 MISMATCH")
elif second == first and third != first:
  print("ENTRY 3 MISMATCH")
else:
  print("OK")
