import reflex as rx
from app.states.document_state import DocumentState


def step_indicator(label: str, status: str, is_last: bool = False) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.cond(
                    status == "completed",
                    rx.icon("check", size=14, class_name="text-white"),
                    rx.cond(
                        status == "current",
                        rx.el.div(class_name="h-2 w-2 bg-white rounded-full"),
                        rx.el.div(class_name="text-xs font-medium text-gray-500"),
                    ),
                ),
                class_name=rx.cond(
                    status == "completed",
                    "h-6 w-6 rounded-full bg-emerald-500 flex items-center justify-center ring-4 ring-white shrink-0 z-10",
                    rx.cond(
                        status == "current",
                        "h-6 w-6 rounded-full bg-indigo-600 flex items-center justify-center ring-4 ring-indigo-100 shrink-0 z-10",
                        "h-6 w-6 rounded-full bg-gray-200 border-2 border-white ring-2 ring-gray-100 shrink-0 z-10",
                    ),
                ),
            ),
            rx.cond(
                ~is_last,
                rx.el.div(
                    class_name=rx.cond(
                        status == "completed",
                        "absolute top-3 left-6 w-full h-0.5 bg-emerald-500",
                        "absolute top-3 left-6 w-full h-0.5 bg-gray-200",
                    )
                ),
            ),
            class_name="relative flex items-center justify-center w-full",
        ),
        rx.el.p(
            label,
            class_name=rx.cond(
                status == "current",
                "text-xs font-semibold text-indigo-700 mt-2 text-center",
                rx.cond(
                    status == "completed",
                    "text-xs font-medium text-emerald-600 mt-2 text-center",
                    "text-xs font-medium text-gray-400 mt-2 text-center",
                ),
            ),
        ),
        class_name="flex flex-col items-center flex-1",
    )


def signing_workflow() -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            "Contract Workflow Status",
            class_name="text-sm font-semibold text-gray-900 mb-6 uppercase tracking-wider",
        ),
        rx.el.div(
            rx.cond(
                DocumentState.selected_document["is_signed"],
                rx.fragment(
                    step_indicator("Draft Created", "completed"),
                    step_indicator("Legal Review", "completed"),
                    step_indicator("Sent to Client", "completed"),
                    step_indicator("Signed", "completed", is_last=True),
                ),
                rx.fragment(
                    step_indicator("Draft Created", "completed"),
                    step_indicator("Legal Review", "completed"),
                    step_indicator("Sent to Client", "current"),
                    step_indicator("Signed", "upcoming", is_last=True),
                ),
            ),
            class_name="flex justify-between w-full mb-8 px-4",
        ),
        rx.cond(
            ~DocumentState.selected_document["is_signed"],
            rx.el.div(
                rx.el.div(
                    rx.icon("cigarette", class_name="text-amber-500", size=20),
                    rx.el.div(
                        rx.el.p(
                            "Action Required",
                            class_name="text-sm font-semibold text-amber-800",
                        ),
                        rx.el.p(
                            "This document requires your digital signature to proceed.",
                            class_name="text-xs text-amber-700 mt-0.5",
                        ),
                        class_name="ml-3",
                    ),
                    class_name="flex items-start bg-amber-50 border border-amber-200 rounded-lg p-3 mb-4",
                ),
                rx.el.button(
                    rx.icon("pen-tool", size=18, class_name="mr-2"),
                    "Sign Document Now",
                    on_click=DocumentState.sign_document,
                    class_name="w-full flex items-center justify-center py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg font-medium transition-colors shadow-sm",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("circle_check_big", class_name="text-emerald-500", size=20),
                    rx.el.div(
                        rx.el.p(
                            "Workflow Complete",
                            class_name="text-sm font-semibold text-emerald-800",
                        ),
                        rx.el.p(
                            "This contract has been fully executed and archived.",
                            class_name="text-xs text-emerald-700 mt-0.5",
                        ),
                        class_name="ml-3",
                    ),
                    class_name="flex items-start bg-emerald-50 border border-emerald-200 rounded-lg p-3",
                )
            ),
        ),
        class_name="bg-white rounded-xl border border-gray-200 p-6 shadow-sm mt-6",
    )