import tweepy
import requests


def Twitter(img, sentence, snsID):

    api_key = "uTvQYZJqlItFoFYM0R9Xmiscu"
    api_secret = "hZLm7qpzsFdCI0rP9mADYiuxy2kfOs20mj5yR2CW0qhTcdC2go"
    access_token = "1570735746612629511-Ne6w46VJcaA8xL1cseogLvy6pXc9Ie"
    access_token_secret = "ffOwBBC4Fpv2fssiQWxyZ3WnMasYb5yoMCU58UWvGZe5s"
    bearer_token = "6bp3XOv1S8mynV4rultCUBXbGFL8htgrdwPndMWIpO9gD"
    user_name = "paiks_papers"
    client_ID = "NEtkVmxrRVNVMG9MeDdlUTlmT1Q6MTpjaQ"
    client_secret = "THdnpoMBvyrCDHw5CQbwwyOmaRHqHNJ-FOPEHtSKUxWrAWb9TI"
    # print(img)
    try:
        auth = tweepy.OAuth1UserHandler(
            api_key, api_secret, access_token, access_token_secret
        )
        format = "@{}".format(snsID)+" "+"#백남준의리포트"
        sentence_format = sentence + " " + format
        inputNum = 165-len(format)
        print(inputNum)
        print(len(sentence_format))
        if len(sentence_format) > 166:
            sentence_re = sentence[0:inputNum]+"⋯"+" "+format
            print(sentence_re)
        else:
            sentence_re = sentence_format
        api = tweepy.API(auth)
        media = api.media_upload(filename=img)
        tweet = api.update_status(status=sentence_re, media_ids=[
            media.media_id_string])
        return True
    except:
        return False
