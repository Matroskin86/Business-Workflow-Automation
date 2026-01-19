import reflex as rx
from app.states.dashboard_state import DashboardState, StatCard


def stat_card(stat: StatCard) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(stat["icon"], size=24, class_name=stat["color"]),
                class_name="p-2.5 rounded-lg bg-white/60 backdrop-blur-sm shadow-sm",
            ),
            rx.el.div(
                rx.el.span(
                    rx.cond(stat["trend"] == "up", "↑", "↓"),
                    class_name=rx.cond(
                        stat["trend"] == "up",
                        "text-emerald-600 mr-1",
                        "text-red-500 mr-1",
                    ),
                ),
                rx.el.span(
                    stat["change"],
                    class_name=rx.cond(
                        stat["trend"] == "up",
                        "text-xs font-semibold text-emerald-700",
                        "text-xs font-semibold text-red-600",
                    ),
                ),
                class_name="flex items-center bg-white/50 px-2 py-1 rounded-full",
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.h3(stat["value"], class_name="text-3xl font-bold text-gray-900 mb-1"),
            rx.el.p(stat["label"], class_name="text-sm font-medium text-gray-600"),
        ),
        class_name=rx.cond(
            True,
            "bg-gradient-to-br "
            + stat["bg_gradient"]
            + " p-6 rounded-2xl border border-gray-100/50 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
            "",
        ),
    )


def stats_grid() -> rx.Component:
    return rx.el.div(
        rx.foreach(DashboardState.stats, stat_card),
        class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
    )


def activity_item(activity: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                class_name="w-0.5 h-full bg-gray-200 absolute left-4 top-10 -z-10"
            ),
            rx.el.div(
                rx.icon(activity["icon"], size=14, class_name="text-white"),
                class_name="h-8 w-8 rounded-full bg-indigo-500 flex items-center justify-center shrink-0 ring-4 ring-white shadow-sm",
            ),
            class_name="relative mr-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    rx.el.span(
                        activity["user"], class_name="font-semibold text-gray-900"
                    ),
                    " ",
                    rx.el.span(activity["action"], class_name="text-gray-600"),
                    class_name="text-sm text-gray-800",
                ),
                rx.el.span(
                    activity["time"],
                    class_name="text-xs text-gray-400 whitespace-nowrap ml-2",
                ),
                class_name="flex justify-between items-start w-full",
            ),
            rx.el.p(
                activity["target"],
                class_name="text-xs font-medium text-indigo-600 mt-0.5",
            ),
            class_name="flex-1 bg-gray-50/50 p-3 rounded-lg border border-gray-100 hover:bg-gray-50 transition-colors",
        ),
        class_name="flex items-start pb-6 last:pb-0",
    )


def recent_activity_list() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3("Recent Activity", class_name="text-lg font-bold text-gray-900"),
            rx.el.button(
                "View All",
                class_name="text-xs font-medium text-indigo-600 hover:text-indigo-800",
            ),
            class_name="flex items-center justify-between mb-6",
        ),
        rx.el.div(
            rx.foreach(DashboardState.recent_activities, activity_item),
            class_name="pl-1",
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm h-full",
    )