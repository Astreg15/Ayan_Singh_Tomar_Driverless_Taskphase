hash_table = [[] for _ in range(10)]
n=int(input("enter the number of strings: "))
print("\n enter your nos:")
for i in range(n):
      num=int(input(f"enter number {i+1}: "))
      index=num%10
      hash_table[index].append(num)
print("\n hash table:")
for i,bucket in enumerate(hash_table):
    print(f"Index {i}(num%10=={i}): {bucket}")