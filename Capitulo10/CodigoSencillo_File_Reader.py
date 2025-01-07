from pathlib import Path

path = Path('./textos/pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)