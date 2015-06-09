display_list = []

with open('C:/1save/test.csv') as data_file:
   for line in data_file:
      display_list.append(line.strip().split(','))

print(display_list[6]) # [i][j]

# 'C:/1save/test.csv'
