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
# I used no outside sources and did not discuss with anyone else.
#---------------------------------------------------------------------

To Run: In terminal, use the command "python3 matrixprod.py" and then the names of the files
being passed into the program. The files must be in the same folder as matrixprod.py.

Implementation: To build the matrices, I simply read each line of the passed file, converted
the values from strings to integers, and then added the line to a list. When multiplying
the matrices, I thought of the equation as m1 * m2 = p. For m1, I used the first matrix
provided as a base value, and then substituted in the product of the overall multiplication
in order to allow for 3 or matrices to be multiplied. For m2, I used the second matrix
provided as a base value, and then switched it with the next provided matrix, if applicable.
I then returned the final product matrix, and printed it to the console.

Additional Notes: This was written in Python 3.11.9, and while in my tests it worked in
Python 3.10.11, it is possible that there will be errors in 3.10.11 due to version
compatibility issues.