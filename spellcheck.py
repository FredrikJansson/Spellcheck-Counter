# ===============================
# =           Imports           =
# ===============================

try:
	import enchant
	import os
except:
	raise ImportError()

# ===============================
# =           Classes           =
# ===============================

class SpellCheck:

	def __init__(self, entry):
		""" Variables """
		d = enchant.Dict("en_US")
		errorCount = 0
		errorList = list()

		""" Reading data. """
		if os.path.exists(entry):
			with open(entry, "r") as f:
				data = [word for line in f for word in line.split()]
		else:
			data = entry.split()

		""" Checking words. """
		for word in data:
			if not d.check(word):
				errorCount += 1
				errorList.append(word)

		""" Saving results. """
		self.errorCount = errorCount
		self.errorList = errorList
		

	def printErrors(self):
		print("\tTotal amount of errors:", self.errorCount)
		if len(self.errorList):
			print("Errors were the following:")
			print(self.errorList)
		return 0

# ====================================
# =           Main Section           =
# ====================================

if __name__ == '__main__':
	sc = SpellCheck("Spellz like a tchamp.")
	sc.printErrors()
