class Passport:

	EYR_LIST = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
	REQUIRED_FIELS = ["ecl","pid","eyr","hcl","byr","iyr","hgt"]

	def __init__(self, ecl,pid,eyr,hcl,byr,iyr,hgt):
		self.ecl = ecl
		self.pid = pid
		self.eyr = eyr
		self.hcl = hcl
		self.byr = int(byr)
		self.iyr = int(iyr)
		self.hgt = hgt

	@staticmethod
	def isInfoSuffucient(diction):
		return all(item in diction.keys() for item in Passport.REQUIRED_FIELS)

	def isValid(self):
		if not(self.byr>=1920 and self.byr<=2002):
			return False

		if not(self.iyr>=2010 and self.iyr<=2020):
			return False

		if not(len(self.eyr)==4 and int(self.eyr)>=2020 and int(self.eyr)<=2030):
			return False

		if self.hgt.endswith("cm"):
			height = int(self.hgt[:-2])
			if not (height>=150 and height<=193):
				return False
		elif self.hgt.endswith("in"):
			height = int(self.hgt[:-2])
			if not (height>=59 and height<=76):
				return False
		else:
			return False

		if not(len(self.hcl)==7 and self.hcl.startswith("#") and all(c.isdigit() or c.islower() for c in self.hcl[1:])):
			return False

		if not (self.ecl in self.EYR_LIST):
			return False

		if not(all(c.isdigit() for c in self.pid) and len(self.pid)==9):
			return False

		return True

class SecurityService:
	@staticmethod
	def getData(location):
		text = open(location)
		lines = text.readlines()
		text.close()
		lines = "".join(lines).split("\n\n")
		return lines

	@staticmethod
	def parseString(string):
		entries = string.split()
		passportDict = { item.split(":")[0]:item.split(":")[1] for item in entries}
		return passportDict

	@staticmethod
	def countValidPassport(data):
		count = 0
		for line in data:
			diction = SecurityService.parseString(line)
			if not Passport.isInfoSuffucient(diction):
				continue
			passport = Passport(*[diction[item] for item in Passport.REQUIRED_FIELS])
			if passport.isValid():
				count+=1
		return count


if __name__ == "__main__":
	data = SecurityService.getData("input.txt")
	count = SecurityService.countValidPassport(data)

	print(count)
