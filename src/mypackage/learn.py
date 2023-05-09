import os


def star(name: str) -> str:
    """Return the description of input name.

    :param name: the input name.

    :returns: the output description.
    """
    return 'name: {0}'.format(name)


path = r'D:\metal\usefudata\1\9'
total_txt = os.listdir(path)

for file_name in total_txt:
    file_path = os.path.join(path, file_name)

    with open(file_path, 'r+') as file1:
        lines = file1.readlines()
        for index, line in enumerate(lines):
            if index == 2:
                lines[index] = '%nprocshared=16\n'

        file1.seek(0)  # 将文件指针移到文件开头
        file1.writelines(lines)
        file1.truncate()  # 清空文件多余内容
