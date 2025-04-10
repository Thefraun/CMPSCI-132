#---------------------------------------------------------------------
# Name: Logan Fraunfelter
# Email: lsf5185@psu.edu
# Class: CMPSC 132
# Program 1.2 / HW 2
# Due Date: February 18, 2025
#
# Description: This program accepts file names and mathematical
# operators as command line arguments, reads the files into matrices,
# and then does the requested operation(s) with said matrices. The
# program can print the result to the console or to another file,
# depending on the command line arguments passed.
#
# Acknowledgement:
# I used no outside sources, and have nothing to acknowledge.
#---------------------------------------------------------------------

import sys

class Matrix:
    
    def __init__(self, file = None, matrix = None):
        
        # Ensure that the class is properly initialised
        assert file != None or matrix != None, "Matrix requires either a file containing a matrix or a matrix in list form to initialise."
        
        # If there is a file to initialise the matrix, use it
        if file != None:
            # Create a list to build the matrix
            self.__matrix = []
            
            # Open the file, keyword 'with' being used to automatically handle closing the file
            with open(file, 'r') as fp:
                
                # Loop through each line in the file
                for line in fp: 
                    
                    # Create a list containing each number (as a str) in the line        
                    nums = line.split()
                    
                    # Convert each number from a str to an int
                    nums = list(map(int, nums))
                    
                    # Add the row, as a list of ints, to the matrix
                    self.__matrix.append(nums)
        
        # If there is no file to initialise the matrix, initialise it using the list
        else:
            self.__matrix = matrix
            
        self.iterStart = 0
            
    def __mul__(self, m2):
        
        # Ensure that the dimensions of the matrices are compatible for the operation
        assert self.__matrix[0][1] == m2.__matrix[0][0], "Matrix calculation cannot be performed because of matrix size issues."
        
        # Store matrices in temp lists so as to not mess up originals
        multiplicand = self.__matrix.copy()
        multiplier = m2.__matrix.copy()
        
        # Create variables to determine dimensions of product matrix (pop to remove dimension row to prevent issues with looping)
        prodRows = multiplicand.pop(0)[0]
        prodCols = multiplier[0][1]
        
        # Create a variable to ensure proper traversal of both matrices without going out of bounds (pop for same reason as above)
        sharedIndex = multiplier.pop(0)[0]
        
        # Create a placeholder product matrix with all zeroes using list comprehension
        product = [[0 for _ in range(prodCols)] for _ in range(prodRows)]
        
        # Go through each row and column and perform matrix multiplication
        for i in range(prodRows):
            for j in range(prodCols):
                for k in range(sharedIndex):
                    product[i][j] += multiplicand[i][k] * multiplier[k][j]
        
        # Insert the dimensional row into the product matrix
        product.insert(0, [prodRows, prodCols])
        
        # Return the final product
        return Matrix(matrix=product)
    
    def __imul__(self, m2):
        
        # Ensure that the dimensions of the matrices are compatible for the operation
        assert self.__matrix[0][1] == m2.__matrix[0][0], "Matrix calculation cannot be performed because of matrix size issues."
        
        # Store matrices in temp lists so as to not mess up originals
        multiplicand = self.__matrix.copy()
        multiplier = m2.__matrix.copy()
        
        # Create variables to determine dimensions of product matrix (pop to remove dimension row to prevent issues with looping)
        prodRows = multiplicand.pop(0)[0]
        prodCols = multiplier[0][1]
        
        # Create a variable to ensure proper traversal of both matrices without going out of bounds (pop for same reason as above)
        sharedIndex = multiplier.pop(0)[0]
        
        # Create a placeholder product matrix with all zeroes using list comprehension
        product = [[0 for _ in range(prodCols)] for _ in range(prodRows)]
        
        # Go through each row and column and perform matrix multiplication
        for i in range(prodRows):
            for j in range(prodCols):
                for k in range(sharedIndex):
                    product[i][j] += multiplicand[i][k] * multiplier[k][j]
        
        # Insert the dimensional row into the product matrix
        product.insert(0, [prodRows, prodCols])
        
        # Update the value of matrix to the product
        self.__matrix = product
        
        # Return self to properly update variable
        return self
            
    def __add__(self, m2):
        
        # Ensure that the dimensions of the matrices are compatible for the operation
        assert self.__matrix[0] == m2.__matrix[0], "Matrix calculation cannot be performed because of matrix size issues."
        
        addend1 = self.__matrix.copy()
        addend2 = m2.__matrix.copy()
        
        # Create variables to determine the dimersions of the sum matrix (pop to prevent issues with looping)
        sumRow = addend1.pop(0)[0]
        sumCol = addend2.pop(0)[1]
        
        # Create a placeholder sum matrix with all zeroes using list comprehension
        sum = [[0 for _ in range(sumCol)] for _ in range(sumRow)]
        
        # Go through each row and column and perform matrix addition
        for i in range(sumRow):
            for j in range(sumCol):
                sum[i][j] = addend1[i][j] + addend2[i][j]
        
        # Insert the dimenstional row into the sum matrix
        sum.insert(0, [sumRow, sumCol])
        
        # Return the sum matrix
        return Matrix(matrix=sum)
    
    def __iadd__(self, m2):
        
        # Ensure that the dimensions of the matrices are compatible for the operation
        assert self.__matrix[0] == m2.__matrix[0], "Matrix calculation cannot be performed because of matrix size issues."
        
        addend1 = self.__matrix.copy()
        addend2 = m2.__matrix.copy()
        
        # Create variables to determine the dimersions of the sum matrix (pop to prevent issues with looping)
        sumRow = addend1.pop(0)[0]
        sumCol = addend2.pop(0)[1]
        
        # Create a placeholder sum matrix with all zeroes using list comprehension
        sum = [[0 for _ in range(sumCol)] for _ in range(sumRow)]
        
        # Go through each row and column and perform matrix addition
        for i in range(sumRow):
            for j in range(sumCol):
                sum[i][j] = addend1[i][j] + addend2[i][j]
        
        # Insert the dimenstional row into the sum matrix
        sum.insert(0, [sumRow, sumCol])
        
        # Update the value of matrix to the sum
        self.__matrix = sum
    
        # Return self to properly update variables
        return self
    
    def __sub__(self, m2):
        
        # Ensure that the dimensions of the matrices are compatible for the operation
        assert self.__matrix[0] == m2.__matrix[0], "Matrix calculation cannot be performed because of matrix size issues."
        
        addend1 = self.__matrix.copy()
        addend2 = m2.__matrix.copy()
        
        # Create variables to determine the dimersions of the difference matrix (pop to prevent issues with looping)
        difRow = addend1.pop(0)[0]
        difCol = addend2.pop(0)[1]
        
        # Create a placeholder sum matrix with all zeroes using list comprehension
        difference = [[0 for _ in range(difCol)] for _ in range(difRow)]
        
        # Go through each row and column and perform matrix subtraction
        for i in range(difRow):
            for j in range(difCol):
                difference[i][j] = addend1[i][j] - addend2[i][j]
        
        # Insert the dimenstional row into the difference matrix
        difference.insert(0, [difRow, difCol])
        
        # Return the difference matrix
        return Matrix(matrix=difference)
    
    def __isub__(self, m2):
        
        # Ensure that the dimensions of the matrices are compatible for the operation
        assert self.__matrix[0] == m2.__matrix[0], "Matrix calculation cannot be performed because of matrix size issues."
        
        addend1 = self.__matrix.copy()
        addend2 = m2.__matrix.copy()
        
        # Create variables to determine the dimersions of the difference matrix (pop to prevent issues with looping)
        difRow = addend1.pop(0)[0]
        difCol = addend2.pop(0)[1]
        
        # Create a placeholder sum matrix with all zeroes using list comprehension
        difference = [[0 for _ in range(difCol)] for _ in range(difRow)]
        
        # Go through each row and column and perform matrix subtraction
        for i in range(difRow):
            for j in range(difCol):
                difference[i][j] = addend1[i][j] - addend2[i][j]
        
        # Insert the dimenstional row into the difference matrix
        difference.insert(0, [difRow, difCol])
        
        # Return the difference matrix
        self.__matrix = difference
        
        # Return self to properly update variables
        return self
    
    def __eq__(self, m2):
        
        # Returns True if the two matrices are equal, False if not equal
        return self.__matrix == m2.__matrix
    
    def __ne__(self, m2):
        
        # Returns True if the two matrices are not equal, False if equal
        return self.__matrix != m2.__matrix
    
    def __str__(self):
        
        # Construct a str version of the matrix, with the proper formatting
        matStr = ''
        for row in self.__matrix:
            for num in row:
                matStr+=str(num) + ' '
            matStr+="\n"
        
        # Return the str version, with leading and trailing whitespace stripped
        return matStr.strip()
        
