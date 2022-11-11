import pytest

from PytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def editprofile(self, dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[2])
        # print(dataload)
        # print(dataload[0])

