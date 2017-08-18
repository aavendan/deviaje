#coding:latin-1
import tweepy
import planificacion as pl

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "TRaEdNf3fli7LBxcFXQiCZVZ2",
    "consumer_secret"     : "E2XQjHigfMn6jiFGk0axz70jD2ESbs6ii05GRRWBTQfcRQWOTV",
    "access_token"        : "887365445870923778-o9l0QM3ndMCB7047ogLJdFwI7t6tdFJ",
    "access_token_secret" : "OzawsPSEjOCEnFJBN2ZEgEXuFreOOc1rhK17WxcaWiJpd"
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  geo = { "type":"Point", "coordinates":[37.78217, -122.40062] }
  status = api.update_status(status=tweet, lat=geo["coordinates"][0], long=geo["coordinates"][1])
  # Yes, tweet is called 'status' rather confusing

def geocod(lat, long, city, query):
    cfg = {
        "consumer_key": "TRaEdNf3fli7LBxcFXQiCZVZ2",
        "consumer_secret": "E2XQjHigfMn6jiFGk0axz70jD2ESbs6ii05GRRWBTQfcRQWOTV",
        "access_token": "887365445870923778-o9l0QM3ndMCB7047ogLJdFwI7t6tdFJ",
        "access_token_secret": "OzawsPSEjOCEnFJBN2ZEgEXuFreOOc1rhK17WxcaWiJpd"
    }

    api = get_api(cfg)
    # result = api.reverse_geocode(lat=lat,long=long)
    # print(result)

    max_tweets = 1000
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, geocode=str(lat)+","+str(long)+",150km").items(max_tweets)]

    file = open("tweetsCity/"+city+".txt", 'w', encoding='utf-8')

    for tweet in searched_tweets:
        file.write(str(tweet._json) + "\n")
    file.close()

def tweetsPorCiudad():
    ciudades = pl.ciudadesDesdeGuayaquil()
    datosciudades = pl.datosCiudades()

    for ciudad in ciudades:
        for datos in datosciudades:
            if ciudad[0] == datos[0]:
                query = datos[-1].split(" ")
                query = "#ecuador OR " + " OR ".join(query)
                # print(ciudad[0], ciudad[3:][0],ciudad[3:][1], datos[-1])
                geocod(ciudad[3:][0], ciudad[3:][1], ciudad[0], query)

if __name__ == "__main__":
    # cfg = {
    #     "consumer_key": "TRaEdNf3fli7LBxcFXQiCZVZ2",
    #     "consumer_secret": "E2XQjHigfMn6jiFGk0axz70jD2ESbs6ii05GRRWBTQfcRQWOTV",
    #     "access_token": "887365445870923778-o9l0QM3ndMCB7047ogLJdFwI7t6tdFJ",
    #     "access_token_secret": "OzawsPSEjOCEnFJBN2ZEgEXuFreOOc1rhK17WxcaWiJpd"
    # }
    #
    # api = get_api(cfg)
    # query = '#ecuador OR #playa OR #feriado OR #quito OR #guayaquil OR #cuenca'
    # max_tweets = 1000
    # searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, geocode="139.6833,35.6833,150km").items(max_tweets)]
    #
    # file = open("tweets2.txt", 'w', encoding='utf-8')
    #
    # for tweet in searched_tweets:
    #     file.write(str(tweet._json)+"\n")
    #
    # file.close()

    #geocod(-2.548985, -78.8714679)

    #main()

    query = "#ecuador OR #guayaquil OR #feriado"
    # print(ciudad[0], ciudad[3:][0],ciudad[3:][1], datos[-1])
    geocod( -2.193772, -79.879707,"Guayaquil2",query)