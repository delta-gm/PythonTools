def get_uniques(list_in):
    list_out = []
    for k in list_in:
        if k not in list_out:
            list_out.append(k)
    return list_out

def txt_to_list(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [k.replace('\n', '') for k in lines]
        return lines

def list_to_txt(list_in, filename):
    with open(filename, 'w') as f:
        for line in list_in:
            f.write(line + '\n')

def txt_to_table(filename, split_by=','):
    lines = txt_to_list(filename)
    return [k.split(split_by) for k in lines]

def table_to_txt(table_in, filename, split_by=','):
    with open(filename, 'w') as f:
        for line in table_in:
            f.write(split_by.join([k for k in line]) + '\n')


# Sample code

data = ['apple', 'apple', 'banana', 'carrot']
data = get_uniques(data)  # Removes redundant 'apple'
list_to_txt(data, 'list_1d.txt')  # Saves a text file with 3 lines: apple, banana, carrot
data = txt_to_list('list_1d.txt')  # data is now a list ['apple', 'banana', 'carrot']
data_rows = []
for k in range(0, 3):
    data_rows.append(data)  # data_rows is now a table, a list of lists
table_to_txt(data_rows, 'table_2d.csv', split_by=',')  # Saves the 2d table as a csv
data_rows = txt_to_table('table_2d.csv', split_by=',')  # Reads the csv into a list of lists. This will work on .txt or .csv.
