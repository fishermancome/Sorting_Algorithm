def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

if __name__=="__main__":
    print(bubble_sort([23,96,12,11,54,87,43]))
