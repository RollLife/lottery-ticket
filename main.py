import re
import requests

ALLOWED_PARSE_SEPARATORS = [",", " "]


class Lottery:
    def __int__(self):
        pass

    def consider_type(self):
        """

        :return:
        """


class Parse:
    def __init__(self, text):
        self.origin_text = text
        self.parse_data = text
        self.separator = None
        print(f"기본 입력 텍스트 : {self.origin_text}")

    def consider_type(self):
        """

        :return:
        """

    def check_sepatator(self):
        # check separate character
        for separator in ALLOWED_PARSE_SEPARATORS:
            if separator in self.origin_text:
                self.separator = separator

        print("Not found correct separator")

    def parse(self):
        self.check_sepatator()

        for separator in ALLOWED_PARSE_SEPARATORS:



    def run(self):
        self.parse()
        return self.parse_data


if __name__ == '__main__':
    numbers = "1,2,3,4,5,6"
    url = "https://dhlottery.co.kr/gameResult.do?method=myWinSearch" \
          "&txtNo00=1&txtNo01=2&txtNo02=3&txtNo03=4&txtNo04=5&txtNo05=6&drwNo=1046"

    a = Parse(numbers)
    result = a.run()
    print(f"변경된 것 : {result}")
    # post 호출
    # txtNo_1=1&txtNo_1=2&txtNo_1=3&txtNo_1=4&txtNo_1=5&txtNo_1=6

    # url2 = "https://dhlottery.co.kr/gameResult.do?method=myWinNumberList2"
    # form_data = {"txtNo_1": 1, "txtNo_1": 2, "txtNo_1": 3, "txtNo_1": 4, "txtNo_1": 5, "txtNo_1": 6}

    # a = requests.get()
