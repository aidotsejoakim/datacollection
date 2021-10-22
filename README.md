# datacollection
This GitHub is created by the participants at AI Sweden Young Talent Program and includes datasets and code used to create datasets. 

## Folder and Files

### Datasets
This folder includes json-files with data. The data should include a label and a text. Please note that the roles are reverse. The label includes a text string (e.g. a movie review) and the text string describes the label (e.g. either 'positive' or 'negative' if it is a movie review). The reason behind this is that the text string in our case is the dependent variable and therefore the label. 

[Google colab link for a dataset containing 560 000 yelp-reviews](https://drive.google.com/file/d/1QfiY0svqTVS2XIK5jyDA2FNweLaSffPK/view?usp=sharing)

[Google colab link for a dataset containing 5,6 million examples of text to title, bier climatefever](4/1AX4XfWjh1-YTpCjkQd2pqExxWSRHNqZxsd0ECmV7xTT8nk0J43VJyYj0xMc)

This is the number of datapoints in each dataset produced by countJsonFiles.py:<br />
app_reviews.json:     288065<br />
contradictions.json:     570152<br />
corpusdataset.json:     3633<br />
cosmosqadataset.json:     35210<br />
GigawordDataset4.json:     150000<br />
goEmotionsDataset.json:     43410<br />
hellaswag.json:     49947<br />
piqadataset.json:     21035<br />
quest.json:     87599<br />
sentimentdata.json:     16000<br />
summarizedataset.json:     4936<br />
swag.json:     93552<br />
winogrande.json:     40398<br />


### promptCreators
Includes code used to create prompts. It generates sentences which is used to create more data. There are thousands of ways to say that you want a positive movie review, which means that we can use the same data more times if we connect it to different ways of calling on that data. 

[Google colab link for Categorized Prompt Generation](https://colab.research.google.com/drive/1sLwwcZw05anp7RrGVUiQDRdzn-z27r78?usp=sharing)
