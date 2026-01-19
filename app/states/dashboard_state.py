import reflex as rx
from typing import TypedDict
import random
from datetime import datetime


class StatCard(TypedDict):
    label: str
    value: str
    change: str
    trend: str
    icon: str
    color: str
    bg_gradient: str


class Activity(TypedDict):
    id: int
    user: str
    action: str
    target: str
    time: str
    icon: str


class PendingTask(TypedDict):
    id: str
    title: str
    due: str
    priority: str


class ThroughputData(TypedDict):
    name: str
    completed: int
    failed: int


class DashboardState(rx.State):
    """State for the main dashboard overview."""

    current_date: str = datetime.now().strftime("%A, %d %B %Y")
    stats: list[StatCard] = [
        {
            "label": "Active Workflows",
            "value": "12",
            "change": "+2 this week",
            "trend": "up",
            "icon": "git-branch",
            "color": "text-blue-600",
            "bg_gradient": "from-blue-50 to-indigo-50",
        },
        {
            "label": "Pending Contracts",
            "value": "5",
            "change": "Action needed",
            "trend": "down",
            "icon": "file-signature",
            "color": "text-amber-600",
            "bg_gradient": "from-amber-50 to-orange-50",
        },
        {
            "label": "Total Documents",
            "value": "1,248",
            "change": "+18% vs last month",
            "trend": "up",
            "icon": "files",
            "color": "text-emerald-600",
            "bg_gradient": "from-emerald-50 to-teal-50",
        },
        {
            "label": "Notifications",
            "value": "8",
            "change": "3 urgent",
            "trend": "up",
            "icon": "bell",
            "color": "text-indigo-600",
            "bg_gradient": "from-indigo-50 to-violet-50",
        },
    ]
    recent_activities: list[Activity] = [
        {
            "id": 1,
            "user": "Sarah Conner",
            "action": "signed",
            "target": "NDA Agreement - Cyberdyne",
            "time": "2 mins ago",
            "icon": "pen-tool",
        },
        {
            "id": 2,
            "user": "John Smith",
            "action": "uploaded",
            "target": "Q3 Financial Report",
            "time": "1 hour ago",
            "icon": "upload",
        },
        {
            "id": 3,
            "user": "System",
            "action": "completed",
            "target": "New Hire Onboarding",
            "time": "3 hours ago",
            "icon": "check-circle",
        },
        {
            "id": 4,
            "user": "Mike Ross",
            "action": "commented on",
            "target": "Merger Proposal v2",
            "time": "5 hours ago",
            "icon": "message-square",
        },
    ]
    pending_tasks: list[PendingTask] = [
        {
            "id": "1",
            "title": "Review Service Agreement",
            "due": "Today",
            "priority": "High",
        },
        {
            "id": "2",
            "title": "Approve Budget Q3",
            "due": "Tomorrow",
            "priority": "Medium",
        },
        {
            "id": "3",
            "title": "Sign NDA - Vendor X",
            "due": "Oct 24",
            "priority": "High",
        },
        {
            "id": "4",
            "title": "Update Workflow Triggers",
            "due": "Oct 25",
            "priority": "Low",
        },
    ]
    throughput_data: list[ThroughputData] = [
        {"name": "Mon", "completed": 45, "failed": 2},
        {"name": "Tue", "completed": 52, "failed": 1},
        {"name": "Wed", "completed": 38, "failed": 4},
        {"name": "Thu", "completed": 65, "failed": 0},
        {"name": "Fri", "completed": 48, "failed": 2},
        {"name": "Sat", "completed": 15, "failed": 0},
        {"name": "Sun", "completed": 10, "failed": 0},
    ]

    @rx.event
    def refresh_stats(self):
        """Simulate fetching new data."""
        pass