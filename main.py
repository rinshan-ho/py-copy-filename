import pyperclip
import sys

paths = sys.argv[1:] # DDされた全ファイルをpathsに格納
paths.sort()

files = []
for path in paths:
    file = path.split('\\')[-1]
    files.append(file)
file_list = '\n'.join(files)

pyperclip.copy(file_list)
