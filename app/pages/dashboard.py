import reflex as rx
from app.components.sidebar import page_layout
from app.components.stats_cards import stats_grid, recent_activity_list
from app.components.dashboard_widgets import (
    throughput_chart,
    pending_tasks_widget,
    quick_actions_widget,
)
from app.states.dashboard_state import DashboardState


def dashboard_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Good Morning, Alex 👋", class_name="text-2xl font-bold text-gray-900"
            ),
            rx.el.p(
                f"Here's what's happening on {DashboardState.current_date}",
                class_name="text-sm text-gray-500 mt-1",
            ),
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("search", size=18, class_name="text-gray-500"),
                class_name="p-2.5 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors shadow-sm",
            ),
            rx.el.button(
                rx.icon("bell", size=18, class_name="text-gray-500"),
                class_name="p-2.5 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors shadow-sm relative",
            ),
            rx.el.button(
                rx.icon("plus", size=18, class_name="mr-2"),
                "New Workflow",
                class_name="flex items-center px-4 py-2.5 bg-indigo-600 text-white text-sm font-medium rounded-lg hover:bg-indigo-700 shadow-md hover:shadow-lg transition-all",
            ),
            class_name="flex items-center gap-3",
        ),
        class_name="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8",
    )


def dashboard_content() -> rx.Component:
    return rx.el.div(
        dashboard_header(),
        stats_grid(),
        rx.el.div(
            rx.el.div(
                throughput_chart(), class_name="col-span-1 lg:col-span-2 order-1 h-fit"
            ),
            rx.el.div(
                recent_activity_list(),
                class_name="col-span-1 lg:col-span-1 lg:row-span-2 order-2 lg:order-2 h-full",
            ),
            rx.el.div(
                pending_tasks_widget(),
                class_name="col-span-1 lg:col-span-1 order-3 lg:order-3 h-full",
            ),
            rx.el.div(
                quick_actions_widget(),
                class_name="col-span-1 lg:col-span-1 order-4 lg:order-4 h-full",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        class_name="p-4 md:p-8 max-w-7xl mx-auto pb-20",
    )


def dashboard_page() -> rx.Component:
    return page_layout(dashboard_content())