import sys

# note: does not handle wrapping first and last word of file for markov chains

def make_values(corpus, word_key):
    
    word_key = tuple(word_key)

    values_list = []
    
    file = open(corpus)


    lastword = ""
    last_key = ()

    for line in file:
        line = line.strip()
        words = line.split(" ")
        

        if last_key == word_key:
            values_list.append(words[0])


        if word_key[1] == words[0]:
        
            if word_key[0] == lastword:
                print word_key
                values_list.append(words[1])
                
    
        
        i = 0
        while i < len(words) - 2:
            if word_key[0] == words[i]:
                if word_key[1] == words[i + 1]:
                    values_list.append(words[i + 2])
            i += 1



        last_key = tuple(words[-2:])
        lastword = words[-1]

    return values_list

print('***')*33
# print make_values("green-eggs.txt", ('you', 'like'))
#print make_values("green-eggs.txt", ('a', 'mouse?'))
print('****')*33


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    file = open(corpus)
    markov_dictionary = {}
    word_key = ['None', 'None']
    word_list = []
    lastword = ""

#use for loop to make lines in file a list
    for line in file:
        line = line.strip()
        words = line.split(" ")

        # generate keys

        word_key[0] = lastword
        word_key[1] = words[0]
        
        if lastword:
            markov_dictionary[tuple(word_key)] = make_values(corpus, word_key)

        # tuple_key = tuple(word_key)

        # markov_dictionary[tuple_key] = markov_dictionary[tuple_key].append(make_values(corpus, word_key))

        # markov_dictionary =  markov_dictionary + {markov_dictionary[tuple_key]:make_values(corpus, word_key)}
        # markov_dictionary.update({tuple_key: make_values(corpus, word_key)})
        #markov_dictionary[tuple(word_key)] = []

        i = 0
        while i < len(words) - 1:
            word_key[0] = words[i]
            word_key[1] = words[i + 1]
            # tuple_key = tuple(word_key)
            
            # markov_dictionary[tuple_key] = markov_dictionary[tuple_key].append(make_values(corpus, word_key))


            # markov_dictionary =  markov_dictionary + {markov_dictionary[tuple_key]:make_values(corpus, word_key)}
      
            #markov_dictionary.update({tuple_key: make_values(corpus, word_key)})
            markov_dictionary[tuple(word_key)] = make_values(corpus, word_key)
            #markov_dictionary[tuple(word_key)] = []

            i += 1

        lastword = words[len(words) - 1]

    return markov_dictionary

print make_chains("gettsburg.txt")





# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# make_chains('green-eggs.txt')


# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
