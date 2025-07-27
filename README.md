# 🏠 House Price Predictor (Flask + ML)

A machine learning-powered web application built with **Flask** that predicts housing prices based on user-provided inputs. The model is trained using scikit-learn's `Linear Regression`, with full preprocessing via a pipeline.

---

## 📊 Model Overview

This app uses a machine learning pipeline trained on a housing dataset. The model was developed in the Jupyter notebook [`practice.ipynb`](practice.ipynb), and includes:

- Handling of missing values using `SimpleImputer`
- Encoding of the `Neighborhood` feature with `OneHotEncoder`
- Scaling of numeric features using `StandardScaler`
- Model training using `Linear Regression`

The trained pipeline was serialized with `pickle` and saved as `pipe.pkl`.

---

## 🖥 Features

- 📥 Accepts inputs like square footage, number of bedrooms, bathrooms, year built, and neighborhood
- 🧠 Predicts house prices using a scikit-learn model pipeline
- 🌐 Flask web interface for user interaction
- ✅ Validates inputs and handles errors gracefully

---

## 🧰 Tech Stack

- Python
- Flask
- Pandas, NumPy
- scikit-learn
- HTML/CSS (with Jinja2 templates)
- Pickle

---

