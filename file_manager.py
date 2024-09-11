from pathlib import Path
from PIL import Image

path_var = Path('.')
#inside = path_var.resolve()
#elements = path_var.iterdir()
#list_of_files = list(path_var.iterdir())
#enumerated_list = enumerate(list_of_files)
our_directory = {}
def file_manager(directory: dict):
    for key in directory:
        print(f'{key}) {directory[key]}')

def analysator4000():
    print(path_var.resolve())
    our_directory = {number: (file) for number, file in enumerate(path_var.iterdir(), start=1)}
    file_manager(our_directory)
    choice = (input("Выберите файл или директорию, набрав его номер - "))
    if choice.isdigit():
        choice = int(choice)
        print(f"Your choice is {choice}")
        if choice in our_directory.keys():
            print(f'Имя файла - {our_directory[choice]}')
            chosen = our_directory[choice]

            def reader(file_name):

                if file_name.is_dir():
                    print(list(file_name.iterdir()))
                    for root, dirs, files in file_name.walk('.'):
                        print(root, dirs, files)
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