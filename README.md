# HackathonProject2022

## Goals:
The theme for this year's Hackathon was Mental Health. Registration is stressful at BC. We decided to create Python script that automatically enrolls you into courses.

## Setup:
pip install selenium (run this in top level folder of project)
Navigate to "login.json.txt" and create a copy. Enter your eagleApps login information in the proper fields, then remove the "txt" from the edited file



## Risk
Note, if script doesn't run chrome, remove 
```
from webdriver_manager.chrome import ChromeDriverManager
```
and the
```
ChromeDriverManager().install()
```

argument from driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
