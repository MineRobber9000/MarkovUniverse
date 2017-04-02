import markov,tvdb_api

t = tvdb_api.Tvdb(language="en")
first = True
synopses = markov.Chain()
for season in t['Steven Universe']:
	if first:
		first = False
		continue
	for episode in t['Steven Universe'][season]:
		synopses.train(t['Steven Universe'][season][episode]['overview'])
with open("synopses.json","w") as f:
	f.write(synopses.to_json())
