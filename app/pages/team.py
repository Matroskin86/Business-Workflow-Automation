import reflex as rx
from app.components.sidebar import page_layout
from app.components.team_management import team_list, invite_modal


def team_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Team Management", class_name="text-2xl font-bold text-gray-900"),
            rx.el.p(
                "Manage workspace members and permissions",
                class_name="text-sm text-gray-500 mt-1",
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.div(team_list(), class_name="col-span-1 lg:col-span-2"),
            rx.el.div(invite_modal(), class_name="col-span-1"),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        class_name="p-8 max-w-7xl mx-auto min-h-full",
    )


def team_page() -> rx.Component:
    return page_layout(team_content())