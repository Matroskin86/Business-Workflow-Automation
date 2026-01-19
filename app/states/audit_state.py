import reflex as rx
from typing import TypedDict
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


class AuditLog(TypedDict):
    id: str
    user: str
    action: str
    target: str
    timestamp: str
    ip: str
    status: str


class AuditState(rx.State):
    """State for audit logs and activity timeline."""

    logs: list[AuditLog] = []
    filter_action: str = ""
    filter_user: str = ""

    @rx.event
    def ensure_data(self):
        """Generate mock data if list is empty"""
        if not self.logs:
            actions = [
                "Login",
                "View Document",
                "Sign Contract",
                "Update Workflow",
                "Delete File",
                "Share Document",
                "Export Data",
            ]
            statuses = ["Success", "Success", "Success", "Failed", "Warning"]
            generated_logs = []
            for i in range(20):
                dt = datetime.now() - timedelta(hours=random.randint(0, 48))
                generated_logs.append(
                    {
                        "id": fake.uuid4(),
                        "user": fake.name(),
                        "action": random.choice(actions),
                        "target": f"Doc-{random.randint(100, 999)}"
                        if random.random() > 0.5
                        else "System",
                        "timestamp": dt.strftime("%Y-%m-%d %H:%M:%S"),
                        "ip": fake.ipv4(),
                        "status": random.choice(statuses),
                    }
                )
            generated_logs.sort(key=lambda x: x["timestamp"], reverse=True)
            self.logs = generated_logs

    @rx.var
    def filtered_logs(self) -> list[AuditLog]:
        logs = self.logs
        if self.filter_action:
            logs = [
                l for l in logs if self.filter_action.lower() in l["action"].lower()
            ]
        if self.filter_user:
            logs = [l for l in logs if self.filter_user.lower() in l["user"].lower()]
        return logs

    @rx.event
    def set_action_filter(self, value: str):
        self.filter_action = value

    @rx.event
    def set_user_filter(self, value: str):
        self.filter_user = value

    @rx.event
    def export_logs(self):
        return rx.toast("Audit logs exported to CSV")