def write_file(file_name, file_content):
    # file_name can be a Path or str without .txt extension
    path = str(file_name) + '.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    path = str(file_name) + '.txt'
    with open(path, 'a', encoding='utf-8') as f:
        f.write(append_content)

def read_file(file_name):
    path = str(file_name) + '.txt'
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()