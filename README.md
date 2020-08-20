![GitHub repo size](https://img.shields.io/github/repo-size/Uttam580/chatbot_using_pytorch?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/Uttam580/chatbot_using_pytorch?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/Uttam580/chatbot_using_pytorch?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/Uttam580/chatbot_using_pytorch?color=red&style=plastic)


### ChatBot implemented using Pytorch

A chatbot is an artificial intelligence (AI) software that can simulate a conversation (or a chat) with a user in natural language through messaging applications, websites, mobile apps or through the telephone.

#### quick demo

![demo.gif](https://github.com/Uttam580/chatbot_using_pytorch/blob/master/demo.gif)

#### Aspects 

Simple chatbot implementation with PyTorch.

* The implementation is straightforward with a Feed Forward Neural net with 2 hidden layers.

*  Customization for your own use case is  easy. Just modify intents.json with possible patterns and responses and re-run the training.

#### Nn visualization

![model.png](https://github.com/Uttam580/chatbot_using_pytorch/blob/master/model_chat.pth.png)


### Project directory tree 

```
chatbot_using_pytorch
├─ .gitignore
├─ chat.py
├─ demo.gif
├─ input
│  └─ intents.json
├─ LICENSE
├─ models
│  └─ model_chat.pth
├─ notebooks
│  └─ chatbot_notebook.ipynb
├─ README.md
├─ requirements.txt
└─ src
   ├─ model.py
   ├─ nltk_utils.py
   └─ train.py

```

#### Installation

##### Create an environment

Whatever you prefer (e.g. conda or venv)

```mkdir myproject
$ cd myproject
$ python3 -m venv venv```

Activate it : 

```venv\Scripts\activate```


#### Bug / Feature Request

If you find a bug, kindly open an issue <a href  ='https://github.com/Uttam580/chatbot_using_pytorch/issues/new'></a> by including your search query and the expected result.


