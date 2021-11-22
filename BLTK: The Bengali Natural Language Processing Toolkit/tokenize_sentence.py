from bltk.langtools import Tokenizer

# Sample text
text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। "\
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

# Creating an instance
tokenizer = Tokenizer()

# Tokenizing words
print('TOKENIZED WORDS')
words = tokenizer.word_tokenizer(text)
print(words)
