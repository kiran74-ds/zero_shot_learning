import gensim

class Word2vec():

    def __init__(self, model_path=WORD2VECMODEL):
        ## Download and keep Google Word2Vec model in the path and assign that path to WORD2VECMODEL 
        self.model_path  = model_path
        self.model       = gensim.models.KeyedVectors.load_word2vec_format(self.model_path, binary=True)
        self.vocab       = self.model.vocab.keys()
    
    def generate_word2vec(self, words):
        print('Number of words  : ' + str(len(words)))
        vectors = list()
        for i,word in enumerate(words):
            print(str(i+1) + "\t" + str(word))
            if ' ' in word:
                word1, word2 = word.split(' ')

                if word1 in self.vocab:
                    vec1 = self.model[word1]
                else:
                    print("Word {} not in vocab".format(word))
                    vectors.append([0])
                    continue

                if word2 in self.vocab:
                    vec2 = self.model[word2]
                else:
                    print("Word {} not in vocab".format(word))
                    vectors.append([0])
                    continue

                vec3 = (vec1 + vec2)/2.
                vectors.append(vec3)
                continue

            if word in self.vocab:
                vectors.append(self.model[word])

            else:
                print("Word {} not in vocab".format(word))
                vectors.append([0])
        return vectors