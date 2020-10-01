import clean_text

# import all our functions
from clean_text import *

#!pylint cleantext

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

training = [
    " I am master of all",
    "I am a absolute learner"
]

generalization = [
    "I am absolute learner learner"
]

vectorization = CountVectorizer(
    stop_words = "english",
    preprocessor = process.master_clean_text)

vectorization.fit(training)

build_vocab = {
     value:key 
     for key , value in vectorization.vocabulary_.items()
}

vocab = [build_vocab[i] for i in range(len(build_vocab))]

extracted = pd.DataFrame(
data = vectorization.transform(generalization).toarray(),
    index=["generalization"],
    columns=vocab
)

print(extracted) 
