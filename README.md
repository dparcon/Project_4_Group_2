# Spotify & YouTube Song Analysis Project

## Project Overview

This project focuses on analyzing the relationship between various musical features of Spotify tracks, aiming to uncover patterns and insights into what makes a song popular in terms of streams. By leveraging the many features used to characterize each song, we aim to provide actionable insights into song popularity.

The project involves data preprocessing, feature engineering, and machine learning models (e.g., logistic regression with recursive feature elimination), alongside outlier detection, multicollinearity tests, and performance evaluations.

---

## Table of Contents

- [Spotify \& YouTube Song Analysis Project](#spotify--youtube-song-analysis-project)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Dataset](#dataset)
    - [Spotify Data](#spotify-data)
    - [YouTube Data](#youtube-data)
    - [Engineered Features](#engineered-features)
  - [Project Structure](#project-structure)
  - [Installation and Setup](#installation-and-setup)
    - [Requirements](#requirements)
  - [Key Analyses](#key-analyses)
    - [Logistic Regression with Recursive Feature Elimination (RFE)](#logistic-regression-with-recursive-feature-elimination-rfe)
    - [Multicollinearity Testing](#multicollinearity-testing)
    - [Outlier Removal](#outlier-removal)
  - [Results](#results)
  - [Future Enhancements](#future-enhancements)
  - [Conclusion](#conclusion)
  - [Author](#author)
  - [License](#license)

---

## Dataset

The dataset includes the following columns:

### Spotify Data
- **Track**: Name of the song
- **Artist**: Artist name
- **Album**: Album name
- **Danceability**: Measure of how suitable a track is for dancing (0 to 1)
- **Energy**: Intensity and activity measure (0 to 1)
- **Loudness**: The average decibel level of the track
- **Speechiness**: Presence of spoken words (0 to 1)
- **Acousticness**: Confidence measure for acoustic sounds (0 to 1)
- **Liveness**: Probability the track was recorded live (0 to 1)
- **Instrumentalness**: Likelihood the track contains no vocals
- **Tempo**: Beats per minute (BPM)
- **Valence**: Musical positiveness conveyed (0 to 1)
- **Streams**: Number of streams on Spotify

### YouTube Data
- **Title**: Title of the YouTube video
- **Channel**: YouTube channel
- **Views**: Number of views
- **Likes**: Number of likes
- **Comments**: Number of comments
- **Description**: Video description

### Engineered Features
- **Engagement**: Sum of `streams` and `views`
- **YouTube Popularity**: Ratio of `likes` to `views`

---

## Project Structure

1. **Data Preprocessing**: Cleaning and merging Spotify and YouTube datasets, handling missing values, and transforming features for further analysis.
2. **Feature Engineering**: New features like `engagement` and `youtube_popularity` were introduced. Numeric features were scaled for machine learning models.
3. **Outlier Detection**: Boxplots were used to detect and remove outliers for key features.
4. **Multicollinearity Testing**: Conducted Variance Inflation Factor (VIF) analysis to check for multicollinearity among features.
5. **Machine Learning Models**:
   - Logistic Regression with Recursive Feature Elimination (RFE) for feature selection.
   - Performance metrics: accuracy, precision, recall, classification report.

---

## Installation and Setup

### Requirements

Ensure you have the following Python packages installed:

pip install pandas numpy scikit-learn matplotlib seaborn statsmodels

Running the Notebook
1. Clone the repository:
    git clone <repository-url>
    cd spotify_youtube_analysis

2. Install required dependencies:
    pip install -r requirements.txt

3. Open the Jupyter notebook:
    jupyter notebook spotify_youtube_song_analysis.ipynb

4. Run the cells sequentially to reproduce the data processing, feature engineering, and machine learning models.

## Key Analyses

### Logistic Regression with Recursive Feature Elimination (RFE)

RFE was applied to logistic regression to select the most influential features in predicting whether a song is above or below the stream threshold. The models were run with varying quantile thresholds and custom classification thresholds.

- **Top Features Identified**: `loudness`, `valence`, `tempo`, `danceability`
- **Thresholds**: We applied a custom threshold to evaluate model performance.

### Multicollinearity Testing

Variance Inflation Factor (VIF) analysis was performed to check for multicollinearity among the independent variables. This helped refine the features to be used in the logistic regression models.

### Outlier Removal

Outliers were identified and removed using boxplot visualizations to reduce the impact of skewed data on model performance. Removing outliers improved model stability and accuracy.

---

## Results

- **Accuracy**: The logistic regression model, after feature selection and tuning, achieved an accuracy of **X%** depending on the quantile thresholds used.
- **Feature Importance**: The features `loudness`, `energy`, and `danceability` were found to have a strong influence on the popularity of a song across platforms.

---

## Future Enhancements

- **Experimenting with other models**: Additional machine learning models like decision trees, random forests, and neural networks could be explored for further insights.
- **Additional feature engineering**: Interaction terms between features (e.g., `energy` and `valence`) could reveal hidden patterns.
- **Time-Series Analysis**: Adding time as a variable to analyze song popularity trends over time could provide more granular insights.

---

## Conclusion

This project provides valuable insights into how various audio attributes impact song popularity across Spotify. By leveraging feature engineering, multicollinearity testing, and logistic regression, we developed models capable of predicting song popularity with reasonable accuracy. These findings can benefit artists, producers, and marketers in optimizing content for better engagement.

---

## Author

Developed by . For any questions or collaboration opportunities, feel free to reach out.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.