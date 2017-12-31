import os
import nltk
import sys
from weather import Weather
from nltk.corpus import wordnet
import similarity
import wikipedia
from PyDictionary import PyDictionary
import pytemperature
dictionary=PyDictionary()
weather = Weather()


def get_input():
    #get input from user
    print "Is there anything I can do for you?"
    #query = raw_input( )
    query= "climate in Delhi?"
    print query
    process_query(query)


def process_query(query):
    query_tokens = nltk.word_tokenize(query)
    #print query_tokens
    stop_words = set(nltk.corpus.stopwords.words('english'))
    #print stop_words
    filtered_query = [w for w in query_tokens if not w in stop_words]
    #print filtered_query
    tagged_query= nltk.pos_tag(filtered_query)
    #print tagged_query
    #ner_tagged_query = nltk.ne_chunk(tagged_query)
    #print ner_tagged_query
    #print type(ner_tagged_query)
    proper_nouns= []
    nouns = []
    verbs = []
    adjectives= []
    for i in range(0, len(tagged_query)):
        if 'NNP' == tagged_query[i][1]:
            proper_nouns.append(tagged_query[i][0])
        if 'NN' == tagged_query[i][1] or 'NNS'==tagged_query[i][1]:
            nouns.append(tagged_query[i][0])    
        if 'J' in tagged_query[i][1]:
            adjectives.append(tagged_query[i][0]) 
        if 'V' in tagged_query[i][1]:
            verbs.append(tagged_query[i][0])      
    #print proper_nouns
    #print verbs
    #print nouns
    #print adjectives
    target = 'null'
    print ""

    
    if (len(adjectives)>0):
        #print "Computing similarity for words in " ,adjectives
        (target,t_word) = similarity.compute_similarity(adjectives)
    if target == 'null':
        if (len(nouns)>0):
                #print "Computing similarity for words in " ,nouns
                (target,t_word) = similarity.compute_similarity(nouns)
    if target == 'null':    
        if (len(verbs)>0):
                #print "Computing similarity for words in " , verbs
                (target,t_word) = similarity.compute_similarity(verbs)             

   
    #print (target,t_word)
    
    roi = []
    for x in adjectives+nouns+verbs+proper_nouns:
        if x== t_word:
            continue
        else: 
            roi.append(x)

    #print "roi = ",roi
    #print "target = ",target       

    if target=='f':
        place = proper_nouns
        if(len(proper_nouns)==0):
            #print "Place not recognized"
            #exit(0)
            place= roi    
        print "Place: ",str(place[0]) 
        location = weather.lookup_by_location(str(place[0]))
        condition = location.condition()   
        #print("In "+proper_nouns[0]+" it is currently: "+ condition.text())
        forecast = location.forecast()
        print "Date:",forecast[0].date()
        print "Condition:", forecast[0].text()
        print "Current:", str(pytemperature.f2c(int(condition.temp()))),"C"
        print "Highest:",str(pytemperature.f2c(int(forecast[0].high()))),"C"
        print "Lowest:",str(pytemperature.f2c(int(forecast[0].low()))),"C"
        
    elif target=='h' or target=='c' or target=='t':
        place = proper_nouns
        if(len(proper_nouns)==0):
            #print "Place not recognized"
            #exit(0)
            place= roi    
        print "Place: ",str(place[0]) 
        location = weather.lookup_by_location(str(place[0]))
        condition = location.condition()
        #print type(int(condition.temp()))    
        print "In "+place[0]+", the temperature is: "+ str(pytemperature.f2c(int(condition.temp()))),"C" 

       
    elif target=='d':
        definitions = dictionary.meaning(str(roi[0]))           
        for k,v in definitions.iteritems():
            for meanings in v:
                print meanings        
        print wikipedia.summary(str(roi[0]))
        #roi_p = wikipedia.page(str(roi[0]))
        #print roi_p.content

    elif target=='s':
        syn= (dictionary.synonym(str(roi[0])))        
        for i in  syn:
            print i        
        #todo synonyms
        #print "syn"
    elif target == 'a':
        ant= (dictionary.antonym(str(roi[0])))        
        for i in  ant:
            print i        
        #todo antonyms
        #print "antonym"
    else:
        print "Can't process query"
        exit(0)      



if __name__ == '__main__':
    get_input()
