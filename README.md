This is a cnn-based deep neural network classifier project on various datasets. I use dropout trick and adaptive learning rate to build the model. The present version supports 2 datasets cifar-10 and svhn.

Cifar-10 data is downloaded from http://www.cs.toronto.edu/~kriz/cifar.html and should be saved in the folder ./cifar-10/. Svhn data is downloaded from http://ufldl.stanford.edu/housenumbers/, I use the format2 without extra training instances. For the svhn file is too large to be uploaded on the Github, you should download the file `` train_32x32.mat`` and ``test_32x32.mat`` yourself and save them in the folder ./svhn/. 

For each dataset, I use a parser to parse them in order to match the interface of cnn. You should run ``python parser.py`` in each dataset's folder and make sure it generates files called ``train_data``,``validate_data`` and ``test_data``.

Simply run the command ``python main.py <dataset>`` like ``python main.py cifar-10`` or ``python main.py svhn`` to train and test the model.

Best precision rate on cifar-10 test batch: 74.0%. Best precision rate on svhm test batch: 91.2%.

