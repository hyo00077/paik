import requests
import json
import datetime


def instagram(img, sentence, snsID,):
    try:
        appID = "881179656204948"
        appSecret = "1df2ce638ff1b374daa9413ed15dabaf"
        accessToken = "EAAMhbaBkMpQBAMyP3mE32LJMPITG8ZCP8v0AsBWTdf82GN4P5O5MoidRZBAry0zJPShJQwraXmwoxPCj0skqTWrEbYbTAvhvpCJYKgIsZAZA4GPk7zUUZBVe1P5PG2J1kOXvEjRSyqSL52CJPkpaTiRzFBLsjgCSTaC4Gav4Q8HFu2HI6L61H"
        insta_secret_tokken = "85c8741e64a59d12966838c4a8b98d0c"

        # Define Parameters Dictionary
        params = dict()
        # not an actual access token
        params['access_token'] = accessToken
        params['client_id'] = appID                  # not an actual client id
        params['client_secret'] = appSecret     # not an actual client secret
        params['graph_domain'] = 'https://graph.facebook.com'
        params['graph_version'] = 'v15.0'
        params['endpoint_base'] = params['graph_domain'] + \
            '/' + params['graph_version'] + '/'
        # not an actual page id
        params['page_id'] = '103735142514508'
        # not an actual instagram business account id
        params['instagram_account_id'] = '104032509150518'
        params['ig_username'] = 'namjune.paik'
        params['instagram_business_account'] = "17841455936352851"

        # Define Endpoint Parameters
        endpointParams = dict()
        endpointParams['input_token'] = params['access_token']
        endpointParams['access_token'] = params['access_token']

        # Define URL
        url = params['graph_domain'] + '/debug_token'

        # Requests Data
        data = requests.get(url, endpointParams)
        access_token_data = json.loads(data.content)
        access_token_data

        # Define URL
        url = params['endpoint_base'] + \
            params['instagram_business_account'] + "/media"

        # Define Endpoint Parameters
        params['user_tags'] = '''   [
        {
        username:'crying_wet_floor',
        x: 0.5,
        y: 0.8
        }
        ]
        '''
        params["caption"] = "@{}".format(snsID)+" "+"#백남준의보고서"+" "+sentence
        endpointParams = dict()
        endpointParams['image_url'] = img
        endpointParams['access_token'] = params['access_token']
        endpointParams['is_place'] = True
        endpointParams["caption"] = params["caption"]
        print(url)
        # Requests Data
        data = requests.post(url, endpointParams)
        basic_insight = json.loads(data.content)
        if "id" in basic_insight:
            url = params['endpoint_base'] + \
                params['instagram_business_account'] + "/media_publish"
            endpointParams["creation_id"] = basic_insight["id"]
            data = requests.post(url, endpointParams)
            basic_insight = json.loads(data.content)
            if "error" not in basic_insight:
                return True
            else:
                print(basic_insight["error"]["code"])
                return basic_insight["error"]["code"]
        elif "error" in basic_insight:
            return False
    except:
        return False


def facebook(img, sentence):
    appID = "881179656204948"
    appSecret = "1df2ce638ff1b374daa9413ed15dabaf"
    accessToken = "EAAMhbaBkMpQBAMyP3mE32LJMPITG8ZCP8v0AsBWTdf82GN4P5O5MoidRZBAry0zJPShJQwraXmwoxPCj0skqTWrEbYbTAvhvpCJYKgIsZAZA4GPk7zUUZBVe1P5PG2J1kOXvEjRSyqSL52CJPkpaTiRzFBLsjgCSTaC4Gav4Q8HFu2HI6L61H"
    insta_secret_tokken = "85c8741e64a59d12966838c4a8b98d0c"

    # Define Parameters Dictionary
    params = dict()
    params['access_token'] = accessToken        # not an actual access token
    params['client_id'] = appID                  # not an actual client id
    params['client_secret'] = appSecret     # not an actual client secret
    params['graph_domain'] = 'https://graph.facebook.com'
    params['graph_version'] = 'v15.0'
    params['endpoint_base'] = params['graph_domain'] + \
        '/' + params['graph_version'] + '/'
    params['page_id'] = '103735142514508'
    endpointParams = dict()

    url = params["endpoint_base"]+params["page_id"]+"?fields=access_token"
    endpointParams['access_token'] = params['access_token']

    data = requests.get(url, endpointParams).json()
    params["page_access_token"] = data["access_token"]
    endpointParams['access_token'] = params['page_access_token']
    # 이미지 url 교체 필요
    endpointParams["url"] = img
    # 문장 메지 패러미터로 넘겨줌
    endpointParams["message"] = "#백남준의보고서"+" "+sentence

    url = params["endpoint_base"]+params["page_id"]+"/photos"
    data = requests.post(url, endpointParams)
    basic_insight = json.loads(data.content)
    print(basic_insight)
    if "id" in basic_insight:
        return "https://facebook.com/"+basic_insight["id"]
    else:
        print(basic_insight["error"]["code"])
        return basic_insight["error"]["code"]
