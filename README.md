# Crop Yield Prediction Project 🌾📊

This repository contains a comprehensive Crop Yield Prediction System developed as part of a summative assignment. The project combines machine learning model development, API implementation, and mobile app integration to predict crop yields based on environmental and agricultural factors.

## Project Overview

The system consists of three main components:

1. **Machine Learning Model Development** - Linear Regression model trained on crop yield data
2. **API Development** - FastAPI backend for serving predictions
3. **Mobile Application** - Flutter app for user interaction

## Key Features

- Accurate crop yield prediction based on environmental factors
- Cross-platform mobile application
- Scalable API backend
- Comprehensive model comparison and evaluation
- User-friendly interfaces (API docs & mobile UI)

## Project Components

### 1. Machine Learning Model Development

**Description**:  
Developed and optimized machine learning models to predict crop yield using the [Crop Yield Prediction Dataset from Kaggle](https://www.kaggle.com/datasets/mrigaankjaswal/crop-yield-prediction-dataset/data).

**Key Activities**:
- Compared the performance of Linear Regression, Decision Tree, and Random Forest algorithms
- Feature engineering and data preprocessing
- Model optimization and evaluation
- Model serialization for production use

**Notebook**:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yDNFH5MmWhlc2YvNihdaEhGiwBWxBeIn?authuser=9#scrollTo=vxrvsmBYBzhd)



### 2. FastAPI Development

**Description**:  
Developed a production-ready API for making predictions using the trained model.

**Features**:
- Input validation with Pydantic
- Comprehensive API documentation
- Error handling and logging
- Deployed on Render cloud platform

**API Documentation**:  
[![API Docs](https://img.shields.io/badge/API_Docs-Swagger_UI-green)](https://fastapi-rm5x.onrender.com/docs)


### 3. Mobile App Development

**Description**:  
Developed a cross-platform mobile application that connects to the prediction API.

**Features**:
- Intuitive user interface
- Real-time predictions
- Responsive design
- Error handling and loading states

**Design**:  
[![Figma Design](https://img.shields.io/badge/Design-Figma-orange)](https://www.figma.com/design/MxoAOSFXKB7azCbUcSEhEW/Wildlife-Activity-Predictor?node-id=0-1&t=qZiQdCtCC99BJ7tF-1)

**Demo Video**:  
[![YouTube Demo] https://youtu.be/7mtrlJgmOos?si=4BWwI8CrEX5GK10q


## Dataset

The [Crop Yield Prediction Dataset](https://www.kaggle.com/datasets/mrigaankjaswal/crop-yield-prediction-dataset/data) contains:

- **Area** (Country)
- **Item** (Crop)
- **Year**
- **hg/ha_yield**: Target variable (yield in hectograms per hectare)
- **average_rain_fall_mm_per_year**
- **pesticides_tonnes**
- **avg_temp**

## Technology Stack

**Machine Learning**:
- Python
- scikit-learn
- pandas
- numpy
- MinMaxScaler
- pickle

**Backend**:
- FastAPI
- Pydantic
- Render (deployment)
- Swagger UI

**Mobile App**:
- Flutter
- Dart

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MarialRK/linear_regression_model.git
   cd linear_regression_model
