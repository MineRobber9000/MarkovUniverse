import markov,tvdb_api

t = tvdb_api.Tvdb(language="en")
first = True
titles = markov.Chain()
for season in t['Steven Universe']:
	if first:
		first = False
		continue
	for episode in t['Steven Universe'][season]:
		titles.train(t['Steven Universe'][season][episode]['episodename'])
with open("titles.json","w") as f:
	f.write(titles.to_json())
