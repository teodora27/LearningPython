lst = list()
while True:
  value = input()
  if value == "":
    break
  lst.append(value)
freq ={}
for item in lst:
    if (item in freq):
        freq[item]+=1
    else:
        freq[item]=1
for key, value in freq.items():
    if value%2==1:
        print(key)