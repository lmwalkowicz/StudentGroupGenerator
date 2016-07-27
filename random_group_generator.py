# the following is from https://gist.github.com/emwdx/3922013
#!/usr/bin/env python
import random

robotics_students = ['shane', 'kevin', 'spencer', 'sam', 'thomas', 'alex', 'minxiu', 'jun hao', 'paul']
geo_students = ['maddie', 'elena', 'roosa', 'suki', 'patricia', 'ali', 'alex', 'jun hao', 'shane', 'tian', 'sho M', 'sho C', 'nick', 'annie', 'minji', 'kimmy', 'shannon', 'kevin', 'sam']
aa_students = ['flo','eigo','jake', 'sam','jane', 'jessie', 'emilly', 'maiti', 'brandon', 'min-xiu', 'paul', 'thomas']
CTF = ['nikita','cherry','jenny','miyu','flaminia','srishti','amy','celine','amelia','esther','maddie']
CTM = ['thomas','rahul','jakob','isaac','tama','ian','aman']




class_name = aa_students

random.shuffle(class_name)
parameters = [0,8,1]

#This will generate randomized groups from a list of names. The input list called parameters consists of
#numbers to indicate how many groups of each size should be created. [0,8,1] will result in no students in
#individual groups, 8 pairs of students, and 1 group of 3.

def get_groups(names,parameters):
    total = 0
    i = 0
    output = []
    for item in parameters:
        i = i + 1
        total = total + i*parameters[i-1]
        if (total!=len(names)):
            print 'Parameters not set correctly'
        else:
            random.shuffle(names)
            i = 0
            curr_index = 0
            num = 1
            for item in parameters:
                    
                    
                    if (item!=0):
                        
                        for i in range(0,item):
                            temp_group = names[0:num]
                            output.append(temp_group)
                            names.__delslice__(0,num)
                            num +=1

        for group in output:
            print group





get_groups(geo_students,[0,5,3])



#for students in class_name:
#	print students