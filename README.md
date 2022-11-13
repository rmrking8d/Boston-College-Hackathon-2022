# HackathonProject2022

## Goals:
Create Python script that automatically enrolls you into courses

## setup
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
