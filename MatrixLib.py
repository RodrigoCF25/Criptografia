
def IsSquare(matrix):
    rows = len(matrix)

    row_not_squared = list(filter(lambda row: row if len(row) != rows else None,matrix))

    if len(row_not_squared) > 0:
        return False
    
    return True


def GetMatrixShape(matrix):

    rows,columns = len(matrix),len(matrix[0])
    return rows,columns


def Multiply(matrixA,matrixB):
    matrixA_shape = GetMatrixShape(matrixA)
    matrixB_shape = GetMatrixShape(matrixB)

    if matrixA_shape[1] != matrixB_shape[0]:
        raise ValueError("Matrix shapes are not compatible for multiplication")
    
    result = [[0 for _ in range(matrixB_shape[1])] for _ in range(matrixA_shape[0])]

    for i in range(matrixA_shape[0]):
        for j in range(matrixB_shape[1]):
            for k in range(matrixB_shape[0]):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result




def Floor(number):
    if int(number) == number:
        return int(number)

    if number >= 0:
        return int(number)
    else:
        return int(number) - 1

def Ceil(number):
    if int(number) == number:
        return int(number)
    
    if number >= 0:
        return int(number) + 1
    else:
        return int(number)



    





def sortMatrix(m,row_with_which_we_will_pivot):
    '''
    m: the matrix
    row_pivot: the row to pivot
    '''

    matrix = [row for row in m]

    column_in_which_we_will_make_zeros = row_with_which_we_will_pivot

    matrix_sorted = matrix[:row_with_which_we_will_pivot]


    matrix = matrix[row_with_which_we_will_pivot:]


    for row in matrix:
        if row[column_in_which_we_will_make_zeros] != 0:
            matrix_sorted.append(row)
            matrix.remove(row)
            break
    
    else:
        return m

    matrix_sorted += matrix
    return matrix_sorted    




def Gauss(m):
    '''
        m: the matrix, matrix must have the equation coefficients and the constant terms if planning to solve a system of equations
    '''

    matrix = [row for row in m]

    rows = len(matrix)
    columns = len(matrix[0])

    matrix = sortMatrix(matrix,0)

    for row in range(rows-1):
        column = row
        diagonal_element = matrix[row][column]

        if diagonal_element == 0:
            return None
        
        matrix[row] = list(map(lambda x: x/diagonal_element,matrix[row]))
        for next_row in range(row+1,rows):
            if matrix[next_row][column] == 0:
                continue

            multiplier = matrix[next_row][column] * -1
            matrix[next_row] = list(map(lambda x,y: x*multiplier + y,matrix[row],matrix[next_row]))


        matrix = sortMatrix(matrix,row+1)

    return matrix


"""
#IMPLEMENTATION WITH MAKING ONES IN THE DIAGONAL
Gauss use to solve systems of equations and also find the determinant of a matrix if the matrix is square
def Gauss(m):

    matrix = [row for row in m]

    rows,columns = GetMatrixShape(matrix)

    determinant = 1

    matrix = sortMatrix(matrix,0)

    if matrix != m:
        determinant *= -1

    for row in range(rows-1):
        if matrix[row][row] == 0:
                return 0
        
        diagonal_element = matrix[row][row]
        determinant *= diagonal_element
        matrix[row] = list(map(lambda x: x/diagonal_element,matrix[row]))

        for next_row in range(row+1,rows):
            multiplier = matrix[next_row][row] * -1

            matrix[next_row] = list(map(lambda x,y: x*multiplier + y,matrix[row],matrix[next_row]))
        
        matrix_sorted = sortMatrix(matrix,row+1)

        if matrix != matrix_sorted:
            determinant *= -1
            matrix = matrix_sorted
    

    determinant *= matrix[-1][-1]

    if int(determinant) == determinant:
        return matrix,int(determinant)
   
    if determinant > 0:
        determinant = Ceil(determinant)
    else:
        determinant = Floor(determinant)

    return matrix,determinant
"""




def Determinant(m): #Is Gauss but not making ones in the diagonal, diagonal product is the determinant
    if not IsSquare(m):
        raise ValueError("Matrix must be square")

    matrix = [row for row in m]

    rows,columns = GetMatrixShape(matrix)

    matrix = sortMatrix(matrix,0)


    determinant = 1


    for row in range(rows-1):
        column = row
        diagonal_element = matrix[row][column]

        if diagonal_element == 0:
            return 0
        
        determinant *= diagonal_element

        for next_row in range(row+1,rows):
            multiplier = matrix[next_row][column]/diagonal_element * -1

            matrix[next_row] = list(map(lambda x,y: x*multiplier + y,matrix[row],matrix[next_row]))

        matrix = sortMatrix(matrix,row+1)
        
    
    determinant *= matrix[-1][-1]

    if int(determinant) == determinant:
        return int(determinant)
    
    if determinant > 0:
        if determinant - int(determinant) >= 0.5:
            determinant = Ceil(determinant)
        else:
            determinant = Floor(determinant)

    else:
        if abs(determinant) - abs(int(determinant)) >= 0.5:
            determinant = Floor(determinant)
        else:
            determinant = Ceil(determinant)

    return determinant



def Transpose(m):
    rows,columns = GetMatrixShape(m)

    tranpose = []

    for column in range(columns):
        column_tranpose = []
        for row in range(rows):
            column_tranpose.append(m[row][column])
        tranpose.append(column_tranpose)

    return tranpose


def CofactorMatrix(m):

    if not IsSquare(m):
        raise ValueError("Matrix must be square")

    rows,columns = GetMatrixShape(m)

    cofactor_matrix = []

    for row in range(rows):
        cofactor_row = []
        matrix_without_the_elements_whose_cofactors_we_will_calculate = [m[i] for i in range(rows) if i != row]

        for column in range(columns):
            sub_matrix_for_cofactor = [sub_matrix_row[:column] + sub_matrix_row[column+1:] for sub_matrix_row in matrix_without_the_elements_whose_cofactors_we_will_calculate]
            determinant = Determinant(sub_matrix_for_cofactor)
            cofactor = determinant * (-1)**(row+column)
            cofactor_row.append(cofactor)
        cofactor_matrix.append(cofactor_row)


    return cofactor_matrix




def Adjoint(m):
    if not IsSquare(m):
        raise ValueError("Matrix must be square")
    return Transpose(CofactorMatrix(m))



if __name__ == "__main__":
    
    matrix = [
        [17,17,5],
        [21,18,21],
        [2,2,19]
    ]

    print(Gauss(matrix))
    print(Determinant(matrix))

    
    matrix = [
        [2,3,1,5],
        [6,7,2,4],
        [1,8,9,3],
        [4,1,2,7]
    ]

    print(Determinant(matrix))


    print(CofactorMatrix(matrix))


    print(Adjoint(matrix))

