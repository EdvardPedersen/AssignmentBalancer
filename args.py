import argparse

def read_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--student_list", type=str, required=True)
    parser.add_argument("-t", "--ta_list", type=str, required=True)
    return parser.parse_args()
