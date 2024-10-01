import os
import subprocess
from setuptools import setup
from Cython.Build import cythonize

def obfuscate_file_with_cmd(file_path):
    try:
        command = f'pyshield -f {file_path} -l 2 -o {file_path}'
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully obfuscated: {file_path}")
        else:
            print(f"Failed to obfuscate {file_path}: {result.stderr}")
    
    except Exception as e:
        print(f"Error while obfuscating {file_path}: {str(e)}")

def obfuscate_folder_with_cmd(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Directory {folder_path} does not exist.")
        return
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py") and file != 'compile.py':
                file_path = os.path.join(root, file)
                obfuscate_file_with_cmd(file_path)

def compile_project_to_cython(source_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".py") and file != 'obfuscate.py':
                py_file = os.path.join(root, file)
                
                os.chdir(root)

                setup(
                    ext_modules=cythonize(file, compiler_directives={'language_level': "3"}),
                    script_args=['build_ext', '--inplace']
                )

                os.remove(py_file)
                print(f"Deleted: {py_file}")

                c_file = os.path.splitext(py_file)[0] + ".c"
                if os.path.exists(c_file):
                    os.remove(c_file)
                    print(f"Deleted: {c_file}")

                print(f"Compiled and saved in: {root}")

def obfuscate_and_compile_inplace(source_dir):
#     obfuscate_folder_with_cmd(source_dir)
    
    compile_project_to_cython(source_dir)

if __name__ == "__main__":
    folder_path = os.getcwd()
    obfuscate_and_compile_inplace(folder_path)
