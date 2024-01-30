import sys
from collections import namedtuple
# import os
import pathlib


File = namedtuple(
    "File",
    ["filename", "extension", "is_directory", "parent"]
)

def get_dir_info(path: pathlib.Path | str) -> list[File]:
    base_dir = pathlib.Path(path)
    # print(base_dir)
    result = []
    for file in base_dir.iterdir():
        result.append(File(file.name, file.suffix, file.is_dir(), file.parent))
        # print(file.name)
    # print(*result, sep="\n\n")
    return result

def command_run(*args) -> pathlib.Path:
    if len(args) == 1:
        return pathlib.Path.cwd()
    print(args)
    _, path, *_ = args
    return pathlib.Path(path)

if __name__ == "__main__":
    args = command_run(*sys.argv)
    print(args)
    args = r"D:\PycharmProjects\112121212121\Погружение в Python (семинары)\Урок 2"
    print(args)
    print(*get_dir_info(args), sep="\n")

























