import reflex as rx
from typing import TypedDict
from faker import Faker

fake = Faker()


class TeamMember(TypedDict):
    id: str
    name: str
    email: str
    role: str
    status: str
    last_active: str


class TeamState(rx.State):
    """State for team management."""

    members: list[TeamMember] = [
        {
            "id": "tm_1",
            "name": "Alex Morgan",
            "email": "alex.morgan@company.com",
            "role": "Admin",
            "status": "Active",
            "last_active": "Now",
        },
        {
            "id": "tm_2",
            "name": "Sarah Conner",
            "email": "sarah.c@company.com",
            "role": "Editor",
            "status": "Active",
            "last_active": "2 hours ago",
        },
        {
            "id": "tm_3",
            "name": "John Smith",
            "email": "j.smith@company.com",
            "role": "Viewer",
            "status": "Inactive",
            "last_active": "5 days ago",
        },
        {
            "id": "tm_4",
            "name": "Mike Ross",
            "email": "mike.ross@company.com",
            "role": "Editor",
            "status": "Active",
            "last_active": "1 day ago",
        },
    ]
    invite_email: str = ""
    invite_role: str = "Viewer"
    is_inviting: bool = False

    @rx.event
    def set_invite_email(self, email: str):
        self.invite_email = email

    @rx.event
    def set_invite_role(self, role: str):
        self.invite_role = role

    @rx.event
    def invite_member(self):
        if not self.invite_email:
            return rx.toast("Please enter an email address")
        self.is_inviting = True
        new_member: TeamMember = {
            "id": f"tm_{len(self.members) + 1}",
            "name": self.invite_email.split("@")[0].title(),
            "email": self.invite_email,
            "role": self.invite_role,
            "status": "Pending",
            "last_active": "-",
        }
        self.members.append(new_member)
        self.invite_email = ""
        self.is_inviting = False
        return rx.toast(f"Invitation sent to {new_member['email']}")

    @rx.event
    def remove_member(self, member_id: str):
        self.members = [m for m in self.members if m["id"] != member_id]
        return rx.toast("Team member removed")

    @rx.event
    def change_role(self, member_id: str, new_role: str):
        new_list = []
        for m in self.members:
            if m["id"] == member_id:
                m["role"] = new_role
            new_list.append(m)
        self.members = new_list
        return rx.toast("Role updated")