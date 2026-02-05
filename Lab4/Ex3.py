# Name: Phuong Duong
# Date: Jan 30, 2026

#Append and Insert Mathods
responses = [5, 7, 3, 8]

responses.append(0)         # add 0 to end
responses.insert(2, 6)      # put 6 in index 2 (3rd position)

print(responses)            # should be [5, 7, 6, 3, 8, 0]


#List slicing:
responses = [5, 7, 3, 8]

responses = responses + [0]                 # add to end
responses = responses[:2] + [6] + responses[2:]  # insert 6 between 7 and 3

print(responses)
# should be [5, 7, 6, 3, 8, 0]