# Namit's Word Machine
Namit is making a word machine which will reverse a word, shrink a word (display only even chars), tell the length of a word and count the number of words in a sentence, since this requires string manipulation so namit is not able to figure it out. Namit gets a sentence input and wants to perform above mentioned operations on the specified word. The word's number is attached to the operation using an underscore character(ex len_5). Help Namit make his word machine.

## Operations
rev = reverse  
shr = shrink  
len = length  
count = number of words  

# Input Format
The first line contains **n** (number of test cases). The second line contains the **sentence** for first test case and the third line contains the **operations** for the first test case. The next two line will have sentence and operations for the next test case and so on.

# Output Format
The _first line_ will have **space joined string** of all the operations performed on the first test case. The _second line_ will have the same for the second test case and so on.

# Sample Input
2  
namit is a good boy  
rev_3 len_4 shr_0 count  
namit loves strawberry milkshake  
shr_2 shr_3 len_2 count rev_0 rev_3  

# Sample Output
doog 3 nmt 5  
srwer mlsae 10 4 timan ekahsklim  
