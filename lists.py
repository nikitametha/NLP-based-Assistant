'''
from gensim.models import KeyedVectors
# load the Stanford GloVe model
filename = 'glove.6B.300d.txt.word2vec'

print "Loading GloVe model"
model = KeyedVectors.load_word2vec_format(filename, binary=False)
print "Loaded!"
print "Calculating.."

temp_t = model.most_similar(positive=['temperature'], topn=10)
hot_t =  model.most_similar(positive=['hot'], topn=10)
cold_t = model.most_similar(positive=['cold'], topn=10)
weather_t = model.most_similar(positive=['weather'], topn=10)
rain_t = model.most_similar(positive=['rain'], topn=10)
humidity_t = model.most_similar(positive=['humidity'], topn=10)
definition_t = model.most_similar(positive=['definition'], topn=10)
synonym_t = model.most_similar(positive=['synonym'], topn=10)
antonym_t = model.most_similar(positive=['antonym'], topn=10)
forecast_t = model.most_similar(positive=['forecast'], topn=10)

temp=['temperature']
hot=['hot']
cold=['cold']
weather=['weather']
rain = ['rain']
humidity = ['humidity']
synonym = ['synonym']
antonym = ['antonym']
forecast = ['forecast']
definition = ['definition']

for i in range(0,10):
    temp.append(str(temp_t[i][0]))
    hot.append(str(hot_t[i][0]))
    cold.append(str(cold_t[i][0]))
    weather.append(str(weather_t[i][0]))
    rain.append(str(rain_t[i][0]))
    humidity.append(str(humidity_t[i][0]))
    synonym.append(str(synonym_t[i][0]))
    antonym.append(str(antonym_t[i][0]))
    forecast.append(str(forecast_t[i][0]))
    definition.append(str(definition_t[i][0]))


print ""
print temp
print ""
print hot
print ""
print cold
print ""
print weather
print ""
print rain
print ""
print humidity
print ""
print synonym
print ""
print antonym
print ""
print forecast
print ""
print definition
'''

# the output after running above code is as follows..

temp = ['temperature', 'temperatures', 'humidity', 'celsius', 'fahrenheit', 'degrees', 'heat', 'precipitation', 'centigrade', 'coldest', 'measurements']

hot = ['hot', 'hottest', 'heat', 'warm', 'dry', 'heated', 'bubbling', 'hotter']

cold = ['cold', 'cool', 'chill', 'chilly', 'freezing', 'frigid', 'winter']

#weather = ['weather', 'conditions', 'report', 'meteorologists']

rain = ['rain', 'rains', 'torrential', 'downpour', 'rainfall', 'snow', 'weather', 'winds', 'downpours', 'rainy', 'fog']

humidity = ['humidity', 'moisture', 'humid',  'precipitation']

synonym = ['synonym', 'synonyms', 'homonym', 'abbreviation', 'synonymous', 'euphemism', 'nomen', 'same', 'similar', 'misnomer', 'interchangeably']

antonym = ['antonym', 'anti', 'dissimilar', 'opposite']

forecast = ['forecast', 'weather', 'report', 'forecasts', 'prediction', 'forecasting', 'predicting', 'estimate', 'analysis', 'forecasters', 'condition']

definition = ['definition', 'defined', 'definitions', 'defines', 'define', 'defining', 'imply', 'meaning', 'interpretation', 'mean', 'concept']