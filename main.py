import os
import nltk
import sys
from weather import Weather
from nltk.corpus import wordnet
weather = Weather()


def get_input():
    #get input from user
    #print "Is there anything I can do for you?"
    #query = raw_input( )
    query= "What is the weather like in Bangalore"
    print query
    process_query(query)


def process_query(query):
    query_tokens = nltk.word_tokenize(query)
    print query_tokens
    stop_words = set(nltk.corpus.stopwords.words('english'))
    #print stop_words
    filtered_query = [w for w in query_tokens if not w in stop_words]
    #print filtered_query
    #tagged_query= nltk.pos_tag(filtered_query)
    #print tagged_query
    #ner_tagged_query = nltk.ne_chunk(tagged_query)
    #print ner_tagged_query
    #print type(ner_tagged_query)
    if "weather" in filtered_query:
        #print "yes"
        print filtered_query[-1]
        location = weather.lookup_by_location(str(filtered_query[-1]))
        condition = location.condition()
        print("In "+filtered_query[-1]+" it is currently: "+ condition.text())
        forecasts = location.forecast()
        '''
        for forecast in forecasts:
            print(forecast.text(),(forecast.date()))
            print(forecast.high())
            print(forecast.low())
        '''

if __name__ == '__main__':
    get_input()