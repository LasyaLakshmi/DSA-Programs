arr = [5, 3, 8, 1, 9]
print("\nOriginal array: ", arr)

print("\nArray Traversing: ")
for i in arr:
    print(i, end = " ")

arr.insert(2, 7)
print("\nArray after insertion: ", arr)

arr.remove(5)
print("\nArray after removing: ", arr)

del arr[4]
print("\nArray after deleting: ", arr)

arr.append(10)
print("\nArray after appennding: ", arr)

if 8 in arr:
    print("\n8 in index: ", arr.index(8))
else:
    print("\n8 not found")

arr[3] = 4
print("\nArray after updating: ", arr)