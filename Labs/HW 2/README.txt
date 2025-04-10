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

To Run: In terminal, use the command "python3 matrixoper.py" and then the names of the files
and operators being passed into the program. The files must be in the same folder as matrixoper.py.

Implementation: I created a matrix class that took a file or a list as an argument to build the matrix.
I stored the created matrix as a class attribute in the form of a list, and used this list to perform
the matrix operations. To know which matrix operations to perform and the matrices to use, I read the
CLI arguments and separated them into matrices and operators. I then looped through the operators,
using the result from each operation as the "left side" of each subsequent operation. I then printed the
result of the operation to the console or wrote it to the specified file, depending on the CLI arguments
passed.

Additional Notes: This was written in Python 3.11.9, and while in my tests it worked in
Python 3.10.11, it is possible that there will be errors in 3.10.11 due to version
compatibility issues.