def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with text and numbers: 5678\n")
        print("File created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the file: {e}")
    finally:
        file.close()


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        file.close()


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("Data appended to the file successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        file.close()


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Reading the file again to display the appended content