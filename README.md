# NLP-based-Assistant (NIKAI)
## A simple assistant which can prove useful for: 
* Queries on weather/forecast/temperature retrieval
* Obtaining Wikipedia definitions on words
* Listing out Synonyms of word
* Listing out Antonyms of a word

#### Uses basic NLP for processing input. GloVe embeddings used for word similarity. API calls are made for obtaining weather/definitions/synonyms/antonyms.

Download GloVe dataset, and change lines 4 and 5 in ```similarity.py``` as required. 

### Usage

```python main.py```
```export PYTHONWARNINGS="ignore"``` to remove dictionary api warnings if needed


### References
http://xrds.acm.org/blog/2017/01/build-natural-language-processing-based-intelligent-assistant-using-python-easy/
https://nlp.stanford.edu/projects/glove/

### Future Enhancements
* Improve number of things the assistant can do.
* Train pos_tag for tagging according to application's need.
* Stemming and Lemmatization for reducing the calls to word similarity.
