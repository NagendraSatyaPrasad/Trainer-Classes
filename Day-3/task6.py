import subprocess

result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)

output = result.stdout.splitlines()

files_dict = {}

for line in output:
    parts = line.split()

    if len(parts) < 4:
        continue

    if "<DIR>" in parts:
        continue

    try:
        size = int(parts[-2])
        filename = parts[-1]

        files_dict[filename] = size
    except:
        continue

print(files_dict)