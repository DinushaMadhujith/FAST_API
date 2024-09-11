# House Price Prediction API with FastAPI
This repository contains a FastAPI-based web API for predicting house prices using a pre-trained machine learning model. The application takes house features as input and returns a predicted price. It is deployed on Render.

**Project Overview** This project is a machine learning application built with FastAPI that predicts house prices based on various features, including area, bedrooms, bathrooms, and other attributes. The model was trained on a dataset of house features and prices, and the API allows users to interact with the model via POST requests.

**Live Demo**

The API is live and available at: https://fast-api-3plu.onrender.com

Medium article titled **“How to Deploy a FastAPI Machine Learning Application in Render”**: https://medium.com/@shdinu888/how-to-deploy-a-fastapi-machine-learning-application-in-render-b1a8cea5b3fa 

 **Make a Prediction**
 
Send a POST request to /predict with house features in the following format

{

  "area": 3500,
  
  "bedrooms": 4,
  
  "bathrooms": 3,
  
  "stories": 2,
  
  "mainroad": 1,
  
  "guestroom": 0,
  
  "basement": 1,
  
  "hotwaterheating": 0,
  
  "airconditioning": 1,
  
  "parking": 2,
  
  "prefarea": 1,
  
  "furnishingstatus": 1
  
}

**You will receive a response like this**

{

  "predicted_price": "$450,000.00"
  
}
