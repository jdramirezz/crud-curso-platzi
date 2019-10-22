import random



def binary_search(data, target, low, high):

    if target not in data:
        print('The number is not in the list')
        pass

    while True:
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid-1
        elif target > data[mid]:
            low = mid+1
        elif target == data[mid]:
            return True
            break



if __name__ =='__main__':
    data = [random.randint(0,100) for i in range(10)]

    data.sort()

    print(data)

    target = int(input('What number would you like to find? '))

    found = binary_search(data, target, 0, len(data)- 1)

    print(found)
