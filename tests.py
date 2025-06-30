from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)
    # print("")

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)

    # result = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(result)

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)

    # - Get File Content Tests -

    # result = get_file_content("calculator", "lorem.txt")
    # print("Result for 'lorem.txt':")
    # print(result)

    # result = get_file_content("calculator", "main.py")
    # print("Result for 'main.py':")
    # print(result)

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for 'pkg/calculator.py':")
    # print(result)

    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for '/bin/cat':")
    # print(result)

    # - Write File Tests - 
    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print("Result for lorem.txt:")
    # print(result)

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print("Result for pkg/morelorem.txt:")
    # print(result)

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print("Result for /tmp/temp.txt")
    # print(result)

    # - Run Python Tests - 
    result = run_python_file("calculator", "main.py")
    print("Result for main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result for tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result for tests.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for tests.py")
    print(result)

if __name__ == "__main__":
    test()
