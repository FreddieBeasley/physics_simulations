def simToMat(listA, listB) -> list:
     matA  = [
          [listA[0], listA[1]],
          [listB[0], listB[1]]
     ]

     matB = [
          listA[2],
          listB[2]
     ]

     return matA, matB


def determinant_2x2(mat) -> list:

     #ad - bc
     determinant = (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])

     return determinant


def ajoint_2x2(mat) -> list:

     ajointMatrix = [
          [mat[1][1], -(mat[0][1])],
          [-(mat[1][0]), mat[0][0]]
     ]

     return ajointMatrix


def inverseMatrix_2x2(mat) -> list:

     ajoint = ajoint_2x2(mat)
     determinant = determinant_2x2(mat)

     if determinant == 0:
          raise ValueError("Matrix in singular")

     for i in range(len(mat)):
          for j in range(len(mat)):
               ajoint[i][j] /= determinant
     
     return ajoint


def multilpyMatrixes_2x2_with_2x1(matA, matB) -> list:

     # matA * matB = matC
     # a  b    e   _ ae + bf   
     # c  d    f   ‾ ce + df

     product = [
          (matA[0][0] * matB[0]) + (matA[0][1] * matB[1]),
          (matA[1][0] * matB[0]) + (matA[1][1] * matB[1])
     ]

     return product

def solve_simultaneos_equation(equationA, equationB) -> list:

     #Validation
     if not isinstance(equationA, list) or not isinstance(equationB, list) or len(equationA) != len(equationB) != 3:
          raise TypeError("equations must be a list of 3 items")

     
     #Assume each list contains the correct data type, in C++ this will happen naturally

     matA, matB = simToMat(equationA, equationB)

     matA_Inv = inverseMatrix_2x2(matA)

     product = multilpyMatrixes_2x2_with_2x1(matA_Inv, matB)

     return product[0], product[1]