import subprocess

from ImagemagickDriver.director import Director

TEST_FILE = "/Users/hborcher/Documents/471223_037.tif"


def main():
    print("Hello")
    command_builder = Director()

    print(command_builder.build_command(src=TEST_FILE, dst=TEST_FILE))
    # command.src = TEST_FILE
    # command.dst = "sadfas.jpg"
    # process = subprocess.Popen(command.command_list)
    # process.communicate()
    # print(process.returncode)


if __name__ == '__main__':
    main()

