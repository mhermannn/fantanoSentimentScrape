import os
import re
import torch
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# nltk.download('stopwords')
# nltk.download('punkt')

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def clean_comment(comment):
    comment = re.sub(r'<.*?>', '', comment)
    comment = re.sub(r'http\S+|www\S+', '', comment)
    comment = re.sub(r'[^A-Za-z\s]', '', comment)
    comment = re.sub(r"[\']+", '', comment)
    comment = comment.lower()
    tokens = word_tokenize(comment)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    cleaned_comment = ' '.join(filtered_tokens)
    return cleaned_comment

def sentiment_score(comment):
    tokens = tokenizer.encode(comment, return_tensors='pt', truncation=True, max_length=512)
    result = model(tokens)
    return int(torch.argmax(result.logits)) + 1  

def plot_sentiment_distribution(name):
    album_dir = os.path.join("albums", name)
    df_path = os.path.join(album_dir, "comments_with_sentiments.csv")
    
    if not os.path.exists(df_path):
        raise FileNotFoundError(f"No comments_with_sentiments.csv file found in {album_dir}. Please run bert(name) first.")
    
    df = pd.read_csv(df_path)
    average_sentiment = df['sentiment'].mean()
    
    plt.figure(figsize=(10, 6))
    df['sentiment'].value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Number of Comments')
    plt.title(f'Sentiment Distribution for {name} with mean {average_sentiment}')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    
    plot_path = os.path.join(album_dir, "sentiment_distribution.png")
    plt.savefig(plot_path)
    print(f"Sentiment distribution plot saved to {plot_path}")

def bert(name):
    neutral_words = [name,"melon","theneedledrop","fantano"]
    album_dir = os.path.join("albums", name)
    df_path = os.path.join(album_dir, "comments.csv")
    
    if not os.path.exists(df_path):
        raise FileNotFoundError(f"No comments.csv file found in {album_dir}")
    
    df = pd.read_csv(df_path)
    
    def preprocess_review(review, neutral_words):
        for word in neutral_words:
            review = review.replace(word, '')
        return review
    
    df['sentiment'] = df['text'].apply(lambda x: sentiment_score(preprocess_review(x[:512], neutral_words)))
    
    sentiment_path = os.path.join(album_dir, "comments_with_sentiments.csv")
    df.to_csv(sentiment_path, index=False)
    print(f"Sentiment analysis completed. Results saved to {sentiment_path}")
    plot_sentiment_distribution(name)

def barGraphs(album_name):
    bert(album_name)
    polarity = []
    positive_comments = []
    negative_comments = []
    neutral_comments = []

    album_dir = os.path.join("albums", album_name)
    comments_file = os.path.join(album_dir, "comments.txt")
    print("Otwieram komentarze")
    with open(comments_file, 'r', encoding='utf-8') as f:
        comments = f.readlines()
    
    for index, items in enumerate(comments):
        print(f"Analizuję komentarz {index}" )
        cleaned_comment = clean_comment(items)
        score = sentiment_score(cleaned_comment)
        polarity.append(score)

        if score >= 4:
            positive_comments.append(items)
        elif score <= 2:
            negative_comments.append(items)
        else:
            neutral_comments.append(items)

    avg_polarity = sum(polarity) / len(polarity)
    
    if avg_polarity >= 4:
        overall_sentiment = "Positive"
    elif avg_polarity <= 2.9:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"
    
    positive_count = len(positive_comments)
    negative_count = len(negative_comments)
    neutral_count = len(neutral_comments)

    results_file = os.path.join(album_dir, 'sentiment_results.txt')
    with open(results_file, 'w', encoding='utf-8') as file:
        file.write(f"Average Polarity: {avg_polarity}\n")
        file.write(f"Overall Sentiment: {overall_sentiment}\n")
        file.write(f"Positive Comments: {positive_count}\n")
        file.write(f"Negative Comments: {negative_count}\n")
        file.write(f"Neutral Comments: {neutral_count}\n")

    labels = ['Positive', 'Negative', 'Neutral']
    comment_counts = [positive_count, negative_count, neutral_count]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, comment_counts, color=['blue', 'red', 'grey'])
    plt.xlabel('Sentiment')
    plt.ylabel('Comment Count')
    plt.title('Sentiment Analysis of Comments for ' + album_name)
    bar_chart_path = os.path.join(album_dir, album_name + '_PosNegNeu.png')
    plt.savefig(bar_chart_path)
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.pie(comment_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=['blue', 'red', 'grey'])
    plt.title('Sentiment Distribution for ' + album_name)
    pie_chart_path = os.path.join(album_dir, album_name + '_Pie.png')
    plt.savefig(pie_chart_path)
    plt.close()

