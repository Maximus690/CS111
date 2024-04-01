import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def read_input_file(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]


def write_output_file(file_name, data):
    with open(file_name, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')


def main(args):
    if len(args) != 3:
        print("Usage: python mergesort.py input_file.txt output_file.txt")
        sys.exit(1)

    input_file = args[1]
    output_file = args[2]

    unsorted_data = read_input_file(input_file)
    sorted_data = merge_sort(unsorted_data)
    write_output_file(output_file, sorted_data)


if __name__ == "__main__":
    main(sys.argv)
