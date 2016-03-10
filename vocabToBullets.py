import glob

def loadFiles(path):
	fileToText = {}
	for filename in glob.glob(path):
		with open(filename) as f:
			fileToText[filename] = f.read().replace("\\", "").replace("-","").lower().split("\n")
	return fileToText

def loadVocab(wordpath):
	with open(wordpath) as w:
		ws = w.read().lower().strip().split("\n")
	return ws

def wordSearch(word, fileToText):
	resultsDict = {key: [] for key in fileToText.keys()}
	for key in fileToText:
		for line in fileToText[key]:
			if word in line:
				resultsDict[key].append(line)
	return resultsDict


def main(outfile):
	fTT = loadFiles("/Users/aakashjapi/history168A/*.rtf")
	with open(outfile, 'w') as f:
		for word in loadVocab("words.txt"):
			f.write("\n" + word.title() + ": \n")
			resultsDict = wordSearch(word, fTT)
			for key in resultsDict:
				if resultsDict[key]:
					f.write("\n\t" + key + ": \n")
					for line in resultsDict[key]:
						f.write("\t\t " + line + "\n ")

if __name__ == "__main__":
	main("defs.txt")
