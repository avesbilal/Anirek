
# Table of Contents

 - [Introduction](#introduction)
 - [Getting Started](#getting-started)
 - [Features](#features)
 - [How it works](#how-it-works)

# Introduction

**Anime** is a form of hand-drawn or computer-generated animation originating from Japan. In terms of genres, there are more than **34,211+** anime listed on [myanimelist.net](https://myanimelist.net/anime.php). The problem is the difficulty in finding anime that aligns with individual viewer preferences due to the vast number of options available.

![CleanShot 2024-10-11 at 11 28 39@2x](https://github.com/user-attachments/assets/4486e727-2c4b-43df-add7-2cd2b4781311)

This web app is designed for anime viewers who:

* Feel overwhelmed by the vast amount of anime available
* Want to avoid wasting time on anime they won't enjoy
* Appreciate a streamlined and user-friendly experience

# Getting Started

To run this app on your local machine:

1. Clone this repository:
    ```sh
    git clone https://github.com/xavesx/Anirek.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Anirek
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the Python file to generate the pickle file:
    ```sh
    python main.py
    ```
5. Run the application:
    ```sh
    streamlit run app.py
    ```

# Features

<p style="text-align:left; font-size:15px;">RECOMMENDATION</p>

![CleanShot 2024-10-11 at 12 23 58](https://github.com/user-attachments/assets/3b96849f-49fe-499a-aa5a-c5001c1f8e06)

<p style="text-align:left; font-size:15px;">CONTACT FORM</p>

![CleanShot 2024-10-11 at 12 40 45](https://github.com/user-attachments/assets/4fbabdcc-c7cc-4fa1-8196-13045a668b33)

# How it works

* The dataset has been obtained from Kaggle, then cleaned and relevant columns are selected: `title`, `genre`, `overview`, and `img_url`. A new column `tags` is created by combining the `overview` and `genre` columns.

* The `CountVectorizer` from `scikit-learn` is used to convert the `tags` column into a matrix of token counts. This matrix is then used to compute the cosine similarity between different anime.

* The cosine similarity matrix is calculated, which measures the cosine of the angle between two vectors in a multi-dimensional space. This helps in finding how similar two anime are based on their `tags`.

* The `recommend` function takes an anime name as input and finds its index in the dataset. It then sorts the anime based on their similarity scores and returns the top 5 most similar anime along with their images.

* When a user selects an anime, the `recommend` function is called. The recommended anime names and their images are displayed in a grid format.