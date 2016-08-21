#在未排序的序列中找一个最小值，放在序列的最前面，
#然后从剩余序列中找出最小值放在已排好序的序列的最后面，直至所有元素排序完毕

def select_sort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if array[j] < array[min]:
                min = j
        array[min],array[i]=array[i],array[min]
    return array

if __name__=="__main__":
    print(select_sort([23,96,12,11,54,87,43]))

