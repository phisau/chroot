import sys
from subprocess import run
from path import getcwd

def get_dependencies(file_name):
    out = []
    output = run(
        [
            "ldd",
            file_name,
        ],
        capture_output=True,
    )
    # raw ldd output
    dependencies = output.stdout.decode().split("\n")
    # only last column (awk '{print $7}')
    for library in dependencies:
        out.append(library.split(" ")[-1])

    out = out[2:]
    return out


# for lib in corected:
#    output2 = run(['ldd',lib, ], capture_output=True)
#    print(output2.stdout.decode())

def create_folder(file_name):
    root = getcwd()
    print(root)
    path = file_name.split('/')[:-1]
    print(path)
#    run(['mkdir', '-p', path)
    return path

def cp_to_chroot(file_name):
    pass
    
def main(file_name):
    library = sys.argv[1]
    list_of_deps = get_dependencies(file_name)
    print(list_of_deps)


if __name__ == "__main__":
    print(f"library: {sys.argv[1]}")
    create_folder('/usr/local/lib/libiconv.so.7.0')
    main(sys.argv[1])
