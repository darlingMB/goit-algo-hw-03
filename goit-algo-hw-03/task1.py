import os
import shutil
import sys

# Функція для створення директорії, якщо вона не існує
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Рекурсивна функція для копіювання та сортування файлів
def copy_and_sort_files(src_dir, dest_dir="dist"):
    try:
        # Перевірка, чи є вихідна директорія
        if not os.path.exists(src_dir):
            print(f"Вихідна директорія '{src_dir}' не існує.")
            return

        # Створення директорії призначення, якщо вона не існує
        create_directory(dest_dir)

        # Перебір елементів у директорії
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dest_path = os.path.join(dest_dir, item)

            if os.path.isdir(src_path):
                # Якщо елемент - це директорія, викликаємо функцію рекурсивно
                new_dest_dir = os.path.join(dest_dir, item)
                create_directory(new_dest_dir)
                copy_and_sort_files(src_path, new_dest_dir)
            elif os.path.isfile(src_path):
                # Якщо елемент - це файл, визначаємо розширення
                file_extension = item.split('.')[-1] if '.' in item else 'no_extension'
                extension_dir = os.path.join(dest_dir, file_extension)

                # Створення піддиректорії за розширенням файлу
                create_directory(extension_dir)

                # Копіювання файлу до відповідної піддиректорії
                shutil.copy(src_path, extension_dir)
                print(f"Файл '{item}' скопійовано до '{extension_dir}'")

    except Exception as e:
        print(f"Сталася помилка: {e}")


def main():
    path = input()
    if len(path) < 2:
        print("Необхідно вказати шлях до вихідної директорії.")
    else:
        copy_and_sort_files(path)


if __name__ == '__main__':
    main()