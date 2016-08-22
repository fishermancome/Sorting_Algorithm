#从序列中找一个基准数，比基准数大的放在右边，比基准数小的放在左边
#再对左右区间进行重复操作直至每个区间只有一个元素

def quick_sort(array):
    return sort(array,0,len(array)-1)

def sort(array,left,right):
    if left >= right:return
    key = array[left]
    lp = left
    rp = right
    while lp < rp:
        while array[rp] >= key and lp < rp:
            rp -= 1
        while array[lp] <= key and lp < rp:
            lp += 1
        array[lp],array[rp] = array[rp],array[lp]
    array[left],array[lp] = array[lp],array[left]
    sort(array,left,lp-1)
    sort(array,rp+1,right)
    return array

if __name__=="__main__":
    print(quick_sort([23,96,12,11,54,87,43]))
