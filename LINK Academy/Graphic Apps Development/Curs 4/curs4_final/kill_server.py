import subprocess

COMMAND = "kill -9 $(lsof -t -i:8000)"

subprocess.run([COMMAND], shell=True)

subprocess.run(["ls"], shell=True)

subprocess.run(["touch split_files.py"], shell=True)

