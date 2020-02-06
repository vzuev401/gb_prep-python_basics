from pathlib import Path


script_dir_path = Path(__file__).resolve().parent
origin_file_path = script_dir_path.joinpath('origin_files', 'task_02_origin')

with open(origin_file_path) as file:
    lines = file.readlines()

    print('Count of lines:', len(lines))
    print('Count of words:')
    for number, line in enumerate(lines, start=1):
        print(f'- line {number}: {len(line.split())} ({line.strip()})')

