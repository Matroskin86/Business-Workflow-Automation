import reflex as rx
from app.states.audit_state import AuditState, AuditLog


def timeline_item(log: AuditLog, is_last: bool = False) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.match(
                    log["status"],
                    ("Success", rx.icon("check", size=14, class_name="text-white")),
                    ("Failed", rx.icon("x", size=14, class_name="text-white")),
                    rx.icon("info", size=14, class_name="text-white"),
                ),
                class_name=rx.cond(
                    log["status"] == "Success",
                    "h-6 w-6 rounded-full bg-emerald-500 flex items-center justify-center ring-4 ring-white shrink-0 z-10",
                    rx.cond(
                        log["status"] == "Failed",
                        "h-6 w-6 rounded-full bg-red-500 flex items-center justify-center ring-4 ring-white shrink-0 z-10",
                        "h-6 w-6 rounded-full bg-blue-500 flex items-center justify-center ring-4 ring-white shrink-0 z-10",
                    ),
                ),
            ),
            rx.cond(
                ~is_last,
                rx.el.div(
                    class_name="absolute top-6 left-3 w-0.5 h-full bg-gray-200 -z-10"
                ),
            ),
            class_name="relative mr-4 flex flex-col items-center",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    rx.el.span(log["user"], class_name="font-semibold text-gray-900"),
                    " ",
                    rx.el.span(log["action"], class_name="text-gray-600"),
                    " ",
                    rx.el.span(log["target"], class_name="font-medium text-indigo-600"),
                    class_name="text-sm",
                ),
                rx.el.span(
                    log["timestamp"],
                    class_name="text-xs text-gray-400 ml-auto whitespace-nowrap",
                ),
                class_name="flex justify-between items-start w-full",
            ),
            rx.el.p(f"IP: {log['ip']}", class_name="text-xs text-gray-400 mt-1"),
            class_name="bg-white p-3 rounded-lg border border-gray-100 shadow-sm w-full",
        ),
        class_name="flex items-start pb-6 w-full",
    )


def activity_timeline() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Activity Timeline", class_name="text-lg font-bold text-gray-900 mb-6"
        ),
        rx.el.div(
            rx.foreach(
                AuditState.filtered_logs,
                lambda log, index: timeline_item(
                    log, is_last=index == AuditState.filtered_logs.length() - 1
                ),
            ),
            class_name="pl-2",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
    )