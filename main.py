# Import library for twitter api
import tweepy
import requests
# import library visualization beatyfull json docs
import json
# Autenticación
# API key:
consumer_key = "DnNcGdUfGQPKjotNwsPSMWZ4L"
# API secret key:
consumer_secret = "IeV7TLhhf5KV9SojK7DkjTTkcP312dCVO5UbU8djymMBwMqafa"
# Access token :
access_token = "1041653961676083200-zx7bIi0pLHjW6KfWcFEHSSxmWqUYos"
# Access token secret :
access_token_secret = "UZTlNoKmm94Ij8xGPUb27ySMtNovRV6hdAsVsZGsdKKaW"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Instanciar el objeto de la clase Api
api = tweepy.API(auth , wait_on_rate_limit=True , wait_on_rate_limit_notify=True)


# Veamos información de mi twitter
# data_me = api.me()
# print(json.dumps(data_me._json, indent=2 ))


# Obtener información de otro usuario,en nuestro ejemplo
# data_adidas = api.get_user("adidas")
# print(json.dumps(data_adidas._json, indent=2))

# Obtener #seguidores de una cuenta(usuario)
#data_followers = api.followers(screen_name="adidas")
# print(len(data_followers))

# for user in data_followers:
#     print(json.dumps(user._json, indent=2))

# Una Clase de tweepy para obtener un grupo de información deseada es:

# for user in tweepy.Cursor(api.followers,screen_name="adidas").items(10):
    # print(json.dumps(user._json, indent=2))

#  Una clase de tweepy para obntener los seguidos de un usuario:

# for user in tweepy.Cursor(api.friends,screen_name="adidas").items(10):
#   print(json.dumps(user._json, indent=2))


# Una clase para obtener todos los tweets de un usuario
# for tweet in tweepy.Cursor(api.user_timeline, screen_name="adidas", tweet_mode = "extended").items(2):
#     print(json.dumps(tweet._json, indent=2))
    

#Busqueda de tweets

# for tweet in tweepy.Cursor(api.search, q="covid-19", tweet_mode="extended").items(2):
#     print(json.dumps(tweet._json, indent=2))


# Extraer informacion de un tema específico

for tweet in tweepy.Cursor(api.search, q = "covid-19", tweet_mode="extended").items(40):
    print(json.dumps(tweet._json["full_text"],indent=2))
   





