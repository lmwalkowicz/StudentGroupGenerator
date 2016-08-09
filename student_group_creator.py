#!/usr/bin/env python
from __future__ import print_function

import random
from IPython.display import HTML, display
import webbrowser


def show_students(groups):
    """Make student pictures display in their groups in an IPython notebook
    NB: requires that image file names are the same as student names in the
    input list"""
    photo_dir = './photodir/'
    # take each group list and parse student names into image file names
    # (strip space, add .jpg)
    for i in range(0, len(groups)):
        student_group = groups[i]
        list_of_image_names = []
        caption_names = ' '
        for j in range(0, len(student_group)):
            individual_names = student_group[j]
            individual_names = individual_names.replace(" ", "")
            individual_names += '.jpg'
            file_name = photo_dir + individual_names
            list_of_image_names.append(file_name)
            # we also want the student name captions to be generated
            # automatically from file names
            if j != len(student_group) - 1:
                caption_names += student_group[j] + ', '
            else:
                caption_names += student_group[j]

        # display each group member's image with their name
        preformat_html_tags = ["<figure>"]
        postformat_html_tags = ["</figure>"]
        image_sources = [
            "<img style='width: 200px; border: 1px solid black;' src='%s' />" % str(s) for s in list_of_image_names]
        pre_captions_tag = ["<figcaption><h1>"]
        caption_mid = [caption_names]
        post_captions_tag = ["</figcaption>"]
        full_img_display_tags = preformat_html_tags + image_sources + \
            pre_captions_tag + caption_mid + \
            post_captions_tag + postformat_html_tags

        images_list = ' '.join(full_img_display_tags)
        display(HTML(images_list))


def show_students_in_browser(groups):
    """Make student pictures display in their groups in a local browser window
    NB: requires that image file names are the same as student names in the input list
    default browser is chrome, preferred browser can be set by altering the
    below."""
    browser_path = 'open -a /Applications/Google\ Chrome.app %s'
    photo_dir = './photodir/'
    outfile = open("groups.html", "w")

    # create html to go before and after code generated for student groups
    html_preamble = "<!DOCTYPE html><html><head><style>table {    font-family: arial, sans-serif;    border-collapse: collapse; } td, th {    border: 1px solid #dddddd;    text-align: center;    padding: 0px;} tr:nth-child(even) {    background-color: #dddddd;}</style></head><body><table>"
    html_closing = "</table></body></html>"

    # take each group list and parse student names into image file names
    # (strip space, add .jpg)
    outfile.write(html_preamble)
    for i in range(0, len(groups)):
        student_group = groups[i]
        caption_names = []
        list_of_image_names = []
        for j in range(0, len(student_group)):
            individual_names = student_group[j]
            individual_names = individual_names.replace(" ", "")
            individual_names += '.jpg'
            file_name = photo_dir + individual_names
            list_of_image_names.append(file_name)
            # we also want the student name captions to be generated
            # automatically from file names
            caption_names.append(student_group[j])

        # construct html to display each group member's image with their name
        preformat_html_tags = ["<tr>"]
        postformat_html_tags = ["</tr>"]
        linebreak = ["</tr><tr>"]
        image_sources = [
            "<td><img style='width: 200px; border: 1px solid black;' src='%s' /><td>" % str(s) for s in list_of_image_names]
        caption_sources = ["<td><h1> %s </h1><td>" %
                           str(s) for s in caption_names]
        full_img_display_tags = preformat_html_tags + image_sources + \
            linebreak + caption_sources + postformat_html_tags
        images_list = ' '.join(full_img_display_tags)
        outfile.write(images_list)

    # replace the below with writing the html file and displaying it in a
    # browser window
    outfile.write(html_closing)
    outfile.close()
    brwsr = webbrowser.get(browser_path)
    brwsr.open_new('groups.html')


def name_counter(pars):
    """Parameters consists of numbers to indicate how many groups of each size should be created.
    e.g. [0,8,1] will result in no students in individual groups, 8 pairs of
    students, and 1 group of 3."""
    total_names = 0
    i = 0
    for item in pars:
        i = i + 1
        total_names = total_names + i * pars[i - 1]
    return total_names


def get_name_list(student_file):
    """Read in student names from a file."""
    student_names = [line.rstrip() for line in open(student_file)]

    return student_names


def create_groups(student_file, parameters):
    """Create groups of students from a text file of student names."""
    list_of_groups = []

    # read in student names from a file
    student_names = get_name_list(student_file)

    # return error if number of students in groups != total number students
    total = name_counter(parameters)

    if total != len(student_names):
        num_students = len(student_names)
        print('There are ' + str(num_students) +
              ' students in total. The total number of students included in groups not equal to total number of students! Check input pars.')
    else:
        # shuffle student names and assemble into groups
        random.shuffle(student_names)
        i = 0
        curr_index = 0
        num = 1
        for item in parameters:
            if (item != 0):
                for i in range(0, item):
                    temp_group = student_names[0:num]
                    list_of_groups.append(temp_group)
                    student_names.__delslice__(0, num)
            num += 1

    return list_of_groups

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
        namelist = get_name_list(fname)

        if len(namelist) % 2:
            group_configs = [1, int(len(namelist) / 2)]

        else:
            group_configs = [0, int(len(namelist) / 2)]

        groups = create_groups(fname, group_configs)

        print("\nGROUP PAIRS:\n")
        for group in groups:
            print("\t" + str(group))

        print("\n")

    else:
        outstr = [
            "\n              ****************************************\n",
            "              ****************************************\n",
            "              **                                    **\n",
            "              **               ERROR                **\n",
            "              **                                    **\n",
            "              ****************************************\n",
            "              ****************************************\n",
            "\nThis will not work from the command line without a file ",
            "containing a list\nof student names.\n\nEach full name should ",
            "be separated by a new line.\n\nSupply the name of the file ",
            "containing the list like so:\n\n$ python ",
            "student_group_creator.py my_name_list.txt\n"
        ]

        print("".join(outstr))
