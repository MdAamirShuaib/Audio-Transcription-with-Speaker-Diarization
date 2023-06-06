import yake
from wordcloud import WordCloud
import base64
from io import BytesIO
import random

def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl({}, {}%, {}%)".format(250, random.randint(30, 80), random.randint(30, 70))

def word_cloud(input_text,num_of_keywords,removeWords):
    w = WordCloud()
    stop_words = list(w.stopwords)
    removeWordslist = removeWords.split(',')
    custom_stop_words = []
    for rmword in removeWordslist:
        custom_stop_words.append(rmword.strip())
    stop_words = set(stop_words + custom_stop_words)
    # use yake to extract keywords
    custom_kw_extractor = yake.KeywordExtractor(lan='english', n=4, dedupLim=0.5, dedupFunc='leve', windowsSize=1, top=num_of_keywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(input_text)

    # get keywords and their position
    keywords_list = []
    for kw in keywords:
        keyword = kw[0].lower()
        ngram_size = len(keyword.split())
        if ngram_size == 1:
            keywords_list.append(keyword)
        elif ngram_size == 2:
            keywords_list.append(keyword.replace(' ', '_'))
        else:
            joined_keyword = ''
            for sub_keyword in keyword.split():
                if joined_keyword:
                    joined_keyword += '_'
                joined_keyword += sub_keyword
            keywords_list.append(joined_keyword)


    keywords_list = ', '.join(keywords_list)
    #print(keywords_list)
    # create and generate a word cloud image
    wordcloud = WordCloud(width=1920, height=1080, 
                min_font_size=25, 
                max_words=num_of_keywords,
                background_color="white", 
                stopwords=stop_words,
                collocations=True,
                relative_scaling=1.0,
                color_func=custom_color_func,
                regexp=r"\w[\w ']+").generate(keywords_list)
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()
    buffer = BytesIO()
    wordcloud.to_image().save(buffer, 'png')
    b64 = base64.b64encode(buffer.getvalue())
    return {'wordcloud': b64}

