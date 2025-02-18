import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure you have the stopwords corpus downloaded
nltk.download('stopwords')

# Access the stopwords list
stop_words = set(stopwords.words('english'))
def clean_text(text):
    text = text.lower() # Convert text to lowercase
    text = re.sub(r'https?://\S+|www\.\S+', '', text) # Remove URLs
    text = re.sub(r'<.*?>', '', text) # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
    text = re.sub(r'\d+', '', text) # Remove digits
    text = re.sub(r'\n', ' ', text) # Remove newline character
    text = re.sub(r'\s+', ' ', text).strip() # Remove extra spaces
    return text

def tokenize_text(text):
    tokens = word_tokenize(text) # Tokenize the text
    tokens = [token for token in tokens if token not in stop_words] # Remove stopwords
    return tokens

def lemmatize_text(tokens):
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens] # Lemmatize the text
    return tokens

def preprocess_text(text):
    text = clean_text(text)
    tokens = tokenize_text(text)
    tokens = lemmatize_text(tokens)
    text = ' '.join(tokens)
    return text

def preprocess_data(data):
    data['Processed_Text'] = data['Text'].apply(preprocess_text)
    return data