import random

def main():
    """
Creates 6 sentances, each with a quantity, and a verb tense. Following this order:
Sentance    Quantity    Tense
 1.	  |      single   |   past
 2.	  |      single   |   present
 3.	  |      single   |   future
 4.	  |      plural   |   past
 5.	  |      plural   |   present
 6.	  |      plural   |   future

 Once all sentances are created they will be printed out for viewing purposes
    """
    sentance_list = []

    #sentance 1
    sentance_list.append(get_full_sentance(1, "past"))

    #sentance 2
    sentance_list.append(get_full_sentance(1, "present"))

    #sentance 3
    sentance_list.append(get_full_sentance(1, "future"))

    #sentance 4
    sentance_list.append(get_full_sentance(2, "past"))
    
    #sentance 5
    sentance_list.append(get_full_sentance(3, "present"))

    #sentance 6
    sentance_list.append(get_full_sentance(4, "future"))
    
    for sen in sentance_list:
        print(sen)



def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    #make random choice
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    else:
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        
    
    #make random choice
    word = random.choice(words)
    return word


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    word = random.choice(prepositions)

    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposistion = get_preposition()
    adjective = get_adjective()

    return f"{preposistion} {determiner} {adjective} {noun}"


def get_adjective():
    """Returns a random adjective"""

    adjectives =["wild", "buggy", "smelly", "purple", "grassy", "old", "young", "new", "feral", "tame", "yellow", "fast", \
    "slow", "chaotic", "cheesy", "mild", "sweet", "sour", "wimpy", "lame", "hot", "cold", "cool", "frozen", "blazing"]

    return random.choice(adjectives)


def get_full_sentance(quantity, tense):
    """Build and a return a complete sentance composed of a determiner, noun, verb, and preposistional phrase.
    
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a complete sentance.
    """
    
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    prep_phrase = get_prepositional_phrase(quantity)

    return f"{determiner.capitalize()} {adjective} {noun} {verb} {prep_phrase}."


if __name__ == "__main__":
    main()