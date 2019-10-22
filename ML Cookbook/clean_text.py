
import re as clear

class process():
    def master_clean_text(text):
            #clean up all the html tags
            text = clear.sub(r'<.*?>','',text)
            #remove the unwanted punctation chars

            text = clear.sub(r"\\","",text)
            text = clear.sub(r"\'","",text)
            text = clear.sub(r"\"","",text)

            # coversion to lowercase to remove complexity
            text = text.strip().lower()

            #removing unwanted expressions

            unwanted = '!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'

            convert = dict((c," ") for c in unwanted)

            # str.maketrans() --->> creates a one to one mapping of a character to its translation/replacement.
            mapping_trans = str.maketrans(convert)

            text = text.translate(mapping_trans)

            return text
    #master_clean_text("<a> Say youre scrapping a text from you'r website !! WEll it might be swap CASE or unevened you wanna remove all the punctation's into separate WOrd !!!!</a>").split()
