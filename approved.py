import argparse
import csv
import os
from collections import defaultdict
from args import read_arguments
from groupreader import read_groups

def student_list(filename):
    results = []
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if row["Section"] == "":
                continue
            assignment_status = get_assignment_status(row)
            group = row["Section"].split(' ')[1]
            username = row["SIS Login ID"].split("@")[0]
            real_name = row["Student"]
            try:
                int_group = int(group)
                results.append([username, real_name, int_group, assignment_status])
            except:
                pass
    return results

def get_assignment_status(row):
    assignment_names = defaultdict(list)
    assignment_scores = defaultdict(int)
    for key in row:
        for num in ['1', '2', '3']:
            if "oppgavesett " + num in key.lower() and "points" not in key.lower() and "score" not in key.lower():
                assignment_names[num].append(key)
    for num in assignment_names:
        for name in assignment_names[num]:
            number = row[name].split(',')[0]
            if number == "":
                continue
            assignment_scores[num] += int(number)
    return assignment_scores

if __name__ == "__main__":
    conf = read_arguments()
    groups = read_groups(conf.ta_list)
    students = student_list(conf.student_list)

    total_ass_1 = 0
    total_ass_2 = 0
    total_ass_3 = 0
    total_finished = 0

    for group in groups:
        print("##### Group {} - {} #####".format(group, groups[group]))
        for student in [x for x in students if x[2] == group]:
            output = "{:40s}".format(student[1])
            if student[3]['1'] >= 30:
                output = output + " - 1 OK"
                total_ass_1 += 1
            if student[3]['2'] >= 30:
                total_ass_2 += 1
            if student[3]['3'] >= 30:
                total_ass_3 += 1
            sum_last_assignments = min(student[3]['2'],30) + min(student[3]['3'], 30)
            if sum_last_assignments >= 50:
                output = output + " - 2&3 OK"
                total_finished += 1
            print(output)
    print("Number who finished assignment 1: {}".format(total_ass_1))
    print("Number who finished assignment 2: {}".format(total_ass_2))
    print("Number who finished assignment 3: {}".format(total_ass_3))
    print("Number who finished all assignments: {}".format(total_finished))

