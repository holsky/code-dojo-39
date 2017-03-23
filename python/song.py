import collections

animal = collections.namedtuple('struct', 'name phrase')

animals = [
	animal("fly", "I don't know why she swallowed a fly - perhaps she'll die!"),
	animal("spider", "That wriggled and wiggled and tickled inside her."),
	animal("bird", "How absurd to swallow a bird."),
	animal("cat", "Fancy that to swallow a cat!"),
	animal("dog", "What a hog, to swallow a dog!"),
	animal("cow", "I don't know how she swallowed a cow!")
]
closing_animal = "horse"

opening = "There was an old lady who swallowed a {0}"
swallow_phrase = "She swallowed the {0} to catch the {1}"
closing = """There was an old lady who swallowed a {}...
...She's dead, of course!"""

def format_swallow_phrase(n):
	return swallow_phrase.format(animals[n].name, animals[n - 1].name)

def format_opening(n):
	return opening.format(animals[n].name) + ("." if n == 0 else ";")

def build_stanza(n):
	stanza = format_opening(n) + "\n" \
		+ animals[n].phrase + "\n"
	for i in range(n, 0, -1):
		stanza += format_swallow_phrase(i) + ("," if i > 1 else ";") + "\n"
	if n > 0:
		stanza += animals[0].phrase + "\n"
	return stanza

def original_song():
	return ''.join([build_stanza(n) + "\n" for n in range(0, 6)]) \
		+ closing.format(closing_animal)

if __name__ == '__main__':
	print(original_song())
