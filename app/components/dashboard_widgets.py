import reflex as rx
from app.states.dashboard_state import DashboardState, PendingTask


def throughput_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Workflow Throughput", class_name="text-lg font-bold text-gray-900"
            ),
            rx.el.select(
                rx.el.option("Last 7 days"),
                rx.el.option("Last 30 days"),
                class_name="text-xs border-none bg-gray-50 rounded-lg text-gray-600 focus:ring-0 cursor-pointer",
            ),
            class_name="flex items-center justify-between mb-6",
        ),
        rx.recharts.responsive_container(
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(
                    stroke_dasharray="3 3", vertical=False, stroke="#f3f4f6"
                ),
                rx.recharts.x_axis(
                    data_key="name",
                    axis_line=False,
                    tick_line=False,
                    tick={"fontSize": 12, "fill": "#9ca3af"},
                    dy=10,
                ),
                rx.recharts.y_axis(
                    axis_line=False,
                    tick_line=False,
                    tick={"fontSize": 12, "fill": "#9ca3af"},
                ),
                rx.recharts.tooltip(
                    content_style={
                        "borderRadius": "8px",
                        "border": "none",
                        "boxShadow": "0 4px 6px -1px rgb(0 0 0 / 0.1)",
                    }
                ),
                rx.recharts.bar(
                    data_key="completed",
                    name="Completed",
                    fill="#4f46e5",
                    radius=[4, 4, 0, 0],
                    bar_size=16,
                    stack_id="a",
                ),
                rx.recharts.bar(
                    data_key="failed",
                    name="Failed",
                    fill="#fca5a5",
                    radius=[4, 4, 0, 0],
                    bar_size=16,
                    stack_id="a",
                ),
                data=DashboardState.throughput_data,
            ),
            height=300,
            width="100%",
        ),
        class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 h-full",
    )


def task_item(task: PendingTask) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.input(
                type="checkbox",
                class_name="rounded text-indigo-600 focus:ring-indigo-500 border-gray-300 h-4 w-4",
            ),
            rx.el.div(
                rx.el.p(task["title"], class_name="font-medium text-sm text-gray-900"),
                rx.el.p(
                    f"Due {task['due']}", class_name="text-xs text-gray-500 mt-0.5"
                ),
                class_name="ml-3",
            ),
            class_name="flex items-center",
        ),
        rx.el.span(
            task["priority"],
            class_name=rx.cond(
                task["priority"] == "High",
                "bg-red-50 text-red-700 text-[10px] uppercase font-bold px-2 py-1 rounded-full tracking-wide",
                rx.cond(
                    task["priority"] == "Medium",
                    "bg-amber-50 text-amber-700 text-[10px] uppercase font-bold px-2 py-1 rounded-full tracking-wide",
                    "bg-blue-50 text-blue-700 text-[10px] uppercase font-bold px-2 py-1 rounded-full tracking-wide",
                ),
            ),
        ),
        class_name="flex justify-between items-center py-3 border-b border-gray-50 last:border-0 hover:bg-gray-50/50 px-2 -mx-2 rounded-lg transition-colors cursor-pointer group",
    )


def pending_tasks_widget() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3("Pending Tasks", class_name="text-lg font-bold text-gray-900"),
            rx.el.button(
                rx.icon("plus", size=16, class_name="text-gray-500"),
                class_name="p-1 hover:bg-gray-100 rounded-lg transition-colors",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.div(
            rx.foreach(DashboardState.pending_tasks, task_item),
            class_name="flex flex-col",
        ),
        class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 h-full",
    )


def quick_link_btn(icon: str, label: str, color: str) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.icon(icon, size=20, class_name=f"{color} mb-2"),
            rx.el.span(label, class_name="text-xs font-semibold text-gray-700"),
            class_name="flex flex-col items-center",
        ),
        class_name="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl hover:bg-white hover:shadow-md hover:scale-105 transition-all duration-200 border border-transparent hover:border-gray-100",
    )


def quick_actions_widget() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Quick Actions", class_name="text-lg font-bold text-gray-900 mb-4"),
        rx.el.div(
            quick_link_btn("file-plus", "New Doc", "text-blue-600"),
            quick_link_btn("git-branch-plus", "Workflow", "text-indigo-600"),
            quick_link_btn("user-plus", "Invite", "text-emerald-600"),
            quick_link_btn("settings", "Settings", "text-gray-600"),
            class_name="grid grid-cols-2 lg:grid-cols-4 gap-3",
        ),
        class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 h-full",
    )