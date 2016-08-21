#每次将一个待排序的数字插入到前面已排好序的序列中，直至全部插入完成
def insert_sort(array):
    n = len(array)
    for i in range(1,n):
        if array[i] < array[i-1]:
            temp = array[i]
            index = i
            for j in range(i-1,-1,-1):
                if array[j] > temp:
                    array[j+1] = array[j]
                    index = j
                else:
                    break
            array[index]=temp
    return array

if __name__=="__main__":
    print(insert_sort([23,96,12,11,54,87,43]))
