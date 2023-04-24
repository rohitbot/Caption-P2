import pandas

def get_value_from_json(file_path, key):
    dic = pandas.read_json(path_or_buf=file_path, dtype="dictionary")
    return dic[key]