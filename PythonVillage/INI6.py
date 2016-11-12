dataset = "We tried list and we tried dicts also we tried Zen"
dataset_words = dataset.split(' ')
word_count = {}
for word in dataset_words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

for k,v in word_count.items():
    print(k, v, sep=" ")