import lists
'''
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = 'glove.6B.300d.txt'
word2vec_output_file = 'glove.6B.300d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)
'''
from gensim.models import KeyedVectors
# load the Stanford GloVe model
filename = 'glove.6B.300d.txt.word2vec'


def compute_similarity(word_list):
    '''
    print "Loading GloVe model"
    model = KeyedVectors.load_word2vec_format(filename, binary=False)
    print "Loaded!"
    print "Calculating.."
    temp_t = model.most_similar(positive=['temperature'], topn=10)
    hot_t =  model.most_similar(positive=['hot'], topn=10)
    cold_t = model.most_similar(positive=['cold'], topn=10)
    weather_t = model.most_similar(positive=['weather'], topn=10)
    temp=['temperature']
    hot=['hot']
    cold=['cold']
    weather=['weather']
    for i in range(0,10):
        temp.append(str(temp_t[i][0]))
        hot.append(str(hot_t[i][0]))
        cold.append(str(cold_t[i][0]))
        weather.append(str(weather_t[i][0]))


    print ""
    print temp
    print ""
    print hot
    print ""
    print cold
    print ""
    print weather
    '''
    #print "Computing.."
    #print "word list ",word_list

    for i in word_list:
        if i in lists.temp:
            return ('t',i)
        elif i in lists.hot:
            return ('h',i)
        elif i in lists.cold:
            return ('c',i)
        #elif i in lists.weather:
            #return 'w'
        elif i in lists.humidity:
            return ('h',i)
        elif i in lists.forecast:
            return ('f',i)
        elif i in lists.rain:
            return ('r',i)
        elif i in lists.definition:
            return ('d',i)
        elif i in lists.synonym:
            return ('s',i)
        elif i in lists.antonym:
            return ('a',i)
    else:
        return ('null','null') 




        



