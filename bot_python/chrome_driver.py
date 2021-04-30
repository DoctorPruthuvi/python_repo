from yaml import load, YAMLError
import logging.config
from task_sender import taskSender
from joblib import Parallel, delayed
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options 
import uuid 

logging.config.fileConfig('logs/logging.ini', disable_existing_loggers=False)
logging.getLogger('paramiko').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


class chromeDriver:

    def __init__(self,task_config_path,app_config):

        self.tempPath =app_config["temp_path"]
        self.app_config = app_config["chrome_driver_path"]
        self.headless = app_config["headless_mode"]
        self.app_config =app_config
        self.task_config_path=task_config_path
        self.chrome()

    def chrome(self):

        # support to get response status and headers
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'performance': 'ALL'}
        opt = webdriver.ChromeOptions()

        if self.headless:
            #add options for the chrome driver
            opt.add_argument("--headless")
            opt.add_argument("--disable-xss-auditor")
            opt.add_argument("--disable-web-security")
            opt.add_argument("--allow-running-insecure-content")
            opt.add_argument("--no-sandbox")
            opt.add_argument("--disable-setuid-sandbox")
            opt.add_argument("--disable-webgl")
            opt.add_argument("--disable-popup-blocking")
            guid = str(uuid.uuid1())
            print(guid) 
            
        opt.add_experimental_option("prefs", { 'download.default_directory': self.tempPath + guid })
        driver = webdriver.Chrome(options=opt,desired_capabilities=d)
        #call task class
        logger.info("starting Downloading reports in"+self.task_config_path)
        
        return(driver,guid,self.app_config,self.tempPath,self.task_config_path)
        
