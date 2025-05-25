from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
finbert_tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
finbert_model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
finbert_classifier = pipeline("sentiment-analysis", model=finbert_model, tokenizer=finbert_tokenizer, device=0)

def get_sentiment(news: list[str]) ->int:
    result = finbert_classifier(news)
    total = 0
    for i in result:
        temp = 0
        if(i['label']=='positive'):
            temp = (50+(50*i['score']))
        elif(i['label']=='neutral'):
            temp=(40+(20*i['score']))
        else:
            temp=(50-(50*(i['score'])))
        total+=temp
    if len(result)==0:
        return 0
    return total/len(result)


