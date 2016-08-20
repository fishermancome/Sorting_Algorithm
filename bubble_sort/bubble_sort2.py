#当某一趟遍历没有进行数据交换的时候说明已经排序完毕，不需要进行接下来的迭代。
def bubble_sort2(array):
    n = len(array)
    for i in range(n):
        flag=1
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            flag=0

        if flag:
            break
    return array

if __name__ == "__main__":
   print(bubble_sort2([23,96,12,11,54,87,43]))
