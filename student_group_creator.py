#!/usr/bin/env python
import random
from IPython.display import Image, HTML, display


def showStudents(groups):
    # would like to make student pictures display in their groups
    # NB: requires that image file names are the same as student names in the input list

    photoDir = './photodir/'
    #take each group list and parse student names into image file names (strip space, add .jpg)
    for i in range(0,len(groups)):
        studentGroup = groups[i]
        listOfImageNames = [ ]
        captionNames = ' '
        for j in range(0,len(studentGroup)):
            individualName = studentGroup[j]
            individualName = individualName.replace(" ", "")
            individualName+='.jpg'
            fileName = photoDir+individualName
            listOfImageNames.append(fileName)
            # we also want the student name captions to be generated automatically from file names
            if j != len(studentGroup)-1:
                captionNames += studentGroup[j] + ', '
            else:
                captionNames += studentGroup[j]
    
        #display each group member's image with their name
        preFormatHTMLTags = ["<figure>"]
        postFormatHTMLTags = ["</figure>"]
        imageSources = [ "<img style='width: 200px; border: 1px solid black;' src='%s' />"  % str(s) for s in listOfImageNames ]
        preCaptionsTag = ["<figcaption><h1>"]
        captionMid = [ captionNames ]
        postCaptionsTag = ["</figcaption>"]
        fullImageDisplayTags = preFormatHTMLTags + imageSources + preCaptionsTag + captionMid + postCaptionsTag + postFormatHTMLTags
        
        imagesList=' '.join( fullImageDisplayTags )
        display(HTML(imagesList))

def nameCounter(pars):
    #Parameters consists of numbers to indicate how many groups of each size should be created.
    # e.g. [0,8,1] will result in no students in individual groups, 8 pairs of students, and 1 group of 3.
    totalNames = 0
    i = 0
    for item in pars:
        i = i + 1
        totalNames = totalNames + i*pars[i-1]
    return totalNames

def createGroups(studentFile, Parameters):

    listOfGroups = []

    #read in student names from a file
    studentNames = [line.rstrip() for line in open(studentFile)]

    #return error if number of students in groups != total number students
    total = nameCounter(Parameters)

    if total != len(studentNames):
        numStudents = len(studentNames)
        print 'There are ' + str(numStudents) + ' students in total. The total number of students included in groups not equal to total number of students! Check input pars.'
    else:
        #shuffle student names and assemble into groups
        random.shuffle(studentNames)
        i = 0
        curr_index = 0
        num = 1
        for item in Parameters:
            if (item!=0):
                for i in range(0,item):
                    temp_group = studentNames[0:num]
                    listOfGroups.append(temp_group)
                    studentNames.__delslice__(0,num)
            num +=1

    return listOfGroups