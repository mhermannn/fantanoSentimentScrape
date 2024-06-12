import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import text2emotion as te
import pandas as pd
import matplotlib.pyplot as plt
import json
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

# Inicjalizacja SentimentIntensityAnalyzer i pobranie zasobów NLTK
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
sid = SentimentIntensityAnalyzer()

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

# Funkcja do analizy sentymentu i emocji dla jednego komentarza
def analyze_comment(comment):
    sentiment_scores = sid.polarity_scores(comment)
    emotions = te.get_emotion(comment)
    return sentiment_scores, emotions

def emotionBars(album_name):
    album_dir = os.path.join("albums", album_name)
    comments_file = os.path.join(album_dir, "comments.csv")

    # Wczytywanie komentarzy z pliku CSV
    df = pd.read_csv(comments_file)

    # Czyszczenie komentarzy
    df['cleaned_text'] = df['text'].apply(clean_comment)

    # Przeprowadzanie analizy sentymentu i emocji dla każdego komentarza
    results = []
    for index, row in df.iterrows():
        original_comment = row['text']
        cleaned_comment = row['cleaned_text']
        sentiment_scores, emotions = analyze_comment(cleaned_comment)
        results.append({
            'original_comment': original_comment,
            'cleaned_comment': cleaned_comment,
            'sentiment': sentiment_scores,
            'emotions': emotions
        })

    # Zapisywanie wyników do pliku JSON
    with open(os.path.join(album_dir, 'comments_analysis.json'), 'w', encoding='utf-8') as outfile:
        json.dump(results, outfile, indent=4, ensure_ascii=False)

    # Przygotowanie danych do wykresów
    aggregate_sentiment = {
        'neg': 0,
        'neu': 0,
        'pos': 0,
        'compound': 0
    }
    emotion_totals = {
        'Happy': 0,
        'Angry': 0,
        'Surprise': 0,
        'Sad': 0,
        'Fear': 0
    }

    for result in results:
        aggregate_sentiment['neg'] += result['sentiment']['neg']
        aggregate_sentiment['neu'] += result['sentiment']['neu']
        aggregate_sentiment['pos'] += result['sentiment']['pos']
        aggregate_sentiment['compound'] += result['sentiment']['compound']
        
        for emotion, score in result['emotions'].items():
            emotion_totals[emotion] += score

    num_comments = len(results)
    for key in aggregate_sentiment:
        aggregate_sentiment[key] /= num_comments

    for key in emotion_totals:
        emotion_totals[key] /= num_comments

    # Tworzenie wykresów słupkowych
    fig, axs = plt.subplots(2, figsize=(10, 10))

    axs[0].bar(aggregate_sentiment.keys(), aggregate_sentiment.values(), color=['red', 'gray', 'green', 'blue'])
    axs[0].set_title('Średnie wyniki sentymentu'.format(album_name))
    axs[0].set_xlabel('Typ sentymentu')
    axs[0].set_ylabel('Średnia wartość')

    axs[1].bar(emotion_totals.keys(), emotion_totals.values(), color=['yellow', 'red', 'purple', 'blue', 'orange'])
    axs[1].set_title('Średnie wyniki emocji'.format(album_name))
    axs[1].set_xlabel('Emocje')
    axs[1].set_ylabel('Średnia wartość')

    plt.tight_layout()
    plt.savefig(os.path.join(album_dir, album_name+'_Emotions.png'))
