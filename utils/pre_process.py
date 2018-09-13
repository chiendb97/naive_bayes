import re
import  string


class PreProcess:
    def __init__(self):
        with open('/home/chiendb/data/aclImdb/stopwords.txt', 'r') as f:
            self.stopwords = f.readlines()

    def rm_punctuation(self, text):
        """

        :param text:
        :return:
        """
        text = text.replace('/><br />', '')
        text = text.replace('<br', '')
        table = str.maketrans('', '', string.punctuation + string.digits)
        return text.translate(table)

    def text2list(self, text):
        """

        :param text:
        :return list:
        """
        return text.lower().split()

    def rm_stopword(self, text):
        """

        :return:
        """
        return [w for w in text if w not in self.stopwords]

    def strip_html_tags(self, text):
        """
        Strip HTML tags from any string and transfrom special entities
        :param text: text
        :type html:
        :return: text
        :rtype:
        """
        # apply rules in given order!
        rules = [
            {r'>\s+': u'>'},  # remove spaces after a tag opens or closes
            {r'\s+': u' '},  # replace consecutive spaces
            {r'\s*<br\s*/?>\s*': u'\n'},  # newline after a <br>
            {r'</(div)\s*>\s*': u'\n'},  # newline after </p> and </div> and <h1/>...
            {r'</(p|h\d)\s*>\s*': u'\n\n'},  # newline after </p> and </div> and <h1/>...
            {r'<head>.*<\s*(/head|body)[^>]*>': u''},  # remove <head> to </head>
            {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},  # show links instead of texts
            {r'[ \t]*<[^<]*?/?>': u''},  # remove remaining tags
            {r'^\s+': u''},  # remove spaces at the beginning
            {r'[0-9]+': u''},  # remove number
            {r'^A-Za-z': u''},  # remove special character
            {r'(.)\1+': r'\1'},  # remove duplicated character
            {'add.* \d ne.? photo.?': ''}
        ]
        for rule in rules:
            for (k, v) in rule.items():
                regex = re.compile(k)
                text = regex.sub(v, text)
        # replace special strings
        special = {
            '&nbsp;': ' ', '&amp;': '&', '&quot;': '"',
            '&lt;': '<', '&gt;': '>', '"': '', '.': ' ', '-': '', '/': '', ',': '', '  ': ' '
        }

        for (k, v) in special.items():
            text = text.replace(k, v)

        return text

    def transform(self, document):
        cleaned = []
        for text in document:
            text = self.rm_punctuation(text)
            text = self.strip_html_tags(text)
            text = self.text2list(text)
            text = self.rm_stopword(text)
            cleaned.append(text)

        return cleaned