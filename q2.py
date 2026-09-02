class String_sorter:
    def selection_sort(self, arr):
        n=len(arr)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
num_strings= int(input("enter the number of strings: "))
string_list=[]
for i in range(num_strings):
    user_string=input(f"enter string:{i+1}")
    string_list.append(user_string)
my_sorter=String_sorter()
sorted_result=my_sorter.selection_sort(string_list)
print("Sorted strings:", sorted_result)