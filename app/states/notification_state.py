import reflex as rx
from typing import TypedDict
from datetime import datetime


class Notification(TypedDict):
    id: str
    type: str
    title: str
    message: str
    time: str
    read: bool
    priority: str


class NotificationState(rx.State):
    """State for managing notifications."""

    notifications: list[Notification] = [
        {
            "id": "1",
            "type": "success",
            "title": "Contract Signed",
            "message": "Acme Corp Service Agreement was signed by Alice Chen.",
            "time": "2 mins ago",
            "read": False,
            "priority": "high",
        },
        {
            "id": "2",
            "type": "info",
            "title": "Workflow Completed",
            "message": "New Client Onboarding workflow finished successfully.",
            "time": "1 hour ago",
            "read": False,
            "priority": "normal",
        },
        {
            "id": "3",
            "type": "warning",
            "title": "Review Required",
            "message": "Budget Approval #402 is pending your review.",
            "time": "3 hours ago",
            "read": True,
            "priority": "high",
        },
        {
            "id": "4",
            "type": "info",
            "title": "Document Shared",
            "message": "Mike Ross shared 'Q3 Financials' with you.",
            "time": "5 hours ago",
            "read": True,
            "priority": "normal",
        },
        {
            "id": "5",
            "type": "info",
            "title": "System Update",
            "message": "FlowSync will undergo maintenance tonight at 2 AM.",
            "time": "1 day ago",
            "read": True,
            "priority": "low",
        },
    ]
    filter_type: str = "all"

    @rx.var
    def filtered_notifications(self) -> list[Notification]:
        if self.filter_type == "all":
            return self.notifications
        elif self.filter_type == "unread":
            return [n for n in self.notifications if not n["read"]]
        return self.notifications

    @rx.var
    def unread_count(self) -> int:
        return len([n for n in self.notifications if not n["read"]])

    @rx.event
    def mark_as_read(self, notification_id: str):
        new_list = []
        for n in self.notifications:
            if n["id"] == notification_id:
                n["read"] = True
            new_list.append(n)
        self.notifications = new_list

    @rx.event
    def mark_all_read(self):
        new_list = []
        for n in self.notifications:
            n["read"] = True
            new_list.append(n)
        self.notifications = new_list
        return rx.toast("All notifications marked as read")

    @rx.event
    def clear_all(self):
        self.notifications = []
        return rx.toast("All notifications cleared")

    @rx.event
    def set_filter(self, type_filter: str):
        self.filter_type = type_filter