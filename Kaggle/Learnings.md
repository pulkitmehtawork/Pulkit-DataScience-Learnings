I am no expert in Kaggle at least not in competitions . 
It needs lot of consistent effort to do well in its competitions but we can still learn a lot by going through top notebooks , past solutions of 
competitons . Here , I am going to list key ideas I get while going through the past solutions , EDA notebooks etc . 

1. Sometimes , you will get huge dataset say in csv or excel format , it wont be able to fit in the memory itself . 
In such cases , you may change the data format to feather format and read the feather file . 
Also , check max size of each column and downcast data type . It will help reduce memory footprint . 
You can write pandas dataframe to feather file using its **to_feather** . It can be load in memory using **read_feather** .
There is great notebook written by Grandmaster Rohan on the same topic .. Worth a read ..
https://www.kaggle.com/code/rohanrao/tutorial-on-reading-large-datasets/notebook

2. In Kaggle and in real world modelling , it is must that we do well on unseen data or our model generalizes well . We should not overfit on public 
leaderboard . We should have a good cross validation strategy and trust on that . 

3. Feature Enginerring ideas -  Say you have product code or similar feature. You may group based on product code and derive many aggregate features.

