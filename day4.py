import re

require_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

with open("day4.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

current = " "
passports = []
for line in lines:
    if len(line) == 0:
        passports.append(current)
        current = " "
    else:
        current = current + " " + line
passports.append(current)

print("tottal number of passport: ", len(passports))


def passport_check(passport):
    for require in require_fields:
        if require not in passport:
            return 0
    return 1


valid_passports = 0
for passport in passports:
    valid_passports += passport_check(passport)

print("valid number of passport: ", valid_passports)


def strict_check(passport):
    content = {
        x.split(":")[0]: x.split(":")[1] for x in passport.split(" ") if x.strip()
    }

    if (
        not re.match(r"^\d{4}$", content["byr"])
        or int(content["byr"]) < 1920
        or int(content["byr"]) > 2002
    ):
        return 0
    if (
        not re.match(r"^\d{4}$", content["iyr"])
        or int(content["iyr"]) < 2010
        or int(content["iyr"]) > 2020
    ):
        return 0
    if (
        not re.match(r"^\d{4}$", content["eyr"])
        or int(content["eyr"]) < 2020
        or int(content["eyr"]) > 2030
    ):
        return 0

    match = re.match(r"^(\d+)(cm|in)$", content["hgt"])
    if not match:
        return 0
    elif match.group(2) == "cm" and (
        int(match.group(1)) < 150 or int(match.group(1)) > 193
    ):
        return 0
    elif match.group(2) == "in" and (
        int(match.group(1)) < 59 or int(match.group(1)) > 76
    ):
        return 0

    if not re.match(r"^#[0-9a-f]{6}$", content["hcl"]):
        return 0
    if content["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return 0
    if not re.match(r"^\d{9}$", content["pid"]):
        return 0
    return 1


valid_passports = 0
count = 0
for passport in passports:
    if passport_check(passport) and strict_check(passport):
        valid_passports += 1

    count += 1
print("valid passports strict role: ", valid_passports)