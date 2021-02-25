# Comprendo

# What is Comprendo?
Comprendo is a Machine Learning tool that uses Entity Extraction to find interesting things on Twitter.

# How does it work?
Comprendo combines a couple of cool cloud technologies to deliver interesting results. The core of Comprendo is AWS Comprehend - an AWS service that lets you use packaged machine models to pull out entities from text.

When you enter a topic into Comprendo, it does a few things. First, it uses the Twitter API to search Twitter for a bunch of tweets related to that topic. Then, it runs each of those tweets through AWS Comprehend to pull out all the entities it can. Finally, it filters the results and displays them.

# Got questions?
This was a fun hobby project! Feel free to reach out to me on LinkedIn or check out [my website](zacharyjklein.com) if you want to know more!