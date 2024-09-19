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
from singleton import singleton

# Types
type Driver = webdriver.Firefox
type DriverWait = WebDriverWait
type ElementRef = WebElement

@singleton
class Driver[T]:
    # Attributs
    _driver: Driver
    _wait: DriverWait
    _service: Service

    # Static
    _timeoutForLoadElement: ClassVar[int] = 10
    _timeoutForTakePicture: ClassVar[int] = 5
    _pathToSavePictureOfSchedule: ClassVar[str] = 'screenshot.png'

    def __init__(self, driverPathExecutable: T, url: T, elemntHtml: T, search: T) -> None:
        self._driverPathExecutable = driverPathExecutable
        self._url = url
        self._elemntHtml = elemntHtml
        self._search = search

    def __setService(self) -> None:
        # Créez l'objet Service ici
        self._service = Service(executable_path=self._driverPathExecutable)

    def __setDriver(self) -> Driver:
        # Configurez les options de Firefox si nécessaire
        options = Options()
        # Créez l'instance du driver en passant l'objet Service
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

        t.sleep(self._timeoutForTakePicture)

        self._driver.save_screenshot(self._pathToSavePictureOfSchedule)

        self._driver.quit()

    def runDriver(self) -> None:
        self.__setService()
        self.__setDriver()
        self.__openWebPage()
        self.__setWebDriverWait()
        self.__saveSchedule()