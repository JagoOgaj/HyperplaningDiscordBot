from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from typing import ClassVar
from selenium.webdriver.common.keys import Keys
import time as t
from utils.tools import singleton
import envVar

# Types
type DriverType = webdriver.Firefox
type DriverWait = WebDriverWait
type ElementRef = WebElement

@singleton
class DriverObj[T]:
    # Attributs
    _driver: DriverType
    _wait: DriverWait
    _service: Service

    # Static
    _timeoutForLoadElement: ClassVar[float] = 1.5
    _timeoutForTakePicture: ClassVar[int] = 1
    _pathToSavePictureOfSchedule: ClassVar[str] = envVar.OUTPUT

    def __init__(self, driverPathExecutable: T, url: T, elemntHtml: T, search: T) -> None:
        self._driverPathExecutable = driverPathExecutable
        self._url = url
        self._elemntHtml = elemntHtml
        self._search = search

    def __setService(self) -> None:
        self._service = Service(executable_path=self._driverPathExecutable)

    def __setDriver(self) -> DriverType:
        options: Options = Options()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        if envVar.FIREFOX_PATH:
            options.binary_location = envVar.FIREFOX_PATH

        self._driver = webdriver.Firefox(service=self._service, options=options)

    def __openWebPage(self) -> None:
        self._driver.get(self._url)

    def __setWebDriverWait(self) -> None:
        self._wait = WebDriverWait(self._driver, self._timeoutForLoadElement)

    def __getElementRef(self) -> ElementRef:
        return self._wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self._elemntHtml)
            )
        )

    def __saveSchedule(self) -> None:
        element: ElementRef = self.__getElementRef()

        element.send_keys(self._search)
        element.send_keys(Keys.RETURN)

        if envVar.ELEMENT_COOKIE_BANNER:
            elements = self._driver.find_elements(By.CLASS_NAME, envVar.ELEMENT_COOKIE_BANNER) 
            if len(elements) != 0:
                self._driver.execute_script(f"document.getElementsByClassName('{envVar.ELEMENT_COOKIE_BANNER}')[0].remove();")

        t.sleep(self._timeoutForTakePicture)

        if envVar.ELEMENT_TO_SCREENSHOT:
            espace_edt = self._driver.find_element(By.CLASS_NAME, envVar.ELEMENT_TO_SCREENSHOT)
            espace_edt.screenshot(self._pathToSavePictureOfSchedule)
        else:
            self._driver.save_screenshot(self._pathToSavePictureOfSchedule)

        self._driver.save_screenshot(self._pathToSavePictureOfSchedule)

        self._driver.quit()

    def runDriver(self) -> None:
        self.__setService()
        self.__setDriver()
        self.__openWebPage()
        self.__setWebDriverWait()
        self.__saveSchedule()