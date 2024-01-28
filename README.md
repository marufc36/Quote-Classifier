# Quote-Classifier


## Overview

This project is a quote classifier built using Flask and trained on a dataset scraped from Goodreads.com. The dataset includes 29,000 quotes along with their author names and associated tags. After extracting and preprocessing the data, we selected the top 1,000 most common tags and removed rows with empty tag lists.

The goal of this project is to allow users to input a quote and receive five relevant tags associated with that quote. The Flask web application provides a user-friendly interface for interacting with the quote classifier model.


## Getting Started


To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   https://github.com/marufc36/Quote-Classifier.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   
   ```bash
   python app.py
   ```

Visit https://quote-classifier.onrender.com/ in your web browser to access the application.


## Usage
Once the application is running, you can input a quote into the provided form. Click on the "Submit" button, and the system will output five relevant tags associated with the input quote.


## Dataset
The dataset used for training the quote classifier consists of 29,000 quotes, author names, and tags scraped from Goodreads.com. We narrowed down the tags to the top 1,000 most common and removed rows with empty tag lists for better model performance.

## Model

The quote classifier model is trained using distilroberta-base that maps quotes to relevant tags.Then it is converted into ONNX. The model is saved in the models directory.


## Demonstrating with pictures :


***HuggingFace Space***


![image](https://github.com/marufc36/Quote-Classifier/assets/151602012/daff2c1c-b17d-48bc-8c36-8ea78f46e68f)


https://huggingface.co/spaces/mmchowdhury/Quote_Classifier





***Flask App***

![image](https://github.com/marufc36/Quote-Classifier/assets/151602012/e4f3293b-06aa-4c06-b58b-4efa772cb987)




