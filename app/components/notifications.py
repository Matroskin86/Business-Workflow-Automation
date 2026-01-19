import reflex as rx
from app.states.notification_state import NotificationState, Notification


def notification_badge(priority: str) -> rx.Component:
    return rx.match(
        priority,
        (
            "high",
            rx.el.span(
                "High Priority",
                class_name="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-red-100 text-red-800",
            ),
        ),
        (
            "low",
            rx.el.span(
                "Low Priority",
                class_name="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-gray-100 text-gray-800",
            ),
        ),
        rx.el.span(
            "Normal",
            class_name="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-blue-100 text-blue-800",
        ),
    )


def notification_item(notification: Notification) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.match(
                    notification["type"],
                    (
                        "success",
                        rx.icon(
                            "circle_check_big", class_name="text-emerald-500", size=20
                        ),
                    ),
                    (
                        "warning",
                        rx.icon("trending_down", class_name="text-amber-500", size=20),
                    ),
                    ("info", rx.icon("info", class_name="text-blue-500", size=20)),
                    rx.icon("bell", class_name="text-gray-500", size=20),
                ),
                class_name=rx.cond(
                    notification["read"],
                    "h-10 w-10 rounded-full bg-gray-100 flex items-center justify-center shrink-0 opacity-50",
                    "h-10 w-10 rounded-full bg-white border border-gray-200 shadow-sm flex items-center justify-center shrink-0",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h4(
                        notification["title"],
                        class_name=rx.cond(
                            notification["read"],
                            "text-sm font-medium text-gray-600",
                            "text-sm font-bold text-gray-900",
                        ),
                    ),
                    notification_badge(notification["priority"]),
                    class_name="flex items-center justify-between mb-1",
                ),
                rx.el.p(
                    notification["message"], class_name="text-sm text-gray-600 mb-2"
                ),
                rx.el.p(notification["time"], class_name="text-xs text-gray-400"),
                class_name="flex-1 ml-4",
            ),
            class_name="flex items-start",
        ),
        rx.cond(
            ~notification["read"],
            rx.el.button(
                rx.icon("check", size=16),
                on_click=lambda: NotificationState.mark_as_read(notification["id"]),
                class_name="absolute top-4 right-4 p-1.5 text-gray-400 hover:text-emerald-600 hover:bg-emerald-50 rounded-full transition-colors",
                title="Mark as read",
            ),
        ),
        class_name=rx.cond(
            notification["read"],
            "relative p-4 rounded-xl border border-transparent bg-gray-50 hover:bg-gray-100 transition-colors mb-3",
            "relative p-4 rounded-xl border border-indigo-100 bg-indigo-50/50 hover:bg-indigo-50 transition-colors mb-3 shadow-sm",
        ),
    )


def notifications_list() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    "All",
                    on_click=lambda: NotificationState.set_filter("all"),
                    class_name=rx.cond(
                        NotificationState.filter_type == "all",
                        "px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg mr-2",
                        "px-4 py-2 text-sm font-medium text-gray-600 hover:bg-gray-100 rounded-lg mr-2",
                    ),
                ),
                rx.el.button(
                    "Unread",
                    on_click=lambda: NotificationState.set_filter("unread"),
                    class_name=rx.cond(
                        NotificationState.filter_type == "unread",
                        "px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg",
                        "px-4 py-2 text-sm font-medium text-gray-600 hover:bg-gray-100 rounded-lg",
                    ),
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.el.button(
                    "Mark all read",
                    on_click=NotificationState.mark_all_read,
                    class_name="text-sm font-medium text-indigo-600 hover:text-indigo-800 mr-4",
                ),
                rx.el.button(
                    "Clear all",
                    on_click=NotificationState.clear_all,
                    class_name="text-sm font-medium text-gray-500 hover:text-gray-700",
                ),
                class_name="flex items-center",
            ),
            class_name="flex items-center justify-between mb-6",
        ),
        rx.cond(
            NotificationState.filtered_notifications.length() > 0,
            rx.el.div(
                rx.foreach(NotificationState.filtered_notifications, notification_item)
            ),
            rx.el.div(
                rx.icon("bell-off", size=48, class_name="text-gray-300 mb-4"),
                rx.el.p("No notifications", class_name="text-gray-500 font-medium"),
                class_name="flex flex-col items-center justify-center py-12 bg-white rounded-xl border border-gray-100 border-dashed",
            ),
        ),
        class_name="max-w-3xl mx-auto",
    )