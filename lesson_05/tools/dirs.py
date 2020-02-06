from pathlib import Path, PureWindowsPath


def get_or_make_output_folder_near_file(file, folder_name='output_files'):
    script_dir_path = Path(file).resolve().parent
    folder_path = script_dir_path.joinpath(folder_name)

    slash = '\\' if isinstance(folder_path, PureWindowsPath) else '/'

    while not folder_path.is_dir() and folder_path.exists():
        print(f'Not valid path {folder_path}')

        output_dir = input(f'Output dir: {script_dir_path}{slash}')
        folder_path = script_dir_path.joinpath(output_dir)

    folder_path.mkdir(exist_ok=True)

    return folder_path

