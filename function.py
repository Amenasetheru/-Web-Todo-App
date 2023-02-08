FILEPATH = "text.txt"


def read_todos_list(filepath=FILEPATH):
    # We open a file in mode read
    with open(filepath, "r") as file_to_read:
        todos = file_to_read.readlines()
    return todos


def write_todos_list(arg_for_todo, filepath=FILEPATH):
    # We create here a new file in mode write
    with open(filepath, "w") as file_to_write:
        file_to_write.writelines(arg_for_todo)


print(__name__)
if __name__ == "__main__":
    print("Hotep from function")
    print(read_todos_list("text.txt"))


