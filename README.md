# Zero Shot Learning 

### Method1 : Zero Short Learning with Word2Vector for class labels(label embedding)
Zero shot learning aims to solve a task to identify classes that are not seen by the model during training.
For example, let’s say you have seen a horse but never seen a zebra. If I tell you that a zebra looks like a horse but it has black and white stripes, you will probably immediately recognize a zebra when you see it.
This is what zero-shot learning aims to tackle.

<img src="https://www.programmersought.com/images/779/99f80acb97763b3b810b016933de6d73.png" width=600, height=400>

Data has been collected from this website https://visualgenome.org/ 20 classes in total where there are 15 classes selected for training and 5 classes selected as Zero-Shot classes

#### Train Classes:
arm, boy, bread, chicken, child, computer, ear, house, leg, sandwich, television, truck, vehicle, watch, woman
#### Zero-Shot Classes:
car, food, hand, man, neck

### Method2 : Embarrassingly Simple approach to Zero Shot learning(EZsl)


<img src="https://iq.opengenus.org/content/images/2020/01/Screenshot-from-2020-01-27-00-56-44.png">

Dataset has been collected from this website https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/zero-shot-learning/latent-embeddings-for-zero-shot-classification.

Different datasets with different length of attributes for each dataset 
+ SUN: Attributes 102,  Classes 717
+ CUB: Attributes 312,  Classes 200
+ AWA1: Attributes 85,  Classes 50 
+ AWA2: Attributes 85,  Classes 50
+ APY: Attributes 64,   Classes 32


### Instructions

Follow the below steps to run the code:
### Zsl with label embedding
+ Install all the necessary packages
+ Open the jupyter notebook located at 
https://github.com/kiran74-ds/zsl/blob/main/Zero_Shot_Learning.ipynb
+ Follow the steps in the note book

Follow the below steps to run the code:

## Eszl
+ Install all the necessary packages
+ Open the jupyter notebook located at 
https://github.com/kiran74-ds/zsl/blob/main/Embarssingly_Simple_ZSL.ipynb
+ Follow the steps in the note book
