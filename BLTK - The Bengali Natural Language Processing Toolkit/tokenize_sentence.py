# no module named 'sklearn.feature_extraction.dictvectorizer' ---- sudo apt install python3-sklearn 
target_url = r'https://www.thedailystar.net/bangla/%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%AF%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF-%E0%A6%93-%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%9F%E0%A6%86%E0%A6%AA/%E0%A6%AC%E0%A6%BF%E0%A6%9C%E0%A7%8D%E0%A6%9E%E0%A6%BE%E0%A6%A8-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%AF%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF-%E0%A6%97%E0%A7%87%E0%A6%9C%E0%A7%87%E0%A6%9F%E0%A6%B8/%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%AF%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF/%E0%A6%B8%E0%A7%8D%E0%A6%AA%E0%A7%87%E0%A6%B8%E0%A6%8F%E0%A6%95%E0%A7%8D%E0%A6%B8-%E0%A6%95%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%AA%E0%A6%B8%E0%A7%81%E0%A6%B2%E0%A7%87%E0%A6%B0-%E0%A6%9F%E0%A7%9F%E0%A6%B2%E0%A7%87%E0%A6%9F-%E0%A6%AD%E0%A6%BE%E0%A6%99%E0%A6%BE-%E0%A6%A1%E0%A6%BE%E0%A7%9F%E0%A6%BE%E0%A6%AA%E0%A6%BE%E0%A6%B0-%E0%A6%AA%E0%A6%B0%E0%A7%87'

def create_session():
    import requests_html
    return requests_html.HTMLSession()

def get(url):
    return session.get(url)

def get_inner_text(response):
	js = """
	        () => {
	            return document.body.innerText
	            }
	    """
	text = response.html.render(script=js, reload=False)
	#print('Source Text')
	#print(text)
	return text

def close_session():
    session.close()

def word_tokenization(text):
    from bltk.langtools import Tokenizer
    print('TOKENIZED WORDS')
    words = Tokenizer().word_tokenizer(text)
    print(words)
    return words

def sentence_tokenization(text):
    from bltk.langtools import Tokenizer
    print("TOKENIZED SENTENCES")
    sentences = Tokenizer().sentence_tokenizer(text)
    print(f"sentences found: {len(sentences)}")
    print(sentences)
    return sentences

def get_named_entities(sentences):
	from bltk.langtools import Tokenizer
	from bltk.langtools import Chunker
	grammar = r"""
	NP: {<DAB>?<JJ|JQ>*<N.>}
	"""
	tokened_text = [Tokenizer().word_tokenizer(sentence) for sentence in sentences]
	noun_phrases = []
	for t in tokened_text:
	    chunky = Chunker(grammar=grammar, tokened_text=t)
	    chunk_tree = chunky.chunk()
	    for i in chunk_tree.subtrees():
	        if i.label() == "NP":
	            print(i)
	            noun_phrases.append(i)
	return noun_phrases


if __name__ == "__main__": 
    session = create_session()
    text = get_inner_text(get(target_url))

    sentences = sentence_tokenization(text)
    named_entities = get_named_entities(sentences)


    close_session()