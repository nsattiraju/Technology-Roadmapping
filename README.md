# Technology-Roadmapping
explore next upcoming technologies with the help of wrdcloud


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
