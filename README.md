# canvas-autogroup

## Converts student-made groups to group submission compatible groups
#### Config file instructions
* Create file called config.py (touch config.py)  
* Navigate to the People tab in the canvas class page.
![test](/img/group_set.png)
* Click on + Group Set and add new group set.
![test2](/img/ids.png)
* Check the URL bar. Copy the circled values.
* Add the circled values to config.py. The first/red circle value is COURSE_ID and blue/second circle value is GROUP_CATEGORY_ID.
* Please refer to [here](https://community.canvaslms.com/docs/DOC-10806-4214724194) for API_KEY.
![test3](/img/sample_config_file.png)
* This is an example config.py

#### Setup and run
###### This program is written with Python 3.   
Install requests library through pip
```python
pip install requests
```
Run tests
```python
python tests.py
```
Run script
```python
python autogroup.py
```
