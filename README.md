# 🎬 Movie Review Sentiment Analysis

A Machine Learning web application that predicts whether a movie review expresses **positive** or **negative** sentiment using a **Simple RNN** trained on the IMDB Movie Reviews dataset. The application is built with **TensorFlow/Keras** and deployed using **Streamlit**.

---

## ✨ Features

- 🎭 Predicts movie review sentiment
- 🤖 Deep Learning model using Simple RNN
- 📚 Trained on the IMDB Movie Reviews dataset
- ⚡ Fast real-time predictions
- 🌐 Interactive Streamlit web interface
- 😊 Displays prediction confidence score

---

## 🛠️ Tech Stack

### Machine Learning
- TensorFlow
- Keras
- NumPy
- Scikit-learn

### Web Framework
- Streamlit

### Language
- Python

---

## 📂 Project Structure

```
movie_review/
│
├── main.py                    # Streamlit application
├── simple_rnn_imdb.h5         # Trained RNN model
├── implemetation.ipynb        # Model training notebook
├── prediction.ipynb           # Prediction notebook
├── requirements.txt
├── runtime.txt
├── LICENSE
└── README.md
```

---

## 🧠 Model Architecture

- Embedding Layer
- Simple RNN Layer
- Dense Output Layer
- Sigmoid Activation

The model is trained for **binary sentiment classification** on the IMDB dataset.

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/HansiG3/movie_review.git
cd movie_review
```

---

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 📖 How It Works

1. User enters a movie review.
2. The review is converted to lowercase and tokenized.
3. Words are mapped to their corresponding IMDB indices.
4. The sequence is padded to a fixed length.
5. The trained Simple RNN predicts the sentiment.
6. The application displays:
   - Predicted sentiment
   - Prediction confidence score

---

## 💡 Example

### Input

```
The movie had an amazing storyline and brilliant acting.
```

### Output

```
Sentiment: Positive 😊

Prediction Score: 0.9821
```

---

### Another Example

### Input

```
The movie was boring and a complete waste of time.
```

### Output

```
Sentiment: Negative 😞

Prediction Score: 0.0415
```

---

## 📊 Dataset

The model is trained using the **IMDB Movie Reviews Dataset**, which contains **50,000** labeled movie reviews equally divided into positive and negative sentiments.

---

## 📸 Screenshots

<img width="953" height="511" alt="image" src="https://github.com/user-attachments/assets/72057f00-477f-43d3-97d7-dae18b5b5058" />
<img width="955" height="512" alt="image" src="https://github.com/user-attachments/assets/a19d708d-8c63-4fee-9fc7-35be8fb172bf" />

## 🔮 Future Enhancements

- Support multi-class sentiment prediction
- Display confidence visualization
- Attention-based RNN/LSTM model
- Compare predictions across multiple models
- Deploy using Docker
- User review history
- Explainable AI (SHAP/LIME)

---

## 📦 Requirements

- Python 3.10+
- TensorFlow
- Streamlit
- NumPy
- Pandas
- Scikit-learn

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Hansi Gupta**

- GitHub: https://github.com/HansiG3
- LinkedIn: *(Add your LinkedIn profile here)*
