import unittest
import song

original_song = """There was an old lady who swallowed a fly.
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a spider;
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

There was an old lady who swallowed a horse...
...She's dead, of course!"""

first_stanza = """There was an old lady who swallowed a fly.
I don't know why she swallowed a fly - perhaps she'll die!
"""

second_stanza = """There was an old lady who swallowed a spider;
That wriggled and wiggled and tickled inside her.
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!
"""

third_stanza = """There was an old lady who swallowed a bird;
How absurd to swallow a bird.
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!
"""

custom_song = """There was an old lady who swallowed a frog.
Wait wog?

There was an old lady who swallowed a giraffe;
Wait baffe?
She swallowed the giraffe to catch the frog;
Wait wog?

There was an old lady who swallowed a lion;
Wait iron?
She swallowed the lion to catch the giraffe,
She swallowed the giraffe to catch the frog;
Wait wog?

There was an old lady who swallowed a norse...
...She's dead, of course!"""

class TestStringMethods(unittest.TestCase):

    def test_original_song(self):
        self.assertEqual(original_song, song.original_song())

    def test_first_stanza(self):
        self.assertEqual(first_stanza, song._build_stanza(song.original_animals, 0))   

    # this one is with the swallow phrase
    def test_second_stanza(self):
        self.assertEqual(second_stanza, song._build_stanza(song.original_animals, 1))

    # this one has a comma in the swallow phrase
    def test_third_stanza(self):
        self.assertEqual(third_stanza, song._build_stanza(song.original_animals, 2))

    def test_with_different_animals(self):
        animals = [
            song.animal("frog", "Wait wog?"),
            song.animal("giraffe", "Wait baffe?"),
            song.animal("lion", "Wait iron?")
        ]
        closing_animal = "norse"
        self.assertEqual(custom_song, song.song(animals, closing_animal))


if __name__ == '__main__':
    unittest.main()