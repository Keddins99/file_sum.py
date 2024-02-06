def file_sum(input_file):
    total_sum = 0

    with open(input_file, 'r') as file:
        for line in file:
            total_sum += float(line.strip())

    with open('sum.txt', 'w') as output_file:
        output_file.write(str(total_sum))