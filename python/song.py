import collections

animal = collections.namedtuple('struct', 'name phrase')

animals = [
	animal("fly", "I don't know why she swallowed a {0} - perhaps she'll die!"),
	animal("spider", "That wriggled and wiggled and tickled inside her."),
	animal("bird", "How absurd to swallow a {0}.")
]
closing_animal = "horse"

opening = "There was an old lady who swallowed a {0}"

swallow_phrase = "She swallowed the {0} to catch the {1}"

stanzas = """There was an old lady who swallowed a cat;
Fancy that to swallow a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

"""

closing = """There was an old lady who swallowed a {}...
...She's dead, of course!"""

def format_animal_phrase(n):
	return animals[n].phrase.format(animals[n].name)

def format_swallow_phrase(n):
	return swallow_phrase.format(animals[n].name, animals[n - 1].name)

def format_opening(n):
	return opening.format(animals[n].name) + ("." if n == 0 else ";")

def build_stanza(n):
	stanza = format_opening(n) + "\n" \
		+ format_animal_phrase(n) + "\n"
	for i in range(n, 0, -1):
		stanza += format_swallow_phrase(i) + ("," if i > 1 else ";") + "\n"
	if n > 0:
		stanza += format_animal_phrase(0) + "\n"
	return stanza

def original_song():
	return build_stanza(0) + "\n" \
		+ build_stanza(1) + "\n" \
		+ build_stanza(2) + "\n" \
		+ stanzas \
		+ closing.format(closing_animal)

if __name__ == '__main__':
	print(original_song())