def main():
    
    # Get the CLI arguments
    args = sys.argv[1:]
    
    # Create a placeholder variable to store the name of the destination file for the final answer, if applicable
    destFile = None
    
    # If the equation contains an equal sign, set the destination file to the first file
    # And remove both the file name and the = sign from the list of arguments to prevent errors
    if '=' in args:
        destFile = args.pop(0)
        args.remove('=')
    
    # Create two separate lists, one to store the matrices and one to store the operations to perform
    matrices = []
    operators = []
    
    # Loop through each argument
    for arg in args:
        
        # If the argument is a file, create a matrix from that file
        if arg.find('.txt') != -1:
            matrices.append(Matrix(file=arg))
        
        # Else, it's an operator
        else:
            operators.append(arg)
    
    # Create a variable to store the left side of the equation (L in L + R = S) 
    leftSide = matrices[0]
    
    # Create a variable to store the index of the matrix used as the right side of the equation (R in L + R = S)
    rightSideInd = 1
    
    # Loop through each operator
    for op in operators:
        
        # Determine which operation to perform, and perform said operation
        # For imul, iadd, and isub, set the destination file equal to the first argument, as it must be based on the guidelines
        # (Sorry, I know it's not pretty, but it gets the job done)
        if op == 'mul':
            leftSide = leftSide * matrices[rightSideInd]
        elif op == 'imul':
            destFile = args[0]
            leftSide *= matrices[rightSideInd]
        elif op == 'add':
            leftSide = leftSide + matrices[rightSideInd]
        elif op == 'iadd':
            destFile = args[0]
            leftSide += matrices[rightSideInd]
        elif op == 'sub':
            leftSide = leftSide - matrices[rightSideInd]
        elif op == 'isub':
            destFile = args[0]
            leftSide -= matrices[rightSideInd]
        elif op == 'eq':
            print(leftSide == matrices[rightSideInd])
        elif op == 'neq':
            print(leftSide != matrices[rightSideInd])
        else:
            print("Operator has not been recognised. Cannot compute further.")
            break
        
        # Increment the right side index to allow for another calculation to be performed, if applicable
        rightSideInd+=1
    
    # If there is no destination file, print the end result to the console
    if destFile == None:
        print(leftSide)
    
    # Else, write the result to the destination file
    else:
        with open(destFile, 'w') as fp:
            fp.write(str(leftSide))
                           
if __name__ == '__main__':
    main()