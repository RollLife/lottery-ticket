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
        self.status_code = True
        print(f"기본 입력 텍스트 : {self.origin_text}")

    def consider_type(self):
        """

        :return:
        """

    def _check_sepatator(self, text):
        # check separate character
        for separator in ALLOWED_PARSE_SEPARATORS:
            if separator in text:
                return separator

        print("Not found correct separator")
        # TODO: raise하여 에러코드를 내뱉게 해야함
        return False

    def parse(self, text):
        self.separator = self._check_sepatator(text)

        if not self.separator or self.separator is None:
            return text

        parse_data = self.origin_text.split(self.separator)

        try:
            parse_data = [int(number) for number in parse_data]
        except Exception as e:
            pass

        return parse_data

    def validate_data(self, parse_data):
        # parse_data가 리스트형이 아닐경우 탈락
        if not isinstance(parse_data, list):
            print("Must be parse data type is list type")
            return False

        # 최소 숫자 6개 이상
        if len(parse_data) <= 5:
            print("Must exist numbers more than 5")
            return False

        # 숫자 이외의 문자가 들어 갔을경우 아웃
        for number in parse_data:
            if not isinstance(number, int):
                print(f"This character is not integer")
                return False

        return True

    def run(self):
        parse_data = self.parse(self.origin_text)

        status = self.validate_data(parse_data)
        if not status:
            print("오류로 인하여 재생성 필요")
            self.status_code = status
            return self.origin_text

        self.parse_data = parse_data
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
