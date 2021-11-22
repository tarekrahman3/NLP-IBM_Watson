<html>
<head>
  <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.0.3/styles/default.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.0.3/highlight.min.js"></script>
  <script>hljs.initHighlightingOnLoad();</script>
</head>
<body>


<h2>The purpose of this repository is to keep track of my NLP learning</h2>
<h3><strong>Learning Resources by Topic</strong></h3>
<strong>Tokenization (Difficulty Level: Easy):</strong>
    Meaning: Splitting text into smaller parts
    Article: <a href="https://www.analyticsvidhya.com/blog/2020/05/what-is-tokenization-nlp/" rel="nofollow">Examples of Tokenization in NLP (Quick Read)</a>
    Different types of tokenization: Sentence Tokenization, Word Tofenization, Character Tokenization, Subword tokenization
    -- <a href="https://www.analyticsvidhya.com/blog/2019/07/how-get-started-nlp-6-unique-ways-perform-tokenization/" rel="nofollow">Methods to Perform Tokenization in Python</a>
    <pre><code class="python">    import re
    text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet 
    species by building a self-sustaining city on, Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed 
    liquid-fuel launch vehicle to orbit the Earth."""
    sentences = re.compile('[.!?] ').split(text)
    print(sentences)</code></pre>
<strong>Sentence Splitting (Difficulty Level: Medium):</strong>
    Meaning: The process of separating free-flowing text into sentences

<strong>Stopwords Filtering (Difficulty Level: Medium):</strong>
</body>
</html>