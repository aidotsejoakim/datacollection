# datacollection
This GitHub is created by the participants at AI Sweden Young Talent Program and includes datasets and code used to create datasets. 

## Files

### Datasets
Includes json-files with data. The data should include a label and a text. Please note that the roles are reverse. The label includes a text string (e.g. a movie review) and the text string is either 'positive' or 'negative'. The reason behind this is that the text string in our case is the dependent variable and therefore the label. 

### promptCreators
Code used to create prompts. It generates sentences which is used to create more data. There are thousands of ways to say that you want a positive movie review, which means that we can use the same data more times if we connect it to different ways of calling on that data. 
