from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class JobComplete(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None) -> NoReturn:
        pass
