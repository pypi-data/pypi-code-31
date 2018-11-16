from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def delete_rule(self, Name: str):
        pass

    def describe_event_bus(self) -> Dict:
        pass

    def describe_rule(self, Name: str) -> Dict:
        pass

    def disable_rule(self, Name: str):
        pass

    def enable_rule(self, Name: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_rule_names_by_target(self, TargetArn: str, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def list_rules(self, NamePrefix: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def list_targets_by_rule(self, Rule: str, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def put_events(self, Entries: List) -> Dict:
        pass

    def put_permission(self, Action: str, Principal: str, StatementId: str, Condition: Dict = None):
        pass

    def put_rule(self, Name: str, ScheduleExpression: str = None, EventPattern: str = None, State: str = None, Description: str = None, RoleArn: str = None) -> Dict:
        pass

    def put_targets(self, Rule: str, Targets: List) -> Dict:
        pass

    def remove_permission(self, StatementId: str):
        pass

    def remove_targets(self, Rule: str, Ids: List) -> Dict:
        pass

    def test_event_pattern(self, EventPattern: str, Event: str) -> Dict:
        pass
