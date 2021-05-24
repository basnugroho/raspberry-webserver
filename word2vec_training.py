# Terlihat dari kode di atas line 13-18 menampilkan output proses pada setiap iterasi, output ini nanti akan menampilkan berapa jumlah artikel yang ada dalam data korpus. Line 20-21 nama file input dan ouput. Pada line 30-35 inilah proses konversi data dilakukan. Dari kode di atas akan menghasilkan output file dari rangkaian beberapa artikel, di mana satu barisnya mewakili satu artikel.
# Setelah data berhasil terkonversi, selanjutnya dilakukan training Word2Vec menggunakan kode berikut.

import multiprocessing
import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
 
program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)
 
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))
 
namaFileInput = "wiki.id.text"
namaFileOutput = "w2vec_wiki_id300_0.txt"
 
 
# size 300 = 300 dimensi vektor, window 10 = 10 pengaruh kata disekitarnya, min_count 5 = kata-kata yang muncul < 5 kali akan dikeluarkan dari kosakata dan diabaikan selama pelatihan, sg 0 = cbow / sg 1 = skip gram 
model = Word2Vec(LineSentence(namaFileInput), size=300, window=10, min_count=5, sg=0, workers=multiprocessing.cpu_count())
 
# trim unneeded model memory = use (much) less RAM
model.init_sims(replace=True)
model.wv.save_word2vec_format(namaFileOutput, binary=False)