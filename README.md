# StudentGroupGenerator

`StudentGroupGenerator` will shuffle a given student list and create groups of varying sizes (individuals, pairs, or triplets). 
It can be run either from the command line or from the interpreter/Jupyter Notebook.

## Usage

### From the Command Line

```
$ python student_group_creator /path/to/my_name_list.txt

GROUP PAIRS:

    ['Full Name One', 'Full Name Two']
    ['Full Name Three', 'Full Name Four']
    ['Full Name Five', 'Full Name Six']
    ['Full Name Seven', 'Full Name Eight']

```

### From the Interpreter

In addition to the path to your list of student names, you must also supply a list specifying how many groups of a certain number you want.

- If you have 10 students and want 5 pairs: `[0, 5]`
- If you have 10 students and want 3 trios: `[1, 0, 3]`

etc.


```
>>> from student_group_creator import create_groups
>>> groups = create_groups("/path/to/my_name_list", [0, 4])
```

**Note:** the total students from each group type needs to equal the total number of students. So if you supply `[1, 0, 3]` you need to have 10 students.

### Other Functionality

- `show_students(groups)` - print the student names in an interpreter
- `show_students_in_browser(groups)` - print groupings of student names in the browser as an HTML table

## Formatting the Input

You need to supply a list of student names whether you run from the command line or inside of an interpreter. The list should look like so:

```
Full Name One
Full Name Two
Full Name Three
...
Full Name N
```

## Using Photos with Names

If you have student pictures, put them in the `photodir` directory (or modify the code to a directoy of your own choosing). You can then use the `show_students` function to pop up their pictures along with the group names (this function is handy if your students don't know each others' names well yet, where a visual reference might help them find each other more quickly). 


