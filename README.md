## The Cupid Shuffle:
### Can music "play cupid"?

When it comes to compiling the ultimate playlist of the heart, the question arises: Are some music genres more romantic than others? 

### Sussing out the answer, the data recipe:  
- Romance song lyrics retrieved using the genius api from country and hip hop compared using machine learning techniques.
- Music lyric extraction with Python, courtesy of the GENIUS Developer API
- Songs were randomly selected uing the Spotify Developer API, the code for which is housed in a separate repository: <a href='https://github.com/sherirosalia/sound_effects.git'>sound_effects</a>
-  Machine learning processing with the NLTK library to count word frequencies.
### Hip Hop Words
[<img src="docs/images/hip_hop_top.png" width="250"/>](images/hip_hop_top.png)
### Folder structure in root
- README.md 
- data_files houses country and hip hop JSON from Spotify
- website files and images in docs
- screenshots are in images 
- python folder holds code for genius api which is complete in app.py. There are also two jupyter notebook files which analyze the lyrics with PySpark, NLTK and Python Pandas
### "We've only just begun." 
There are so many avenues to take music analysis using natural language libraries (NLP). Thank you for reading this far and I hope you find the scripts helpful. If you do, please feel free to clone or fork the project and take it to the next level. I would love to hear what you do with it. An explanation of the project is here: <a href='https://sherirosalia.github.io/cupid_shuffle/'>Cupid Shuffle</a>

### Related article from OkCupid 
For more on this topic, check out this article:  <a href ="https://theblog.okcupid.com/https-theblog-okcupid-com-dating-deal-breakers-music-e9bc60c95222">Understanding Deal Breakers: The Psychology of Music and Romance"</a>





