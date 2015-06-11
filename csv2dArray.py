# 注意！這個是用於Shift-JIS編碼的檔案，如果是UTF-8，要改那行編碼

def csvToArray(day_array):
    def_array = []
    with open(day_array, encoding = "shift-jis") as data_file:
        for line in data_file:
            def_array.append(line.strip().split(','))
        return def_array
