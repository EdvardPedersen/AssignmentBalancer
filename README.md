# AssignmentBalancer

This tool allows you to quickly check how many students have submitted assignments between groups in Canvas.

To use the tool, download all assignments and put them into a folder called "submissions".
All assignments that include the username of the student are counted, and the ones that do not provide a warning.

## How to use

1. Download the list of students (Karakterer -> Eksport), make sure all students are selected (not a sub-group)
2. Move the list of students into the same folder as balance.py, and give it a reasonable name (e.g. students.csv)
3. Create a folder with the name "submissions"
4. Download all submitted assignments (Oppgaver -> Oppgavesett 1 -> Last ned alle)
5. Unzip the submitted assignments into the "submissions" folder
6. Run the program as follows: `python balance.py -l students.csv` replace students.csv with the name of the list of the students if you chose a different name

The output is as follows:
First is a list of invalid assignments, these do not contain any user name in the filename.
Second is a listing of all the TAs, with the number of assignments assigned to each.
