import markov

def chainFromFile(filename):
	with open(filename) as f:
		return markov.Chain.from_json(f.read())

titles = chainFromFile("data/titles.json")
synopses = chainFromFile("data/synopses.json")

def new_episode():
	title = titles.generate()
	synopsis = synopses.generate()
	return (title,synopsis)

if __name__=="__main__":
	details = new_episode()
	print "New episode:\n{} - {}".format(*details)
