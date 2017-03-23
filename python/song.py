import collections

animal = collections.namedtuple('struct', 'name phrase')

animals = [
	animal("fly", "I don't know why she swallowed a {0} - perhaps she'll die!"),
	animal("spider", "That wriggled and wiggled and tickled inside her.")
]
closing_animal = "horse"

opening = "There was an old lady who swallowed a {0}"

swallow_phrase = "She swallowed the {0} to catch the {1};"

stanzas = """There was an old lady who swallowed a bird;
How absurd to swallow a bird.
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a cat;
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

def get_first_stanza():
	return opening.format(animals[0].name) + "." + "\n" \
		+ animals[0].phrase.format(animals[0].name) \
		+ "\n\n"

def get_second_stanza():
	return opening.format(animals[1].name) + ";" + "\n" \
		+ animals[1].phrase + "\n" \
		+ swallow_phrase.format(animals[1].name, animals[0].name) + "\n" \
		+ animals[0].phrase.format(animals[0].name) + "\n" \
		+ "\n"

def original_song():
	return get_first_stanza() \
		+ get_second_stanza() \
		+ stanzas \
		+ closing.format(closing_animal)

if __name__ == '__main__':
	print(original_song())
