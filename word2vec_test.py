import gensim
 
namaFileModel = "w2vec_wiki_id300_0.txt"
model = gensim.models.Word2Vec.load(namaFileModel)
sim = model.wv.most_similar("Jakarta")
print("10 kata terdekat dari Jakarta:{}".format(sim))
sim = model.wv.most_similar("Bandung")
print("10 kata terdekat dari Bandung:{}".format(sim))
 
sim = model.wv.similarity("Yogyakarta", "Surakarta")
print("Kedekatan Yogyakarta-Surakarta: {}".format(sim))
sim = model.wv.similarity("Yogyakarta", "Semarang")
print("Kedekatan Yogyakarta-Semarang: {}".format(sim))
 
sim = model.wv.most_similar_cosmul(positive=['minuman', 'rendang'], negative=['makanan'])
print("makanan-rendang, minuman-?: {}".format(sim))
sim = model.wv.most_similar_cosmul(positive=['mobil', 'honda'], negative=['motor'])
print("motor-honda, mobil-?: {}".format(sim))