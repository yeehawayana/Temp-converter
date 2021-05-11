#quick component to convert degrees C to F.
#Function takes in value, does conversion and puts answer into a list

def to_c(from_f):
  celsius = (from_f *9/5) - 32
  return celsius

#Main Rountine 
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
  answer = to_c(item)
  ans_statement = "{} degrees to F is {} degrees C".format(item, answer)
  converted.append(ans_statement)

print(converted)