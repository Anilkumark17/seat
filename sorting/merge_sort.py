def merge_sort(arr):
    
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    right=merge_sort(arr[mid:])
    left=merge_sort(arr[:mid])
    
    return merge(left,right)
    
def merge(left,right):
    sorted_arr=[]
    
    while left and right:
        if(left[0]<right[0]):
         
            sorted_arr.append(left.pop(0))
           
        else:
         
            sorted_arr.append(right.pop(0))
            

           

    return sorted_arr+left+right        
    
    
print(merge_sort([8, 3, 5, 4, 7, 6, 1, 2]))    