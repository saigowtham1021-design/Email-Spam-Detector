# 📧 Email Spam Detection System

A Machine Learning-based Email/SMS Spam Detection System built using Python and Scikit-learn.
This project classifies messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing techniques.

---

## 🚀 Project Overview

This project focuses on building a text classification model that can automatically detect spam messages.
It uses **TF-IDF vectorization** to convert text into numerical features and applies the **Naive Bayes algorithm** for classification.

The model is trained on a real-world dataset and achieves high accuracy in identifying spam messages.

---

## 🎯 Features

* 📩 Classifies messages as **Spam** or **Not Spam**
* 🧠 Uses Machine Learning (Naive Bayes)
* 🔤 Text vectorization using **TF-IDF**
* ⚡ Fast and efficient predictions
* 💻 Simple command-line interface for testing
* 📊 Achieves ~96% accuracy

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Naive Bayes Algorithm

---

## 📂 Project Structure

```
Email-Spam-Detector/
│
├── spam_model.ipynb      # Model training and evaluation
├── predict.py            # Script for real-time predictions
├── spam_model.pkl        # Trained ML model
├── vectorizer.pkl        # TF-IDF vectorizer
├── README.md             # Project documentation
```

---

## ⚙️ How It Works

1. Load dataset (spam.csv)
2. Preprocess text data
3. Convert text → numerical features using TF-IDF
4. Train model using Naive Bayes
5. Save model and vectorizer
6. Use predict.py for real-time predictions

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```
git clone https://github.com/saigowtham1021-design/Email-Spam-Detector.git
cd Email-Spam-Detector
```

### Step 2: Run Prediction Script

```
python predict.py
```

### Step 3: Enter Message

```
Enter your message: You won a free lottery!
Prediction: Spam
```

---

## 📊 Model Performance

* Accuracy: **~96%**
* High precision for spam detection
* Evaluated using classification metrics (Precision, Recall, F1-score)

---

## 🧪 Example

| Input Message                      | Prediction |
| ---------------------------------- | ---------- |
| "Congratulations! You won a prize" | Spam       |
| "Let's meet tomorrow"              | Not Spam   |

---

## 📌 Future Improvements

* Build a web interface using Flask
* Improve recall for spam detection
* Deploy as a web application
* Add deep learning models

---

## 👨‍💻 Author

**G.Shanmuka Ramana Sai Gowtham**

* GitHub: https://github.com/saigowtham1021-design

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
