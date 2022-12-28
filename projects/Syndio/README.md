# INSTRUCTIONS 

## Overview

Take home assignment was completed using Golem framework https://golem-framework.readthedocs.io/en/latest/. Golem framework uses Python and Selenium. 

* From Tests page, each test can be ran individually via default Chrome browser. 

* To run all tests, go to Suites and run 

`all_tests_multiple_chrome_configurations`

Suite will run all 6 test files in 4 Chrome configurations: Desktop screen size Chrome, Tablet vertical and horizontal, Phone screen size.

Reports can be viewed in reports section of Golem gui with screenshots attached on failures. 

Recording of test execution:

<video src="run.mov" controls="controls">
</video>

## Requirements
### Python
Golem requires Python 3.6 or higher.

#### Windows:

The Windows installer works fine, you can get it from here: python.org/downloads/

#### Mac:

To install on Mac OS follow these instructions: Installing Python 3 on Mac OS X

#### Linux:

Debian 8 and Ubuntu 14.04 comes with Python 3.4 pre-installed, newer Linux distributions might come with newer Python versions.

Since Linux tends to have both Python 2 and 3 installed alongside each other, the command to execute the latter should be ‘python3’ instead of just ‘python’.

### PIP
PIP is the package manager for Python. It is required to install Golem and its dependencies. Check if you already have it. PIP comes bundled with the newer versions of Python.

`pip --version`

or

`pip3 --version`
If you don’t have PIP installed, follow these instructions.

## Create a Virtual Environment
It is recommended to install Golem and its dependencies in a virtual environment instead of globally. To do that, follow these steps:

### Install Virtualenv
`pip install virtualenv`

Create a new virtualenv in the ‘./env’ folder

`virtualenv env`

If the virtual environment is being created with Python 2 instead of 3, use the following command instead:

`virtualenv env -p python3`

### Activate the Environment¶

To use a virtual environment it needs to be activated first.

### Windows:

`env\scripts\activate`

### Mac/Linux:

`source env/bin/activate`

### Install Golem Using PIP

The quickest and the preferred way to install Golem.

`pip install golem-framework`

### Installing From Source

`pip install -U https://github.com/golemhq/golem/archive/master.tar.gz`

## Download Webdriver

Each browser requires its own Webdriver executable. Golem uses the webdriver-manager tool to download these automatically.

`cd <test_directory>`

`webdriver-manager update`

The Webdriver executables are downloaded into the drivers folder inside the Test Directory.

The settings.json file contains a key for each browser that should point to the Webdriver file for that browser. For example:

settings.json

`{
    "chromedriver_path": "./drivers/chromedriver*"
}`

The ‘*’ wildcard at the end of the path is used to match the highest version available, in the case there’s more than one present.

This doesn’t need to be modified unless the Webdriver files are located elsewhere.

For more detail, check this page.

## Start the Web Module
To start the Golem Web Module, run the following command:

`golem gui`

The Web Module can be accessed at http://localhost:5000/

The following superuser is available at the start: username: **admin** / password: **admin**

## Run Tests with Golem

Navigate to http://localhost:5000/

From Tests page, each test can be ran individually via default Chrome browser. 

To run all tests, go to Suites and run 

`all_tests_multiple_chrome_configurations`