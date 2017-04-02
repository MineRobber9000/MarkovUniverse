import random,json
class Chain:
	def __init__(self):
		self.map = {}

	def addWord(self,lastWord,word):
		if lastWord in self.map and not word in self.map[lastWord]:
			self.map[lastWord].append(word)
		elif not lastWord in self.map:
			self.map[lastWord] = [word]

	def train(self,sentance):
		words = sentance.split(" ")
		lastWord = words.pop(0)
		self.addWord("",lastWord)
		for word in words:
			self.addWord(lastWord,word)
			lastWord = word
		self.addWord(lastWord,"")

	def generate(self):
		lastWord = random.choice(self.map[""])
		sentence = lastWord
		while lastWord != "":
			word = random.choice(self.map[lastWord])
			sentence += " " + word
			lastWord = word
		return sentence[:-1]

	def to_json(self):
		return json.dumps(self.map)

	@classmethod
	def from_json(cls,jsonstr):
		ret = cls()
		ret.map = json.loads(jsonstr)
		return ret

def addLinesFromFile(chain,filename):
	with open(filename) as f:
		for line in f.readlines():
			chain.train(line.rstrip())
