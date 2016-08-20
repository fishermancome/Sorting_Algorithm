#纪录某次遍历时最后发生交换的位置，在该位置之后的数据都是有序的
def bubble_sort3(array):
    n = len(array)
    k = n
    for i in range(n):
        flag = 1
        for j in range(k-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                k = j+1
                flag = 0
        if flag:
            break
    return array

if __name__ == "__main__":
    print(bubble_sort3([23,96,12,11,54,87,43]))
