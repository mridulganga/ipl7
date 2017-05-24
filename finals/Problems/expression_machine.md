# Expression Machine
There are **n** expressions and they are all binary. The first expression can have numbers only. All the expressions are assigned to a variable (ex a = 2 + 3). The expressions following the first expression may have number or variable (ex b = a + 3). There is one space between all the entities in the expression. No variable can be reinitialised. Allowed operations are +,-,*,/,%. You are supposed to display the value of all the variables in the order they were initialised.

# Constraints
0 < n < 27
variable are alphabets of length 1  
There is space between every entity  
First expression contains numbers  

# Input format
The first line contains **n** the number of expressions. The following n lines contain an expression in each line. The expressions will always be in format **a = 2 + 3**
The expressions after the first expressions may have numbers or variables **b = a + 2** or **c = a + b**.

# Output format
Total n lines with the value of variable in the order they were initialised in each line.

# Sample Input
4  
a = 3 + 4  
b = a - 2  
c = 2 * b  
d = a * c  

# Sample Output
7  
5  
10  
70  
