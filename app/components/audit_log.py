import reflex as rx
from app.states.audit_state import AuditState, AuditLog


def audit_row(log: AuditLog) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.span(
                    log["timestamp"], class_name="text-sm text-gray-900 font-medium"
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/7.x/initials/svg?seed={log['user']}",
                    class_name="h-6 w-6 rounded-full bg-gray-200 mr-2",
                ),
                rx.el.span(log["user"], class_name="text-sm text-gray-700"),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(
                log["action"],
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(log["target"], class_name="text-sm text-indigo-600 font-mono"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(log["ip"], class_name="text-sm text-gray-500 font-mono"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.match(
                log["status"],
                (
                    "Success",
                    rx.icon("circle_check_big", class_name="text-emerald-500", size=16),
                ),
                (
                    "Failed",
                    rx.icon("message_circle_reply", class_name="text-red-500", size=16),
                ),
                rx.icon("cigarette", class_name="text-amber-500", size=16),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-center",
        ),
        class_name="hover:bg-gray-50 transition-colors border-b border-gray-100 last:border-0",
    )


def audit_table() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("search", class_name="text-gray-400 ml-3", size=18),
                rx.el.input(
                    placeholder="Filter by user...",
                    on_change=AuditState.set_user_filter,
                    class_name="w-full border-none focus:ring-0 text-sm text-gray-700 placeholder-gray-400 bg-transparent py-2.5 px-3",
                ),
                class_name="flex items-center bg-gray-100 rounded-lg w-full md:w-64 mr-4",
            ),
            rx.el.div(
                rx.icon("filter", class_name="text-gray-400 ml-3", size=18),
                rx.el.input(
                    placeholder="Filter by action...",
                    on_change=AuditState.set_action_filter,
                    class_name="w-full border-none focus:ring-0 text-sm text-gray-700 placeholder-gray-400 bg-transparent py-2.5 px-3",
                ),
                class_name="flex items-center bg-gray-100 rounded-lg w-full md:w-64",
            ),
            rx.el.button(
                rx.icon("download", size=18, class_name="mr-2"),
                "Export CSV",
                on_click=AuditState.export_logs,
                class_name="flex items-center px-4 py-2 bg-white border border-gray-200 text-gray-700 rounded-lg hover:bg-gray-50 text-sm font-medium transition-colors ml-auto",
            ),
            class_name="flex flex-col md:flex-row items-center mb-6 gap-4",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Timestamp",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "User",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Action",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Target",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "IP Address",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-center text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50 border-b border-gray-200",
                ),
                rx.el.tbody(
                    rx.foreach(AuditState.filtered_logs, audit_row),
                    class_name="bg-white divide-y divide-gray-100",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="overflow-x-auto rounded-xl border border-gray-200 shadow-sm bg-white",
        ),
    )