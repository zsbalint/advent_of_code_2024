import re

file = open('input.txt', 'r')
content = file.read()

do_commands = []
dont_commands = []
# ki kell törölni a "fölösleges" részeket a contentből
for match in re.finditer("do\(\)", content):
    do_commands.append(match.start())

for match in re.finditer("don't\(\)", content):
    dont_commands.append(match.start())


# átmásoljuk a content tartalmát egy 'tisztított' változóba
cleaned_content = ''
copy = True
for i in range(len(content)):
    if i in do_commands:
        copy = True
    if i in dont_commands:
        copy = False
    if copy:
        cleaned_content += content[i]



matches = re.findall("mul\(\d{1,3},\d{1,3}\)", cleaned_content)

sum = 0
for item in matches:
    a, b = re.findall("\d{1,3}", item)
    sum += int(a)*int(b)

print(sum)


