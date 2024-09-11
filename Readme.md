## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/SeleniumSimpleExample.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```
- Required libraries (Review requirements.txt)
```
conda create --name selenium python jupyter pandas matplotlib seaborn
conda activate selenium
pip install selenium
pip install webdriver-manager
pip install -U selenium
pip install pytest
pip install html-testRunner
pip install pytest-html
pip install robotframework
pip install webdrivermanager
pip install --upgrade robotframework-browser jupyterlab-server \
                      typing-extensions robocorp-inspector-commons \
                      jupyterlab notebook
pip install --upgrade robotframework-seleniumlibrary
pip install --upgrade robotframework-browser robocorp-inspector-commons

# In Windows powershell
Get-ExecutionPolicy         # To confirm current police Bypass/RemoteSigned
Set-ExecutionPolicy RemoteSigned
(Install nodejs and reboot)
rfbrowser clean-node
rfbrowser init
Set-ExecutionPolicy Default

pip install robotframework-requests
conda install conda-forge::rpaframework
```

- To run unittest
```
python -m unittest
```

- To run pytest
```
pytest
pytest --html=test_with_pytest/Reports/report.html
```

- To test robotframework is correctly installed
```
robot --version
```

- To run roboframework tests
```
robot -d test_with_robotframework\output\ test_with_robotframework
```
