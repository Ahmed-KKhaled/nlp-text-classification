# 📰 20 Newsgroups Text Classification

This project compares Traditional Machine Learning, LSTM, and BERT for multi-class text classification using the 20 Newsgroups dataset. The goal is to classify text documents into 20 different categories and evaluate which approach performs best for NLP classification tasks.

---

## 📌 Problem Statement

Text classification in real-world data is challenging due to the diversity of topics and overlap between categories. The 20 Newsgroups dataset contains documents from different domains such as technology, science, politics, religion, and sports.

The main challenge is that many topics share similar vocabulary, making it difficult for models to distinguish between classes.

For example:
- "The system crashed after update" → could belong to **Windows OS / Hardware**
- "The team won the final match" → could belong to **sports categories**

This project evaluates how different models handle such ambiguity.

---

## 📂 Dataset

- **Dataset:** 20 Newsgroups
- **Number of Classes:** 20
- **Categories:** Technology, Science, Politics, Religion, Sports, Hardware, and more
- **Type:** Text documents
- **Link** https://github.com/Ahmed-KKhaled/nlp-text-classification/tree/main/Text_Classification_Project/data

---
## 🏷️ Class Labels Explanation

Below is a simple explanation for each category in the dataset:

### 🖥️ Technology & Hardware
- **comp.graphics** → Topics related to computer graphics, image rendering, and visualization.
- **comp.os.ms-windows.misc** → Discussions about Windows operating system issues and features.
- **comp.sys.ibm.pc.hardware** → IBM PC hardware components and troubleshooting.
- **comp.sys.mac.hardware** → Apple Mac hardware discussions and issues.
- **comp.windows.x** → X Window System and Unix-based graphical interface systems.

---

### 🚗 Automotive & Sports
- **rec.autos** → Cars, engines, maintenance, and automotive discussions.
- **rec.motorcycles** → Motorcycle models, riding experiences, and maintenance.
- **rec.sport.baseball** → Baseball games, players, and statistics.
- **rec.sport.hockey** → Hockey matches, teams, and sports analysis.

---

### 🔬 Science & Technology
- **sci.crypt** → Cryptography, encryption methods, and security systems.
- **sci.electronics** → Electronic circuits, devices, and engineering topics.
- **sci.med** → Medical science, health discussions, and research.
- **sci.space** → Space exploration, satellites, and astronomy.

---

### 🏛️ Politics & Religion
- **talk.politics.guns** → Gun control and firearm regulations.
- **talk.politics.mideast** → Political issues in the Middle East.
- **talk.politics.misc** → General political discussions.
- **talk.religion.misc** → Various religious discussions.
- **soc.religion.christian** → Christianity-related topics and discussions.

---

### 📦 Others
- **misc.forsale** → Items for sale, classifieds, and buying/selling posts.
- **alt.atheism** → Discussions about atheism and philosophical arguments about religion.

---
## 🧪 Approach

Three different models were implemented and compared:

### 1. Traditional Machine Learning
Uses TF-IDF features with classical classifiers like Logistic Regression and SVM.  

### 2. LSTM
A deep learning model that processes text sequentially and captures word dependencies.  

### 3. BERT
A transformer-based model that understands context bidirectionally using pre-training on large text corpora.  
It achieves the best performance in this project due to its ability to capture deep contextual relationships between words and leverage transfer learning.

---

## 📊 Results

### Traditional Machine Learning
| Model | F1 Score |
|-------|----------|
| Naive Bayes | 82% |
| Logistic Regression | 83%|
| Linear SVC | 85.3% |

### LSTM
| Model | F1 Score |
|-------|----------|
| LSTM | 76% |

### BERT
| Model | F1 Score |
|-------|----------|
| BERT | **85.7%** |

---

## 🔍 Model Comparison Example

| Text | SVM | LSTM | BERT |
|------|----|------|------|
| System crashes after update | Windows OS | Hardware | Windows OS |
| NASA launched a new satellite | Space | Space | Space |
| The team won the championship | Hockey | Hockey/Baseball | Hockey |
| Selling used laptop cheap | For Sale | For Sale | For Sale |<img width="1535" height="1389" alt="WhatsApp Image 2026-04-21 at 15 20 06" src="https://github.com/user-attachments/assets/82f5d0e2-7bb2-4606-bb15-5161ec30932b" />

| Debate about government laws | Politics | Politics | Politics |

---

## 📉 Confusion Matrix

**Bert** 
<img width="1535" height="1389" alt="WhatsApp Image 2026-04-21 at 15 20 06" src="https://github.com/user-attachments/assets/e7710c15-0965-4760-8bbe-9037121682f1" />

**SVM**
<img width="1535" height="1389" alt="WhatsApp Image 2026-04-21 at 16 33 07" src="https://github.com/user-attachments/assets/b72b6a90-44f0-441d-9df6-e9d46ad78f6a" />


### Key Observations:
- talk.politics.misc sometimes misclassified as talk.politics.gun
- talk.religion.misc sometimes misclassified as alt.atheism
- SVM shows better separation between similar emotions

---

## 🔍 Why SVM performed so well?

In this project, Linear SVM achieved strong performance (85.3%), sometimes competing with transformer-based models.

This can be explained by:

- **High-dimensional TF-IDF features:** SVM performs extremely well with sparse, high-dimensional data like TF-IDF representations.
- **Clear decision boundaries:** SVM is effective at finding optimal separating hyperplanes between classes.
- **Small-to-medium dataset size:** Traditional ML models often outperform deep learning when data is not extremely large.
- **Less overfitting:** Unlike deep models, SVM generalizes well on structured text features.
- **Strong baseline for text classification:** SVM has historically been one of the best classical algorithms for NLP tasks.

---
## 🔍 Why BERT Performs so well?

- Pre-trained on large-scale text data
- Understands bidirectional context
- Captures semantic meaning better than ML and LSTM
- Handles ambiguous sentences more effectively

---

## 🛠️ Models Used

- Naive Bayes
- Logistic Regression
- Linear SVC
- LSTM (PyTorch)
- BERT (HuggingFace Transformers)

---

## ⚙️ Technologies Used

- Python
- Scikit-learn
- PyTorch
- TensorFlow
- HuggingFace Transformers
- Pandas / NumPy
- Streamlit (for deployment)
