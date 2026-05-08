collection_numbers = [1,2,3,5,6,3,7,5,9,12,16,12,32,44,19,2,3,5,6]
print("list of 20 numbers")

print(collection_numbers)

userinput = int(input("Enter the number for Deletion")) 
if userinput in collection_numbers:

    first_index = collection_numbers.index(userinput)




else:
    print("Number not in list")