#Finish the directory listing for the Test scripts Directory listing. It has an error for not displaying the
# content of that folder

# ScriptCo Script Manager to organize scripts for testing purposes.
import os

def get_files_dict(directory_path):
    files_dict = {}
    i = 0
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        if os.path.isfile(item_path):
            i += 1
            files_dict[item] = (i , item_path)
    return files_dict


def main():
    print('Welcome to ScriptCo Script Manager')
    directory =os.path.expanduser('~\PycharmProjects\PythonScripts\TestScripts')
    folders = get_files_dict(directory)
    for i in folders:
        print(f"{folders}")

if __name__ == '__main__':
    main()