import collections

animal = collections.namedtuple('struct', 'name phrase')

original_animals = [
	animal("fly", "I don't know why she swallowed a fly - perhaps she'll die!"),
	animal("spider", "That wriggled and wiggled and tickled inside her."),
	animal("bird", "How absurd to swallow a bird."),
	animal("cat", "Fancy that to swallow a cat!"),
	animal("dog", "What a hog, to swallow a dog!"),
	animal("cow", "I don't know how she swallowed a cow!")
]
original_closing_animal = "horse"

_opening = "There was an old lady who swallowed a {0}"
_swallow_phrase = "She swallowed the {0} to catch the {1}"
_closing = """There was an old lady who swallowed a {}...
...She's dead, of course!"""

def _format_swallow_phrase(animals, n):
	return _swallow_phrase.format(animals[n].name, animals[n - 1].name)

def _format_opening(animals, n):
	return _opening.format(animals[n].name) + ("." if n == 0 else ";")

def _build_stanza(animals, n):
	stanza = _format_opening(animals, n) + "\n" \
		+ animals[n].phrase + "\n"
	for i in range(n, 0, -1):
		stanza += _format_swallow_phrase(animals, i) + ("," if i > 1 else ";") + "\n"
	if n > 0:
		stanza += animals[0].phrase + "\n"
	return stanza

def original_song():
	return song(original_animals, original_closing_animal)

def song(animals, closing_animal):
	return ''.join([_build_stanza(animals, n) + "\n" for n in range(0, len(animals))]) \
		+ _closing.format(closing_animal)

if __name__ == '__main__':
	print(original_song())
