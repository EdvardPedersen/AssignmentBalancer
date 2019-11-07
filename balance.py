import argparse
import csv
import os
from groupreader import read_groups
from args import read_arguments

def student_list(filename):
    results = []
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if row["Section"] == "":
                continue
            group = row["Section"].split(' ')[1]
            username = row["SIS Login ID"].split("@")[0]
            real_name = row["Student"]
            results.append([username, real_name, group])
    return results

def get_assignments(students):
    group_counter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    names = []
    for filename in os.listdir('submissions/'):
        file_matched = False
        for username, real_name, group in students:
            if username in filename.lower():
                file_matched = True
                if username not in names:
                    group_counter[int(group)] += 1
                    names.append(username)
        if not file_matched:
            print("Incorrect submission: {}".format(filename))
    return group_counter


if __name__ == "__main__":
    conf = read_arguments()
    groups = read_groups(conf.ta_list)
    students = student_list(conf.student_list)
    good_assignments = get_assignments(students)
    for group, number in good_assignments.items():
        print("{}\t{}".format(groups[group], number))
