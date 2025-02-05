#---------------------------------------------------------------------
# Name: Logan Fraunfelter
# Email: lsf5185@psu.edu
# Class: CMPSC 132
# Program 1.1 / HW 1
# Due Date: February 06, 2025
#
# Description: This program accepts file names as command line arguments,
# reads the files, and transforms their contents into matrices. Following this,
# the program multiplies the matrices, writing the output to the console.
#
# Acknowledgement:
# I used no outside sources, and have nothing to acknowledge.
#---------------------------------------------------------------------

import sys

class MatrixMultiplier:
    
    def __init__(self, files: list):

        # Create a list to hold each matrix
        self.matrices = []
        
        # Add each matrix into matrices
        for matrix in self.__createMatrices(files):
            self.matrices.append(matrix)
    
    def __createMatrices(self, files: list):
        
        # Loop through each file
        for file in files:
        
            # Create a list to build the matrix
            matrix = []
            
            # Open the file, keyword 'with' being used to automatically handle closing the file
            with open(file, 'r') as fp:
                
                # Loop through each line in the file
                for line in fp: 
                    
                    # Create a list containing each number (as a str) in the line        
                    nums = line.split()
                    
                    # Convert each number from a str to an int
                    nums = list(map(int, nums))
                    
                    # Add the row, as a list of ints, to the matrix
                    matrix.append(nums)
            
            # Pass created matrix back
            yield matrix
            
    def multiplyMatrices(self):
        
        # If there is only one matrix, return it unaltered
        if len(self.matrices) == 1:
            return self.matrices[0]
        
        # If there is more than one matrix, multiply them
        else:
            
            # Create a variable to store the multiplicand (m1 in m1 * m2 = p)
            multiplicand = self.matrices[0]
            
            # Create a variable to determine index of multiplier
            matrixNum = 1
            
            # While there are still matrices left to be multiplier, continue multiplying
            while matrixNum < len(self.matrices):
                
                # Create a variable to store the multiplier (m2 in m1 * m2 = p)
                multiplier = self.matrices[matrixNum]
                
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
                
                # Set the multiplicand equal to the product to be used for next multiplication, if applicable
                multiplicand = product
                
                # Increase counter to show that it is time for the next matrix to be the multiplier, if applicable
                matrixNum+=1
            
            # Return the final product
            return product
        
def main():
    
    # Get the files passed as CLI arguments
    files = sys.argv[1:]
    
    # Create an instance of the MatrixMultiplier class to perform operations, passes files in order to create initial list of matrices
    matrixMult = MatrixMultiplier(files)
    
    # Store the final product of the matrix multiplication
    product = matrixMult.multiplyMatrices()
    
    # Print the matrix in proper form
    for row in product:
        for num in row:
            print(num, end=' ')
        print()
            
if __name__ == '__main__':
    main()