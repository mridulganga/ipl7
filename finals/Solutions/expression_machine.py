n = int(raw_input())
main_list = []
vars_list = []
ans_list = []

# get all the expressions
for i in xrange(n):
    main_list.append(raw_input())

# the first expression will always have numbers, so store the ans and var_val
ans_list.append(eval(main_list[0][3:]))
vars_list.append([main_list[0][0:1],str(eval(main_list[0][3:]))])

# replace vars with their vals
def cleanvars(s):
    for x in vars_list:
        s = s.replace(x[0],x[1])
    return s

# process each expression
for i in xrange(1,len(main_list)):
    ans_list.append(eval(cleanvars(main_list[i][3:])))
    vars_list.append([main_list[i][0:1],str(eval(cleanvars(main_list[i][3:])))])

# print the answers
for ans in ans_list:
    print ans


# The eval() function has been used to make the program look more redable. This can easily be replaced by a user defined function
# str_exp = s.split(" ")
# val1 = int(str_exp[0])
# val2 = int(str_exp[2])
# op = str_exp[1]
# if (op=='+'):
#   return val1+val2
#...
