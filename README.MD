# Local Whisperer



## How to setup environment

Assuming using miniconda from Anaconda.org

CREATE an .env file (contents)
```
HUGGING=hf_<YOUR_TOHEN_HERE>
```

Usage (requires python version 3.11)

Create a python environment 
```{sh}
conda create whisper_env python=3.11.0
```

 ## Files 
 wavconverter.py script to convert MP3/M4A/etc formats to wav formats 


 ``` {sh}
 python wavconverter.py hello_quiet.m4a out\Quiet.wav
 ```
### On windows you can use Sound recorder app to record M4A files

Code taken from [Local whisperer | KDNuggets](https://www.kdnuggets.com/local-whisper-audio-transcription)

Code for git ignore taken from [Python Github gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)