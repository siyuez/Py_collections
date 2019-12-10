# create new list -> slow

# def quick_sort(numbers):
# 	print('1 time cal')
# 	mid = []
# 	left = []
# 	right = []
# 	mid.append(numbers[0])
# 	numbers.remove(numbers[0])
# 	for number in numbers:
# 		if number < mid[0]:
# 			left.append(number)
# 		elif number == mid[0]:
# 			mid.append(number)
# 		else:
# 			right.append(number)
# 	if len(left) <= 1 and len(right) >1:
# 		return left + mid + quick_sort(right)
# 	if len(left) >1 and len(right) <=1:
# 		return quick_sort(left) + mid + right
# 	if len(left) >1 and len(right) >1:
# 		return quick_sort(left) + mid + quick_sort(right)
# 	return left + mid + right


# def quick_sort(numbers):
# 	return sorted(numbers)


def quick_sort(array, low, high):
	if low < high:
		key_index = partion(array, low, high)
		quick_sort(array,low, key_index)
		quick_sort(array, key_index+1, high)


# low <-> high meet when all compare
def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1

        if low < high:
            array[low] = array[high]
            print([array, low, high])

        while low < high and array[low] < key:
            low += 1

        if low < high:
            array[high] = array[low]
            print([array, low, high])

    array[low] = key
    print([array, low, high])
    return low

if __name__ == '__main__':
    array2 = [4,3,2,1,5]

    print(array2)
    quick_sort(array2,0,len(array2)-1)
    print(array2)
