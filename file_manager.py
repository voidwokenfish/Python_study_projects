from pathlib import Path
from PIL import Image

path_var = Path('.')
full_path = path_var.resolve()
current_dir = full_path.parts[-1]
upper_dir = full_path.parent
print(upper_dir)

#inside = path_var.resolve()
#elements = path_var.iterdir()
#list_of_files = list(path_var.iterdir())
#enumerated_list = enumerate(list_of_files)
our_directory_no_0 = {}
our_directory = {}
def file_manager(directory: dict):
    print(f'Весь путь - {full_path}')
    print(f'Текущая папка - {current_dir}')
    print('0) -- Подняться выше')
    print("Файлы внутри:")
    for key in directory:
        print(f'{key}) {directory[key]}')

def analysator4000():
    our_directory_no_0 = {number: (file) for number, file in enumerate(path_var.iterdir(), start=1)}
    our_directory = {
        0: upper_dir,
        **our_directory_no_0
    }
    file_manager(our_directory)
    choice = (input("Выберите файл или директорию, набрав его номер - "))
    if choice.isdigit():
        choice = int(choice)
        print(f"Your choice is {choice}")
        if choice in our_directory.keys():
            chosen = our_directory[choice]

            def reader(file_name):

                if file_name.is_dir():
                    global path_var
                    global full_path
                    global current_dir
                    global upper_dir
                    path_var = Path(chosen)
                    full_path = path_var.resolve()
                    current_dir = full_path.parts[-1]
                    upper_dir = full_path.parent
                    analysator4000()
                elif file_name.suffix in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
                    image = Image.open(file_name)
                    image.show()
                    image.close()
                else:
                    with file_name.open('r', encoding="utf-8") as file:
                        for line in file:
                            print(file.readline())
            return reader(chosen)
        else:
            print("Некорректный ввод, файла с таким номером нет в списке.")
            return analysator4000()
    else:
        print("Некорректный ввод, укажите число.")
        return analysator4000()


analysator4000()