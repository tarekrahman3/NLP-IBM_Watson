<pre>
The purpose of this repository is to keep track of my NLP learning

<h3>Learning Resources by Topic</h3>
<strong>Tokenization:</strong>
    Meaning: Splitting text into smaller parts
    Article: <a href="https://www.analyticsvidhya.com/blog/2020/05/what-is-tokenization-nlp/" rel="nofollow">Examples of Tokenization in NLP (Quick Read)</a>
    Different types of tokenization: Sentence Tokenization, Word Tofenization, Character Tokenization, Subword tokenization
    -- <a href="https://www.analyticsvidhya.com/blog/2019/07/how-get-started-nlp-6-unique-ways-perform-tokenization/" rel="nofollow">Methods to Perform Tokenization in Python</a>

</pre>
<section><h4>Re Example 1</h4>
<div class="oembed-gist"><script src="https://gist.github.com/shubham-singh-ss/36a880cce668bb203a99dd9bc5840650.js" type="text/javascript"></script><link rel="stylesheet" href="https://github.githubassets.com/assets/gist-embed-ff75a167df5efbfedb0e388793ca9fe7.css"><div id="gist97055668" class="gist">
    <div class="gist-file" translate="no">
      <div class="gist-data">
        <div class="js-gist-file-update-container js-task-list-container file-box">
  <div id="file-re2-py" class="file my-2">
    
  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python  ">

      
<div class="js-check-bidi blob-code-content">
  <template class="js-file-alert-template">
  <div data-view-component="true" class="flash flash-warn flash-full d-flex flex-items-center">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
  
    <span>
      This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      <a href="https://github.co/hiddenchars" target="_blank">Learn more about bidirectional Unicode characters</a>
    </span>


  <div data-view-component="true" class="flash-action">        <a href="{{ revealButtonHref }}" data-view-component="true" class="btn-sm btn">
  
  Show hidden characters
  

</a>
</div>
</div></template>
<template class="js-line-alert-template">
  <span aria-label="This line has hidden Unicode characters" data-view-component="true" class="bidi-line-alert tooltipped tooltipped-e">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
</span></template>

  <table class="highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file" data-tab-size="8" data-paste-markdown-skip="" data-tagsearch-lang="Python" data-tagsearch-path="re2.py">
        <tbody><tr>
          <td id="file-re2-py-L1" class="blob-num js-line-number js-code-nav-line-number" data-line-number="1"></td>
          <td id="file-re2-py-LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">re</span></td>
        </tr>
        <tr>
          <td id="file-re2-py-L2" class="blob-num js-line-number js-code-nav-line-number" data-line-number="2"></td>
          <td id="file-re2-py-LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s">"""Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet </span></td>
        </tr>
        <tr>
          <td id="file-re2-py-L3" class="blob-num js-line-number js-code-nav-line-number" data-line-number="3"></td>
          <td id="file-re2-py-LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-s">species by building a self-sustaining city on, Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed </span></td>
        </tr>
        <tr>
          <td id="file-re2-py-L4" class="blob-num js-line-number js-code-nav-line-number" data-line-number="4"></td>
          <td id="file-re2-py-LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-s">liquid-fuel launch vehicle to orbit the Earth."""</span></td>
        </tr>
        <tr>
          <td id="file-re2-py-L5" class="blob-num js-line-number js-code-nav-line-number" data-line-number="5"></td>
          <td id="file-re2-py-LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">sentences</span> <span class="pl-c1">=</span> <span class="pl-s1">re</span>.<span class="pl-en">compile</span>(<span class="pl-s">'[.!?] '</span>).<span class="pl-en">split</span>(<span class="pl-s1">text</span>)</td>
        </tr>
        <tr>
          <td id="file-re2-py-L6" class="blob-num js-line-number js-code-nav-line-number" data-line-number="6"></td>
          <td id="file-re2-py-LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">sentences</span></td>
        </tr>
  </tbody></table>
</div>


  </div>

  </div>
</div>
</div>
<noscript>View the code on <a href="https://gist.github.com/shubham-singh-ss/36a880cce668bb203a99dd9bc5840650">Gist</a>.</noscript></div>


</section>