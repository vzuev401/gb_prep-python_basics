from tools import get_or_make_output_folder_near_file as get_folder


output_folder_path = get_folder(__file__)
output_file_path = output_folder_path.joinpath('task_01_output_file')


with open(output_file_path, 'w') as file:
    print(f'Input lines to write into file "{file.name}":')
    while user_input := input():
        file.write(user_input + '\n')

