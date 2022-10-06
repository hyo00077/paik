import os
from .twitter_api import Twitter
from .facebook_api import instagram, facebook


class snsShare:
    def __init__(self, snsChoice, snsID, img, sentence):
        self.snsChoice = str(snsChoice)
        self.snsID = str(snsID)
        self.sentence = sentence
        if os.path.isfile(img):
            self.img = img
        else:
            return
        print(self.snsChoice, self.snsID)

    def params(self):
        return self.snsChoice, self.snsID,

    def twitter(self):
        return Twitter(self.img, self.sentence, self.snsID)

    def instagram(self):
        print("인스타그램입니다.")

        return instagram(self.sentence, self.snsID)

    def facebook(self):
        print("페이스북입니다.")

        return facebook(self.sentence)

    def snsDetect(self):
        if self.snsChoice == "twitter":
            return self.twitter()
        if self.snsChoice == "instagram":
            return self.instagram()
        if self.snsChoice == "facebook":
            return self.facebook()
