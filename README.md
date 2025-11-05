
# SMS-Spam-Detection

## SMS Spam Detection Model

### Task Objectives

The goal of this project is to build a machine learning model capable of classifying SMS messages as either "Spam" or "Not Spam" (Ham). The model is built using a **Multinomial Naive Bayes** classifier, trained on a balanced dataset. The project includes a **Streamlit app** that allows users to input SMS messages and get real-time predictions.

### Key Objectives:
- **Preprocess and clean** the SMS text data.
- **Train a spam classification model** using **TF-IDF vectorization** and **Multinomial Naive Bayes**.
- **Build an interactive Streamlit application** for real-time SMS spam detection.
- **Evaluate the model** using common metrics such as accuracy, precision, recall, and F1-score.

---

## Steps to Run the Project

### 1. Clone the Repository
Start by cloning this repository to your local machine:

```bash
git clone https://github.com/Anushkajoshii/SMS-Spam-Detection.git
cd sms-spam-detection
```

### 2. Install Dependencies

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
```

Install the required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install the necessary libraries for the project.

### 3. Train the Model

To train the model and generate the necessary files (`spam_classifier.pkl` and `vectorizer.pkl`), run the following command:

```bash
python train_model.py
```

This will:
- Load and preprocess the dataset (`spam.csv`).
- Train a **Multinomial Naive Bayes** model using **TF-IDF** for text vectorization.
- Save the trained model and vectorizer as `spam_classifier.pkl` and `vectorizer.pkl`.

### 4. Run the Streamlit App

Once the model is trained, you can run the Streamlit app to interact with the model and classify SMS messages as spam or not.

Run the following command:

```bash
streamlit run app.py
```

This will launch the app in your web browser. Enter a message into the text box, and the app will predict whether it is spam or not.

---

## File Structure

- **train_model.py**: Script for training the spam detection model.
- **app.py**: Streamlit app for real-time SMS spam detection.
- **spam_classifier.pkl**: The trained model file.
- **vectorizer.pkl**: The TF-IDF vectorizer used for transforming the text.
- **spam.csv**: The dataset used for training the model.
- **requirements.txt**: Python libraries required to run the project.
- **README.md**: Documentation for the project.

---


The Streamlit app allows users to interact with the model easily without requiring deep technical knowledge.

---

## Evaluation Criteria

### Functionality
- The model correctly classifies SMS messages as **Spam** or **Not Spam**.
- The Streamlit app is fully functional and intuitive.


### Innovation & Creativity
- The app includes a simple yet effective user interface.
- The model is trained using a **balanced dataset** and optimized for text classification tasks.
- The app's design provides immediate feedback to the user, displaying whether the message is spam or not.

### Documentation
- Clear instructions on how to set up and run the project.
- A description of the task and objectives.
- Information on dependencies and project structure.

---

## Example Output

When a user inputs an SMS message, the model will predict whether the message is spam or not:

### Example Input:
"Congratulations, you've won a free iPhone!"
- **Output**: Spam

### Example Input:
"Hey, are we still meeting tomorrow?"
- **Output**: Not Spam

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
