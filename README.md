# datacollection
This GitHub is created by the participants at AI Sweden Young Talent Program and includes datasets and code used to create datasets. 

## Folder and Files

### Datasets
This folder includes json-files with data. The data should include a label and a text. Please note that the roles are reverse. The label includes a text string (e.g. a movie review) and the text string describes the label (e.g. either 'positive' or 'negative' if it is a movie review). The reason behind this is that the text string in our case is the dependent variable and therefore the label. 

[Google colab link for a dataset containing yelp-reviews](https://drive.google.com/file/d/1QfiY0svqTVS2XIK5jyDA2FNweLaSffPK/view?usp=sharing)

### promptCreators
Includes code used to create prompts. It generates sentences which is used to create more data. There are thousands of ways to say that you want a positive movie review, which means that we can use the same data more times if we connect it to different ways of calling on that data. 

[Google colab link for Categorized Prompt Generation](https://colab.research.google.com/drive/1sLwwcZw05anp7RrGVUiQDRdzn-z27r78?usp=sharing)
