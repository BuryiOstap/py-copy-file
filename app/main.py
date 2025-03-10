def copy_file(file_copy: str) -> None:
    file_copy = file_copy.split()
    if len(file_copy) == 3 and file_copy[0] == "cp":
        try:
            with (open(file_copy[1], "r") as current_file,
                  open(file_copy[2], "w") as new_file):
                new_file.write(current_file.read())
        except FileNotFoundError:
            print(f"File {file_copy[1]} not found.")
