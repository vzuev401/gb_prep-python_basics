from pathlib import Path
import re


script_dir_path = Path(__file__).resolve().parent
origin_file_path = script_dir_path.joinpath('origin_files', 'task_06_origin')


subjects_with_hours = {}
with open(origin_file_path) as file:
    for line in file:
        subject, hours_str = line.split(':', 1)
        hours_list = map(int, re.findall(r'\d+', line))

        subjects_with_hours[subject] = sum(hours_list)

print(subjects_with_hours)

