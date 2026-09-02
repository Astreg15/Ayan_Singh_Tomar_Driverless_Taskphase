class a3:
    def selection_sort(self, arr):
        n=len(arr)
        for i in range(n):
            min_idx=i
            for j in range(i+1,n): 
                if arr[j]<arr[min_idx]:
                    min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
        return arr

    def binary_search(self, arr, target):
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target: 
                return mid
            elif arr[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
num_strings=int(input("enter the number of strings: "))
string_list=[]
for i in range(num_strings):
    user_string=input(f"enter string:{i+1}")
    string_list.append(user_string)
searcher=a3()
sorted_list=searcher.selection_sort(string_list)
print("Sorted strings:", sorted_list)
target_string=input("enter the string to search: ")
search_result=searcher.binary_search(sorted_list, target_string)
if search_result!=-1:
    print(f"String '{target_string}' found at index {search_result}.")
else:
    print(f"String '{target_string}' not found in the list.")