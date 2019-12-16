# Technology-Roadmapping
explore next upcoming technologies with the help of wordcloud


Technology Roadmapping explores a technology background by collecting the words having most frequency from a webpage. The words are refined and processed before producing the output. The words with maximum frequency are shown in bigger font size as compared to those having less frequency. In addition to this it gives an sentiment analysis on each technological domain. 

###Algorithm to calculate font size based on frequency

```python
fontMax = 5.5
fontMin = 1.5
K = (freqTag - minFreq)/(maxFreq - minFreq)
frange = fontMax - fontMin
C = 4            
K = float(freqTag - minFreq)/(maxFreq - minFreq)
size = fontMin + (C*float(K*frange/C))
```
## To run the project 
1. Download the Github file as zip and extract the files and store in your local computer
2. Install all the requirements mentioned in requirements.txt
3. Run as python words.py in your terminal from the folder
4. Copy the local host address and paster in the browser
