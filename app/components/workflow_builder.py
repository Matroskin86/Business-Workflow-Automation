import reflex as rx
import reflex_enterprise as rxe
from app.states.workflow_state import WorkflowState


def toolbox_button(label: str, icon: str, color: str, type_label: str) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, size=16, class_name=f"{color} mr-2"),
        rx.el.span(label, class_name="text-sm font-medium text-gray-700"),
        on_click=lambda: WorkflowState.add_node(type_label),
        class_name="flex items-center w-full px-3 py-2 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 hover:border-gray-300 transition-all shadow-sm mb-2 text-left",
    )


def workflow_builder() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    WorkflowState.active_workflow["name"],
                    class_name="text-lg font-bold text-gray-900",
                ),
                rx.el.span(
                    WorkflowState.active_workflow["status"],
                    class_name="ml-3 px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-700 text-xs font-semibold",
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.cond(
                    WorkflowState.is_running,
                    rx.el.div(
                        rx.spinner(size="2", class_name="text-indigo-600 mr-2"),
                        rx.el.span(
                            "Running...",
                            class_name="text-sm font-medium text-indigo-600",
                        ),
                        class_name="flex items-center mr-4 bg-indigo-50 px-3 py-1.5 rounded-lg",
                    ),
                ),
                rx.el.button(
                    rx.icon("play", size=16, class_name="mr-2"),
                    "Run Test",
                    disabled=WorkflowState.is_running,
                    on_click=WorkflowState.run_simulation,
                    class_name="flex items-center px-3 py-1.5 bg-emerald-600 text-white text-sm font-medium rounded-lg hover:bg-emerald-700 disabled:opacity-50 disabled:cursor-not-allowed mr-2 transition-colors",
                ),
                rx.el.button(
                    rx.icon("save", size=16, class_name="mr-2"),
                    "Save",
                    on_click=WorkflowState.save_workflow,
                    class_name="flex items-center px-3 py-1.5 bg-indigo-600 text-white text-sm font-medium rounded-lg hover:bg-indigo-700 mr-2 transition-colors",
                ),
                rx.el.button(
                    rx.icon("x", size=16),
                    on_click=WorkflowState.close_editor,
                    class_name="p-1.5 hover:bg-gray-100 rounded-lg text-gray-500 transition-colors",
                ),
                class_name="flex items-center",
            ),
            class_name="h-14 border-b border-gray-200 bg-white px-4 flex items-center justify-between shrink-0 z-10 relative",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "TOOLBOX",
                    class_name="text-xs font-bold text-gray-400 mb-4 tracking-wider",
                ),
                toolbox_button("Add Trigger", "zap", "text-emerald-500", "Trigger"),
                toolbox_button("Add Action", "activity", "text-blue-500", "Action"),
                toolbox_button(
                    "Add Condition", "git-branch", "text-amber-500", "Condition"
                ),
                rx.el.div(class_name="h-px bg-gray-200 my-4"),
                rx.el.p(
                    "EXECUTION LOG",
                    class_name="text-xs font-bold text-gray-400 mb-2 tracking-wider",
                ),
                rx.el.div(
                    rx.foreach(
                        WorkflowState.execution_log,
                        lambda log: rx.el.div(
                            log,
                            class_name="text-xs text-gray-600 font-mono mb-1 border-b border-gray-100 pb-1 last:border-0",
                        ),
                    ),
                    class_name="bg-gray-50 rounded-lg p-2 h-48 overflow-y-auto border border-gray-200",
                ),
                class_name="w-64 border-r border-gray-200 bg-white p-4 flex flex-col shrink-0 z-10",
            ),
            rx.el.div(
                rxe.flow(
                    rxe.flow.background(),
                    rxe.flow.controls(),
                    rxe.flow.mini_map(),
                    nodes=WorkflowState.active_nodes,
                    edges=WorkflowState.active_edges,
                    on_nodes_change=lambda changes: WorkflowState.set_nodes(
                        rxe.flow.util.apply_node_changes(
                            WorkflowState.active_nodes, changes
                        )
                    ),
                    on_edges_change=lambda changes: WorkflowState.set_edges(
                        rxe.flow.util.apply_edge_changes(
                            WorkflowState.active_edges, changes
                        )
                    ),
                    on_connect=WorkflowState.on_connect,
                    fit_view=True,
                    fit_view_options={"padding": 0.2},
                ),
                class_name="flex-1 h-full bg-gray-50",
            ),
            class_name="flex-1 flex min-h-0",
        ),
        class_name="flex flex-col h-full w-full absolute inset-0 bg-white z-50",
    )