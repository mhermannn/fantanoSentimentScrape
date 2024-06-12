from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import nltk

def barGraphs(album_name):
    # Inicjalizacja SentimentIntensityAnalyzer i pobranie zasobów NLTK
    nltk.download('vader_lexicon')
    nltk.download('stopwords')
    nltk.download('punkt')
    
    # Funkcja do czyszczenia komentarzy
    def clean_comment(comment):
        # Usuwanie HTML
        comment = re.sub(r'<.*?>', '', comment)
        # Usuwanie linków
        comment = re.sub(r'http\S+|www\S+', '', comment)
        # Usuwanie specjalnych znaków i cyfr
        comment = re.sub(r'[^A-Za-z\s]', '', comment)
        # Usuwanie apostrofów i innych podobnych znaków
        comment = re.sub(r"[\']+", '', comment)
        # Przetworzenie na małe litery
        comment = comment.lower()
        # Tokenizacja
        tokens = word_tokenize(comment)
        # Usuwanie stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        # Łączenie tokenów w string
        cleaned_comment = ' '.join(filtered_tokens)
        return cleaned_comment

    def sentiment_scores(comment, polarity):
        # Tworzenie obiektu SentimentIntensityAnalyzer
        sentiment_object = SentimentIntensityAnalyzer()
        sentiment_dict = sentiment_object.polarity_scores(comment)
        polarity.append(sentiment_dict['compound'])
        return polarity

    polarity = []
    positive_comments = []
    negative_comments = []
    neutral_comments = []

    album_dir = os.path.join("albums", album_name)
    comments_file = os.path.join(album_dir, "comments.txt")
    
    with open(comments_file, 'r', encoding='utf-8') as f:
        comments = f.readlines()
    
    # print("Analysing Comments...")
    for index, items in enumerate(comments):
        cleaned_comment = clean_comment(items)
        polarity = sentiment_scores(cleaned_comment, polarity)

        if polarity[-1] > 0.05:
            positive_comments.append(items)
        elif polarity[-1] < -0.05:
            negative_comments.append(items)
        else:
            neutral_comments.append(items)

    avg_polarity = sum(polarity) / len(polarity)
    print("Average Polarity:", avg_polarity)
    if avg_polarity > 0.05:
        print(album_name+ " has got a Positive response")
    elif avg_polarity < -0.05:
        print(album_name+ " has got a Negative response")
    else:
        print(album_name+ " has got a Neutral response")

    positive_count = len(positive_comments)
    negative_count = len(negative_comments)
    neutral_count = len(neutral_comments)

    # labels and data for Bar chart
    labels = ['Positive', 'Negative', 'Neutral']
    comment_counts = [positive_count, negative_count, neutral_count]

    # Creating bar chart
    plt.bar(labels, comment_counts, color=['blue', 'red', 'grey'])
    plt.xlabel('Sentiment')
    plt.ylabel('Comment Count')
    plt.title('Sentiment Analysis of Comments for ' + album_name)
    plt.savefig(os.path.join(album_dir, album_name+'_PosNegNeu.png'))

    # Plotting pie chart
    plt.figure(figsize=(10, 6))
    plt.pie(comment_counts, labels=labels)
    plt.savefig(os.path.join(album_dir, album_name+'_Pie.png'))
