from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class EndpointDeleted(Waiter):
    def wait(self, EndpointName: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class EndpointInService(Waiter):
    def wait(self, EndpointName: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class NotebookInstanceDeleted(Waiter):
    def wait(self, NotebookInstanceName: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class NotebookInstanceInService(Waiter):
    def wait(self, NotebookInstanceName: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class NotebookInstanceStopped(Waiter):
    def wait(self, NotebookInstanceName: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class TrainingJobCompletedOrStopped(Waiter):
    def wait(self, TrainingJobName: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class TransformJobCompletedOrStopped(Waiter):
    def wait(self, TransformJobName: str, WaiterConfig: Dict = None) -> NoReturn:
        pass
