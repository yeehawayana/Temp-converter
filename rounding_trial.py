#display output using int / float


to_round = [1/1, 1,2, 1/3]
print("**** Numbers to round ****")
print(to_round)

print()
print("**** Rounded Numbers ****")

for item in to_round:
  if item%1==0:
    print("{..01}".format(item))
  else:
    print("{:.1f".format(item))