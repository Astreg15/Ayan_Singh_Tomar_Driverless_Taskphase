def get_matrix_input(matrix_name):
    print(f"\n---  Inputing {matrix_name} ---")
    rows =  int(input("enter the number of rows: "))
    cols =  int(input("enter the number of columns: "))
    matrix = []
    print(f"enter the number for each row separated by spaces:")
    for i in range(rows):
        raw_row=input(f"row {i+1}: ")
        int_list= [int(num) for num in raw_row.split()]
        matrix.append(int_list)
    return matrix
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    if cols_a != rows_b:
        print(f"\n error: dimensions mismatch.")
        print(f"matrix A columns ({cols_a}) must equal matrix B rows ({rows_b}) for multiplication.")
        return None
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

print("welcome to matrix multiplier!")
A= get_matrix_input("Matrix A")
B=get_matrix_input("Matrix B")
final_matrix=multiply_matrices(A,B)
if final_matrix is not None:
    print("result matrix")
    for row in final_matrix:
        print (row)

