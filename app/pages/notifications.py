import reflex as rx
from app.components.sidebar import page_layout
from app.components.notifications import notifications_list


def notifications_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Notifications", class_name="text-2xl font-bold text-gray-900"),
            rx.el.p(
                "Stay updated with system alerts and activities",
                class_name="text-sm text-gray-500 mt-1",
            ),
            class_name="mb-8",
        ),
        notifications_list(),
        class_name="p-8 max-w-7xl mx-auto min-h-full",
    )


def notifications_page() -> rx.Component:
    return page_layout(notifications_content())