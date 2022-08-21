**Bias and variance trade off**

Bias is the wrong assumption we have while creating the model say data is non linear but we assumed it is linear .
It leads to underfitting the data .

Variance is the sensitivity of the model to the variations in the data . It leads to overfitting .
By increasing variance ( increasing complexity of the model )  , we decrease bias and vice-versa. So , it is a trade off .

**Active learning**

When human experts are requested by Model to label some data , it is called Active Learning . 
It has many strategies . One of them is that we train the model on labeled dataset and then we predict on unlabled dataset.
For records with confidence probability less then certain threshold , we give it to experts to label . 

**Role of activation function in Deep learning**
It is to bring non - linearlity.

