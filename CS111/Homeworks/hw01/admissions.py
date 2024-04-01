# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


def convert_row_type(rows: list[str]) -> list[float]:
    return [float(i) for i in rows]


def is_outlier(row):

    if row[2] == 0 or (row[1] * 2) - (row[0] / 160) > 2:
        return True
    else:
        return False


def calculate_score(row):
    return ((row[0] / 160) * 0.3) + ((row[1] * 2) * 0.4) + (row[2] * 0.1) + (row[3] * 0.2)


def calculate_score_improved(row):
    if is_outlier(row) or calculate_score(row) >= 6:
        return True
    else:
        return False


def grade_outlier(row):
    return sorted(row)[1] - sorted(row)[0] > 20


def grade_improvement(row):
    return row == sorted(row)


def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")

    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()
    rows = [line.strip().split(',') for line in input_file.readlines()]
    names = [row.pop(0) for row in rows]
    floats = [convert_row_type(row) for row in rows]
    for i in floats:
        if check_row_types(i) is False:
            print("there is an error")
            return False
    print(headers)

    list1 = [row[:4] for row in floats]
    list2 = [row[4:] for row in floats]
    scores = [calculate_score(row) for row in list1]

    out_file1 = open('student_scores.csv', "w")
    for i in range(len(names)):
        out_file1.write(f"{names[i]},{scores[i]:.2f}\n")

    out_file2 = open('chosen_students.csv', "w")
    [out_file2.write(names[i]+'\n') for i in range(len(names)) if scores[i] >= 6]

    outliers = [is_outlier(row) for row in list1]

    out_file3 = open('outliers.csv', "w")
    [out_file3.write(names[i]+'\n') for i in range(len(names)) if outliers[i]]

    out_file4 = open('chosen_improved.csv', 'w')
    [out_file4.write(names[i]+'\n') for i in range(len(names)) if scores[i] >= 6 or (outliers[i] and scores[i] >= 5)]

    improved_scores = [calculate_score_improved(row) for row in list1]
    print(improved_scores)
    out_file5 = open("better_improved.csv", "w")
    [out_file5.write(f"{names[i]},{list1[i][0]},{list1[i][1]},{list1[i][2]},{list1[i][3]}\n") for i in range(len(names)) if improved_scores[i]]

    outlier2 = [grade_outlier(row) for row in list2]
    improvement = [grade_improvement(row) for row in list2]

    print(outlier2)
    print(improvement)

    composite_chosen = [scores[i] >= 6 or (scores[i] >= 5 and (outliers[i] or outlier2[i] or improvement[i])) for i in range(len(names))]
    out_file6 = open("composite_chosen.csv", "w")
    print(composite_chosen)
    [out_file6.write(names[i]+'\n') for i in range(len(names)) if composite_chosen[i]]


    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions


if __name__ == "__main__":
    main()
