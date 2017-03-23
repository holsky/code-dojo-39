animal = ("fly", "I don't know why she swallowed a {0} - perhaps she'll die!")
closing_animal = "horse"

stanza = """There was an old lady who swallowed a {0}.
I don't know why she swallowed a {0} - perhaps she'll die!"""

stanzas = """There was an old lady who swallowed a spider;
That wriggled and wiggled and tickled inside her.
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a bird;
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
	return stanza.format(animal[0]) + "\n\n"

def original_song():
	return get_first_stanza() \
		+ stanzas.format(animal[0]) \
		+ closing.format(closing_animal)

if __name__ == '__main__':
	print(original_song())
