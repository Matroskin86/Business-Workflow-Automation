import reflex as rx
from app.components.sidebar import page_layout
from app.states.workflow_state import WorkflowState, Workflow
from app.components.workflow_builder import workflow_builder


def workflow_card(wf: Workflow) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("git-branch", class_name="text-indigo-600", size=24),
                class_name="h-12 w-12 rounded-xl bg-indigo-50 flex items-center justify-center mb-4",
            ),
            rx.el.div(
                rx.el.span(
                    wf["status"],
                    class_name=rx.cond(
                        wf["status"] == "Active",
                        "px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800",
                        "px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800",
                    ),
                )
            ),
            class_name="flex justify-between items-start",
        ),
        rx.el.h3(wf["name"], class_name="text-lg font-bold text-gray-900 mb-1"),
        rx.el.p(
            wf["description"], class_name="text-sm text-gray-500 mb-4 line-clamp-2 h-10"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Success Rate",
                    class_name="text-xs text-gray-400 uppercase tracking-wide",
                ),
                rx.el.p(
                    wf["success_rate"], class_name="text-sm font-semibold text-gray-900"
                ),
            ),
            rx.el.div(
                rx.el.span(
                    "Total Runs",
                    class_name="text-xs text-gray-400 uppercase tracking-wide",
                ),
                rx.el.p(wf["runs"], class_name="text-sm font-semibold text-gray-900"),
            ),
            rx.el.div(
                rx.el.span(
                    "Last Run",
                    class_name="text-xs text-gray-400 uppercase tracking-wide",
                ),
                rx.el.p(
                    wf["last_run"], class_name="text-sm font-semibold text-gray-900"
                ),
            ),
            class_name="grid grid-cols-3 gap-2 border-t border-gray-100 pt-4 mb-4",
        ),
        rx.el.button(
            "Edit Workflow",
            on_click=lambda: WorkflowState.edit_workflow(wf["id"]),
            class_name="w-full py-2 bg-white border border-gray-200 text-gray-700 hover:text-indigo-600 hover:border-indigo-200 rounded-lg text-sm font-medium transition-colors",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow",
    )


def workflows_list() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1("Workflows", class_name="text-2xl font-bold text-gray-900"),
                rx.el.p(
                    "Automate your business processes",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("plus", size=18, class_name="mr-2"),
                "Create Workflow",
                on_click=WorkflowState.create_workflow,
                class_name="flex items-center px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 text-sm font-medium transition-colors shadow-sm",
            ),
            class_name="flex justify-between items-center mb-8",
        ),
        rx.el.div(
            rx.foreach(WorkflowState.workflows, workflow_card),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
        ),
        class_name="p-8 max-w-7xl mx-auto min-h-full",
    )


def workflows_page() -> rx.Component:
    return page_layout(
        rx.cond(WorkflowState.is_editing, workflow_builder(), workflows_list())
    )