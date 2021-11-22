from bltk.langtools import Tokenizer
import requests_html

target_url = r'https://www.thedailystar.net/bangla/%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%AF%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF-%E0%A6%93-%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%9F%E0%A6%86%E0%A6%AA/%E0%A6%AC%E0%A6%BF%E0%A6%9C%E0%A7%8D%E0%A6%9E%E0%A6%BE%E0%A6%A8-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%AF%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF-%E0%A6%97%E0%A7%87%E0%A6%9C%E0%A7%87%E0%A6%9F%E0%A6%B8/%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%AF%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF/%E0%A6%B8%E0%A7%8D%E0%A6%AA%E0%A7%87%E0%A6%B8%E0%A6%8F%E0%A6%95%E0%A7%8D%E0%A6%B8-%E0%A6%95%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%AA%E0%A6%B8%E0%A7%81%E0%A6%B2%E0%A7%87%E0%A6%B0-%E0%A6%9F%E0%A7%9F%E0%A6%B2%E0%A7%87%E0%A6%9F-%E0%A6%AD%E0%A6%BE%E0%A6%99%E0%A6%BE-%E0%A6%A1%E0%A6%BE%E0%A7%9F%E0%A6%BE%E0%A6%AA%E0%A6%BE%E0%A6%B0-%E0%A6%AA%E0%A6%B0%E0%A7%87'
js = """
        () => {
            return document.body.innerText
            }
    """

requests = requests_html.HTMLSession()

resp = requests.get(target_url)
text = resp.html.render(script=js, reload=False)
print('Source Text')
print(text)
tokenizer = Tokenizer()

print('TOKENIZED WORDS')
words = tokenizer.word_tokenizer(text)
print(words)