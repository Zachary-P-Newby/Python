from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_full_sentance, get_adjective
import random
import pytest
#--------------------------------------------------------------------------------------------------

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
#--------------------------------------------------------------------------------------------------

def test_get_noun():
    #test single noun
    nouns_single = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range(11):
        noun = get_noun(1)
        assert noun in nouns_single

    #test plural noun
    nouns_plural = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(11):
        noun = get_noun(2)
        assert noun in nouns_plural


#--------------------------------------------------------------------------------------------------

def test_verb():
    #test past verbs
    verbs_past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    for _ in range(11):

        verb = get_verb(1, "past")
        assert verb in verbs_past
    
    #test future verbs
    verbs_future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    for _ in range(11):

        verb = get_verb(1, "future")
        assert verb in verbs_future
    
    #test present single verbs
    verbs_present_single = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    for _ in range(11):

        verb = get_verb(1, "present")
        assert verb in verbs_present_single

    #test present plural verbs
    verbs_present_plural = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    for _ in range(11):

        verb = get_verb(2, "present")
        assert verb in verbs_present_plural
#--------------------------------------------------------------------------------------------------
#test get preposistion

def test_preposistion():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for num in range(0,10):
        prep = get_preposition()
        assert prep in prepositions
#--------------------------------------------------------------------------------------------------
#test adjective

def test_adjective():
    adjectives =["wild", "buggy", "smelly", "purple", "grassy", "old", "young", "new", "feral", "tame", "yellow", "fast", \
    "slow", "chaotic", "cheesy", "mild", "sweet", "sour", "wimpy", "lame", "hot", "cold", "cool", "frozen", "blazing"]

    for num in range(1,11):
        assert get_adjective() in adjectives



#--------------------------------------------------------------------------------------------------
#test get preposistional_pharse

def test_preposistional_phrase():
    phrases = []

    for num in range(0,5):
        phrases.append(get_prepositional_phrase(random.randint(1,3)))
    
    for phrase in phrases:
        phrase = phrase.split()
        assert len(phrase) == 4

#--------------------------------------------------------------------------------------------------
#test get_full_sentance

def test_full_sentance():
    sen = get_full_sentance(1, "past")
    sen = sen.split()

    assert len(sen) == 8

    plur = get_full_sentance(2, "present")
    plur = plur.split()

    assert len(plur) == 8

#--------------------------------------------------------------------------------------------------
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])