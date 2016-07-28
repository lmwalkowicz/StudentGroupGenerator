#!/usr/bin/env python
import random
from IPython.display import Image, HTML, display
import webbrowser


def showStudents(groups):
    # make student pictures display in their groups in an IPython notebook
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

def showStudentsInBrowser(groups):
    # make student pictures display in their groups in a local browser window
    # NB: requires that image file names are the same as student names in the input list
    # default browser is chrome, preferred browser can be set by altering the below
    browser_path = 'open -a /Applications/Google\ Chrome.app %s'
    photoDir = './photodir/'
    outFile = open("groups.html", "w")
    
    #create html to go before and after code generated for student groups
    htmlPreamble = "<!DOCTYPE html><html><head><style>table {    font-family: arial, sans-serif;    border-collapse: collapse; } td, th {    border: 1px solid #dddddd;    text-align: center;    padding: 0px;} tr:nth-child(even) {    background-color: #dddddd;}</style></head><body><table>"
    htmlClosing = "</table></body></html>"

    #take each group list and parse student names into image file names (strip space, add .jpg)
    outFile.write(htmlPreamble)
    for i in range(0,len(groups)):
        studentGroup = groups[i]
        captionNames = [ ]
        listOfImageNames = [ ]
        for j in range(0,len(studentGroup)):
            individualName = studentGroup[j]
            individualName = individualName.replace(" ", "")
            individualName+='.jpg'
            fileName = photoDir+individualName
            listOfImageNames.append(fileName)
            # we also want the student name captions to be generated automatically from file names
            captionNames.append(studentGroup[j])

        #construct html to display each group member's image with their name
        preFormatHTMLTags = ["<tr>"]
        postFormatHTMLTags = ["</tr>"]
        lineBreak = ["</tr><tr>"]
        imageSources = [ "<td><img style='width: 200px; border: 1px solid black;' src='%s' /><td>"  % str(s) for s in listOfImageNames ]
        captionSources = [ "<td><h1> %s </h1><td>"  % str(s) for s in captionNames ]
        fullImageDisplayTags = preFormatHTMLTags + imageSources + lineBreak + captionSources + postFormatHTMLTags
        imagesList=' '.join( fullImageDisplayTags )
        outFile.write(imagesList)

    #replace the below with writing the html file and displaying it in a browser window
    outFile.write(htmlClosing)
    outFile.close()
    brwsr = webbrowser.get(browser_path)
    brwsr.open_new('groups.html')

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