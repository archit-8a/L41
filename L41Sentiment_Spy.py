import colorama
from colorama import Fore,Style
from textblob import TextBlob   


colorama.init()

print("Welcome to the Sentiment Spy!")

user_name=input("Please enter your Name:  ").strip()#strip=Remove all the faces
if not user_name:
    user_name="Mystery Agent"

print("Hello Agent",user_name)
print("Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment.")


while True:
    user_input=input("Enter a sentence or type exit to quit  ").strip()

    if not user_input: 
        print("Please enter some valid text or command")
        continue

    if user_input.lower()=="exit":
        print("Farewell,Agnet",user_name)
        break


    else:
        polarity= TextBlob(user_input).sentiment.polarity
        if polarity>0.25:
            sentiment_type="Positive"
            print(sentiment_type,"sentiment detected!")

        elif polarity<-0.25:
            sentiment_type="Negative"
            print(sentiment_type,"sentiment detected!")

        else:
            sentiment_type="Neutral"
            print(sentiment_type,"sentiment detected!")
            continue
































































































