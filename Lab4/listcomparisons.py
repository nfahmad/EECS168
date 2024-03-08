'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 10/05/22
Lab: lab04
Last modified: 10/06/22
Purpose: Prompt the user for two file names and print statistics comparing the two lists
'''
data1 = input("Enter name of the first data file: ")
data2 = input("Enter name of the second data file: ")

file_one = open(data1, 'r')
file_two = open(data2, 'r')

print(" ")

print("List statistics: ")

list_one = []
list_two = []

for i in file_one:
    list_one.append(int(float(i)))

for i in file_two:
    list_two.append(int(float(i)))


if (sum(list_one)) > (sum(list_two)):
    print(f"The first list has the larger sum of {sum(list_one)}")
elif (sum(list_two)) > sum(list_one):
    print(f"The second list has the larger sum of {sum(list_two)}")
else:
    print("The sum of the two lists are the same")

if(sum(list_one)/len(list_one)) > (sum(list_two)/len(list_two)):
    print(f"The first list has the larger average of {(sum (list_one)/len(list_one)):0.1f}")
elif (sum(list_one)/len(list_one)) < (sum(list_two)/len(list_two)):
    print(f"The second list has the larger average of {(sum (list_two)/len(list_two)):0.1f}")
else:
    print("The average of the two lists are the same")

count_comparison = 0
for i in range(len(list_one)):
    for j in range(len(list_two)):
        if list_one[i] == list_two[j]:
            count_comparison += 1
print(f"Count of values that appear in both lists: {count_comparison}")

if len(list_one) == len(list_two):
    list_two.reverse()
    if list_one == list_two:
        print("The lists are palindromes")
    else:
        print("The lists are not palindromes")
else:
    print("The lists are not palindromes")

file_one.close()
file_two.close()
