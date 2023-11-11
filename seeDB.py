import chromadb
import json
import yake
from nrclex import NRCLex

path = 'db'
client = chromadb.PersistentClient(path)
collection = client.get_or_create_collection(name="MemoryDB")
#print(collection.peek())

filter={"type" : {"$eq" : "systemPrompt"}}
queries = ['0']
nResults = 1
response = collection.query(query_texts=queries, where=filter, n_results=nResults)
response = json.loads(json.dumps(response))
response = response['documents'][0][0]
#print(response)

topN = 3
keywordExtractor = yake.KeywordExtractor(stopwords=[])
keywords = keywordExtractor.extract_keywords(text='who are you')
keywords.sort(key=lambda e: e[1])
#print(keywords)
keywords = keywords[-topN:]
#print(keywords)
topKeywords = []
for kwPair in keywords:
    topKeywords.append(kwPair[0])
nResults = 1
generalInfo = collection.query(query_texts=topKeywords, n_results=nResults)
generalInfo = json.loads(json.dumps(generalInfo))
generalInfo = generalInfo['documents'][0][0]
#print(generalInfo)

n = NRCLex()
n.load_raw_text(text='fuck you i hate you')
print(n.top_emotions)