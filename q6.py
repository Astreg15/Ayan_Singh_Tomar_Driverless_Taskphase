def get_insertion_index(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left

hash_table = [[] for _ in range(10)]
n=int(input("how many numbers you want to enter: "))
for i in range(n):
    num=int(input(f"enter number {i+1}: "))
    bucket_index = num % 10
    bucket= hash_table[bucket_index]
    insert_pos = get_insertion_index(bucket, num)
    bucket.insert(insert_pos, num)
print("\n--- Final Sorted Hash Table ---")
for i, bucket in enumerate(hash_table):
    print(f"Bucket {i}: {bucket}")