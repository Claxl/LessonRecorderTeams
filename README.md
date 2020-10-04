# Lesson Recorder 

This is a simple script that start record when you have lesson with teams

## What's needed
- OBS studio
- Python 3.7
- Microsoft Teams
## How to proceed
- Create your scene in OBS studio
- For record teams window disable in teams option the GPU acceleration 
- Edit the src code provided 
- For startup start with windows, just put a shortcut in 
```bash
C:\Users\<USER>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
```
## Usage

```python
lesson = ["day1","day2"];
timeLesson = {}
timeLesson["day1"] = "time1","time2"
timeLesson["day2"] = "time1"
```
Put your correct day and time lesson for correct work, the day should be in this form "Sunday", and time is "12:00"
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
