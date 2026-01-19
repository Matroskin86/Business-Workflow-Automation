import reflex as rx
from app.components.sidebar import page_layout
from app.components.audit_log import audit_table
from app.components.activity_timeline import activity_timeline
from app.states.audit_state import AuditState


def audit_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Audit Logs", class_name="text-2xl font-bold text-gray-900"),
            rx.el.p(
                "Track system security and user activities",
                class_name="text-sm text-gray-500 mt-1",
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.div(audit_table(), class_name="col-span-1 lg:col-span-3"),
            rx.el.div(activity_timeline(), class_name="col-span-1 lg:col-span-1"),
            class_name="grid grid-cols-1 lg:grid-cols-4 gap-6",
        ),
        class_name="p-8 max-w-7xl mx-auto min-h-full",
    )


def audit_page() -> rx.Component:
    return page_layout(audit_content())