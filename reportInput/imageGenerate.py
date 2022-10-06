from .ImageBack import gradientGenerate, noiseGenerate
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
import os


class ImageGenerate:
    def __init__(self, textShared, generatedDate):
        self.textShared = str(textShared)
        self.generatedDate = generatedDate
        # print(self.textShared, self.generatedDate)

    def params(self):
        return self.textShared, self.generatedDate

    def imageDir(self):
        return os.path.join("./static/image/sns", "{}.jpg".format("{}{}".format(self.generatedDate.split(
            "T")[0], self.generatedDate.split(
            "T")[1][0:8])))

    def imageComp(self):
        text = self.textShared
        print(text)
        fontColor = "#000000"
        date = self.generatedDate

        date = "{} {}".format(date.split(
            "T")[0], date.split(
            "T")[1][0:8])

        print(date)
        shape = (1080, 1080)

        fontSize = 40
        dateSize = 18

        gradientDir = ["hori", "vert"]
        # 그라디언트 생성
        colorizedImg = gradientGenerate(random.choice(gradientDir))

        draw = ImageDraw.Draw(colorizedImg)
        font = ImageFont.truetype('./static/font/sandolGothic.ttf', fontSize)
        date_font = ImageFont.truetype(
            './static/font/sandolGothic.ttf', dateSize)

        var_title_width_length = 26  # 줄글 넓이
        var_pad = 17  # 글간격

        var_title_wrap = textwrap.wrap(text, width=var_title_width_length)
        # var_date_wrap= textwrap.wrap(date, width=var_title_width_length)
        var_len_line = len(var_title_wrap)
        # var_len_date = len(var_date_wrap)
        var_x_point = shape[0]/2-320  # 글자를출력할x축Point:가운데정렬이므로나누기2함
        # var_y_point = shape[1]/2  # 글자를출력할y축Point:가운데정렬로아래에서계산함
        var_y_point = 50

        # 글자사이즈
        var_textsize_h = draw.textsize(var_title_wrap[0], font=font)[1]
        var_datesize_h = draw.textsize(date, font=date_font)[1]

        # var_x_date = shape[0]-draw.textsize(date, font=date_font)[0]-100
        var_x_date = shape[0]/2-draw.textsize(date, font=date_font)[0]/2
        var_y_date = shape[1]-100+dateSize

        # 글자기준yPoint계산
        # var_y_point = var_y_point - \
        #     (((var_textsize_h*var_len_line)+(var_pad*(var_len_line-1)))/2) + \
        #     (var_textsize_h/2)

        for var_line in var_title_wrap:

            draw.text((var_x_point, var_y_point), var_line, fontColor,
                      font=font, )

            var_y_point = var_y_point+var_textsize_h+var_pad

        draw.text((var_x_point+5, var_y_point+20),
                  date, fontColor, font=date_font)

        frame = Image.open('./static/image/Paik_Frame_3.png')
        frame.mode = "RGBA"
        colorizedImg.paste(frame, (0, 0), frame)
        colorizedImg.save(self.imageDir())
