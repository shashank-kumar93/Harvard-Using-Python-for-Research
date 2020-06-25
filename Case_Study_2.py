import pandas as pd
import numpy as np

def read_book(title_path):
	"""
	Read a book and retunr it as a string.
	"""
	
	with open(title_path, "r", encoding="utf8") as current_file:
		text = current_file.read()
		text = text.replace('\n','').replace('\r', '')
	return text


def count_words_fast(text):
	"""
	Count the number of times each word occurs in text (str). Return
	dictionnary where keys are unique words and values are word counts.
	Skip punctuation.
	"""
	text = text.lower()
	skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]  # remove all punctuations
	# punctuations can lead to misleading counting...
	
	from collections import Counter

	for ch in skips:
		text = text.replace(ch, "")

	word_counts = Counter(text.split())
	
	return word_counts 	

def word_stats(word_counts):
	"""
	Return number of unique words and word frequencies.
	"""
	
	num_unique = len(word_counts) # number of unique words in the dict
	counts = word_counts.values() # list of word counts
	return (num_unique, counts)


def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data['frequency'] = np.where(data['count'] > 10, 'frequent',
	np.where(data['count'] == 1, 'unique', 'infrequent'))

    #print (data[data.frequency == 'frequent'].count())
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)


#Exercise1
hamlets = pd.DataFrame({'language': [], 'text' :[]})
#or hamlets=pd.DataFrame(columns=['language', 'text'])

hamlets = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@hamlets.csv", 
                      index_col=0)


#Excercise2
language, text = hamlets.iloc[0]
text = text.lower()
text = text.replace('\n','').replace('\r', '')
counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

#Excercise3
data['frequency'] = np.where(data['count'] > 10, 'frequent',
np.where(data['count'] == 1, 'unique', 'infrequent'))

data["length"] = data["word"].apply(len)

#Excercise4
sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })


#Excercise5

grouped_data = pd.DataFrame(columns = [
		"language", "frequency", "mean_word_length", "num_words"])

for i in range(hamlets.shape[0]):
        
    language, text = hamlets.iloc[i]
    text = text.lower()
    text = text.replace('\n','').replace('\r', '')
    
    grouped_data = grouped_data.append(summarize_text(language,text))


#Excercise6
colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.show()


