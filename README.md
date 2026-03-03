🧠 AI & Machine Learning Project Portfolio

This repository contains three progressively advanced Machine Learning and NLP projects:

Beginner Level – Boston House Price Prediction

Intermediate Level – Car Selling Price Prediction

Advanced Level – Language Model Deployment & Analysis

The projects are designed following the AI & Data Science roadmap:
🔗 https://roadmap.sh/ai-data-scientist

📘 1️⃣ Beginner Level – Boston House Price Prediction
📌 Problem Statement

The objective of this project is to build a regression model to predict house prices in Boston using features such as:

Number of rooms

Crime rate

Property tax rate

Distance to employment centers

And other socio-economic factors

The goal is to design a complete ML pipeline including:

Data preprocessing

Feature engineering

Model training

Evaluation

📂 Dataset

https://drive.google.com/drive/folders/1ENkWLF2q9shwiET9z0CMckA_0lmCiVpU

Features include:

CRIM – Crime rate per capita

RM – Average number of rooms

TAX – Property tax rate

LSTAT – % lower status population

MEDV – Median house value (Target variable)

⚙️ Project Workflow
1️⃣ Data Preprocessing

Handling missing values

Feature scaling (StandardScaler)

Train-test split (80-20)

2️⃣ Model Selection

Implemented:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

3️⃣ Model Evaluation

Evaluation metrics used:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score

4️⃣ Best Model Selection

The model with the highest R² and lowest error metrics was selected.

📊 Results

Random Forest achieved better generalization.

Linear Regression showed good interpretability.

Feature importance analysis revealed that:

Number of rooms (RM)

% Lower status population (LSTAT)
strongly affect house prices.

🎯 Key Learning Outcomes

Understanding regression problems

Model comparison techniques

Feature importance analysis

Building end-to-end ML pipeline

🚗 2️⃣ Intermediate Level – Car Selling Price Prediction
📌 Problem Statement

Build a Machine Learning system to predict the selling price of used cars based on:

Fuel Type

Years of Service

Showroom Price

Number of Previous Owners

Kilometers Driven

Seller Type (Dealer/Individual)

Transmission Type (Manual/Automatic)

📂 Dataset

https://drive.google.com/file/d/1yFuNVPXM5CH6g0TthYKcTGrZCCJo6n8Z/view?us%20p=drive_link

Target Variable:

Selling_Price

⚙️ Project Workflow
1️⃣ Data Cleaning & Preprocessing

Encoding categorical features (One-Hot Encoding)

Feature engineering:

Car_Age = Current_Year – Year

Handling skewness

Scaling numerical features

2️⃣ Model Training

Models implemented:

Linear Regression

Ridge & Lasso Regression

Random Forest Regressor

Gradient Boosting Regressor

3️⃣ Hyperparameter Tuning

GridSearchCV

Cross-validation

4️⃣ Model Evaluation

Metrics used:

MAE

RMSE

R² Score

📊 Results & Analysis

Ensemble models outperformed linear models.

Car Age and Showroom Price are strong predictors.

Dealer cars tend to have higher selling prices.

Automatic transmission cars show slightly higher resale value.

🚀 Deployment

The trained model can be deployed using:

Flask API

Streamlit Web App

FastAPI

The system provides an estimated selling price based on user inputs.

🎯 Key Learning Outcomes

Handling categorical data

Feature engineering

Regularization techniques

Hyperparameter tuning

Model deployment basics

🤖 3️⃣ Advanced Level – Language Model Deployment & Analysis
📌 Problem Statement

In this project, we explore and deploy a Language Model (LM) to analyze its:

Context understanding

Text generation capabilities

Adaptability to different domains

Performance characteristics

🧠 Selected Language Model

For this project, we selected:

BERT (Bidirectional Encoder Representations from Transformers)
(For contextual understanding & classification tasks)

OR

GPT-based Model (For text generation tasks)

📓 Implementation (Jupyter Notebook)

The notebook includes:

Model loading using HuggingFace Transformers

Tokenization process

Attention mechanism visualization

Text generation experiments

Fine-tuning (if applicable)

🔍 Exploration & Analysis
Tested Capabilities:

Contextual understanding

Sentence completion

Domain adaptability

Sentiment classification

Question answering

🧪 Research Questions

How well does the LM understand long-range dependencies?

Does the model generate coherent text for ambiguous prompts?

How does it behave with domain-specific inputs?

What biases are observable in generated text?

How does temperature/top-k sampling affect creativity?

📊 Visualization

Used:

Attention heatmaps

Probability distributions of token predictions

Loss curves during fine-tuning

Comparison charts with baseline models

⚖️ Ethical Considerations

Bias in training data

Hallucination in text generation

Responsible AI deployment

Fairness and transparency

📈 Results

Strong contextual understanding with BERT

GPT-based model demonstrated high fluency in text generation

Limitations observed in domain-specific knowledge without fine-tuning

Attention visualization provided interpretability insights

🎯 Conclusion

This project demonstrates:

Practical implementation of modern NLP models

In-depth LM behavior analysis

Visualization-driven interpretation

Alignment with evolving AI research trends

The findings highlight both the immense potential and the critical limitations of large language models in real-world applications.

🛠️ Technologies Used

Python

NumPy

Pandas

Scikit-learn

Matplotlib & Seaborn

HuggingFace Transformers

PyTorch / TensorFlow

Jupyter Notebook

📚 Learning Roadmap Reference

This project aligns with the AI/Data Scientist roadmap:

🔗 https://roadmap.sh/ai-data-scientist

🏁 Final Thoughts

This repository represents a complete AI learning journey:

📘 Beginner → Regression fundamentals

🚗 Intermediate → Feature engineering & deployment

🤖 Advanced → Transformer models & research-level NLP

By completing these projects, you demonstrate:

Strong ML fundamentals

Practical modeling skills

NLP expertise

Research & analytical thinking ability