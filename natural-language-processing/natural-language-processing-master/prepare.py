def basic_clean(string):
    '''
    Takes in a string and apply some basic text cleaning to it:
    - Lowercase everything
    - Normalize unicode characters
    - Replace anything that is not a letter, number, whitespace or a single quote
    '''
    
    # Lowercase Everything
    string = string.lower()
    
    # Normalize Unicode Characters
    string = (unicodedata.normalize('NFKD', string)
                .encode('ascii', 'ignore')
                .decode('utf-8', 'ignore')
             )
    
    # Replace anything that isn't a letter, number, whitespace or single quote
    string = re.sub(r"[^a-z0-9'\s]", '', string)
 
    return string


def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()

    return tokenizer.tokenize(string, return_str=True)


def stem(string):
    # Create the nltk stemmer object, then use it
    ps = nltk.porter.PorterStemmer()

    stems = [ps.stem(word) for word in string.split()]
    string_stemmed = ' '.join(stems)
    
    return string_stemmed


def lemmatize(string):
    wnl = nltk.stem.WordNetLemmatizer()

    lemmas = [wnl.lemmatize(word) for word in string.split()]
    string_lemmatized = ' '.join(lemmas)

    return string_lemmatized


def remove_stopwords(string, extra_words=[], exlude_words=[]):
    # Making the stopword list
    stopword_list = stopwords.words('english')
    
    # Adding words to the list
    if extra_words != []:
        [stopword_list.append(word) for word in extra_words]

    # dropping words from the stopword list so we keep them in the text
    if exlude_words != []:
        [stopword_list.remove(word) for word in exlude_wars]

    words = string.split()
    filtered_words = [w for w in words if w not in stopword_list]

    string_without_stopwords = ' '.join(filtered_words)

    return string_without_stopwords


def prep_article(article):
    '''
    Takes in an article, returns a dictionary with the following:
    'title': 'the original title'.
    'original': original,
    'stemmed': article_stemmed,
    'lemmatized': article_lemmatized,
    'clean': article_without_stopwords
    '''
    
    title   = article['title']
    body    = article['body']
    stemmed = stem(body)
    lem     = lemmatize(body)
    clean   = remove_stopwords(body)
        
    article_data = {'title'      : title,
                    'original'   : body,
                    'stemmed'    : stemmed,
                    'lemmatized' : lem,
                    'clean'      : clean
                    }

    return article_data


def prep_article_data(articles):
    '''
    Takes in a list of articles dictionaries. 
    Applies the prep_article function to each one, and returns the transformed data
    '''
    
    output = []
    for article in articles:
        article_data = prep_article(article)
        output.append(article_data)
   
    return output
        
    
    