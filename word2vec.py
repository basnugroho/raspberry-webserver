from __future__ import print_function
 
# Ignore warnings dari gensim
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
 
import logging
import os.path
import sys
 
from gensim.corpora import WikiCorpus
 
program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)
 
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))
 
namaFileInput = "idwiki-latest-pages-articles.xml.bz2"
namaFileOutput = "wiki.id.text"
 
space = " "
i = 0
 
# Write file ke variabel namaFileOutput encoder utf-8
output = open(namaFileOutput, 'w', encoding='utf-8')
 
# lower=False: huruf kecil dan besar dibedakan
wiki = WikiCorpus(namaFileInput, lemmatize=False, dictionary={}, lower=False)
for text in wiki.get_texts():
    output.write(' '.join(text) + '\n')
    i = i + 1
    if i % 10000 == 0:
        logger.info("Saved " + str(i) + " articles")
 
output.close()
logger.info("Finished Saved " + str(i) + " articles")
