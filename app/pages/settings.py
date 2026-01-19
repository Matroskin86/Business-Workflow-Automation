import reflex as rx
from app.components.sidebar import page_layout
from app.components.settings_form import settings_view


def settings_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Settings", class_name="text-2xl font-bold text-gray-900"),
            rx.el.p(
                "Manage application preferences and account details",
                class_name="text-sm text-gray-500 mt-1",
            ),
            class_name="mb-8",
        ),
        settings_view(),
        class_name="p-8 max-w-7xl mx-auto min-h-full",
    )


def settings_page() -> rx.Component:
    return page_layout(settings_content())