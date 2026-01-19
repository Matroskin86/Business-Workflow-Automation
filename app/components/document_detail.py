import reflex as rx
from app.states.document_state import DocumentState, Document
from app.components.contract_signing import signing_workflow


def property_row(label: str, value: str) -> rx.Component:
    return rx.el.div(
        rx.el.span(label, class_name="text-sm text-gray-500 w-24 shrink-0"),
        rx.el.span(value, class_name="text-sm font-medium text-gray-900 truncate"),
        class_name="flex items-center py-2 border-b border-gray-100 last:border-0",
    )


def document_detail_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    DocumentState.selected_document["name"],
                    class_name="text-xl font-bold text-gray-900 mb-1",
                ),
                rx.el.p(
                    DocumentState.selected_document["description"],
                    class_name="text-sm text-gray-500",
                ),
            ),
            rx.el.button(
                rx.icon("x", size=20),
                on_click=DocumentState.clear_selection,
                class_name="p-2 hover:bg-gray-100 rounded-lg text-gray-500 transition-colors",
            ),
            class_name="flex justify-between items-start mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("file-text", size=48, class_name="text-gray-300 mb-4"),
                        rx.el.p(
                            "Document Preview", class_name="text-gray-400 font-medium"
                        ),
                        class_name="aspect-[3/4] bg-gray-50 rounded-lg border-2 border-dashed border-gray-200 flex flex-col items-center justify-center mb-6",
                    ),
                    rx.el.h3(
                        "Document Details",
                        class_name="text-sm font-bold text-gray-900 mb-3 uppercase tracking-wide",
                    ),
                    rx.el.div(
                        property_row("Type", DocumentState.selected_document["type"]),
                        property_row("Size", DocumentState.selected_document["size"]),
                        property_row("Owner", DocumentState.selected_document["owner"]),
                        property_row(
                            "Modified", DocumentState.selected_document["modified"]
                        ),
                        property_row(
                            "Version", DocumentState.selected_document["version"]
                        ),
                        class_name="bg-white rounded-xl border border-gray-200 px-4 py-2",
                    ),
                ),
                class_name="col-span-1 lg:col-span-2",
            ),
            rx.el.div(
                rx.cond(
                    DocumentState.is_contract,
                    signing_workflow(),
                    rx.el.div(
                        rx.el.h3(
                            "Actions",
                            class_name="text-sm font-bold text-gray-900 mb-3 uppercase tracking-wide",
                        ),
                        rx.el.div(
                            rx.el.button(
                                rx.icon("share-2", size=16, class_name="mr-2"),
                                "Share Document",
                                class_name="w-full flex items-center justify-center py-2 bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 rounded-lg font-medium text-sm transition-colors mb-2",
                            ),
                            rx.el.button(
                                rx.icon("download", size=16, class_name="mr-2"),
                                "Download",
                                class_name="w-full flex items-center justify-center py-2 bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 rounded-lg font-medium text-sm transition-colors",
                            ),
                            class_name="bg-white rounded-xl border border-gray-200 p-4",
                        ),
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Version History",
                        class_name="text-sm font-bold text-gray-900 mb-3 mt-6 uppercase tracking-wide",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                class_name="h-2 w-2 rounded-full bg-indigo-500 mt-1.5"
                            ),
                            rx.el.div(
                                rx.el.p(
                                    f"Version {DocumentState.selected_document['version']}",
                                    class_name="text-sm font-medium text-gray-900",
                                ),
                                rx.el.p(
                                    "Current version",
                                    class_name="text-xs text-gray-500",
                                ),
                                class_name="ml-3",
                            ),
                            class_name="flex items-start mb-3",
                        ),
                        rx.el.div(
                            rx.el.div(
                                class_name="h-2 w-2 rounded-full bg-gray-300 mt-1.5"
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Version 0.9",
                                    class_name="text-sm font-medium text-gray-500",
                                ),
                                rx.el.p(
                                    "Initial draft", class_name="text-xs text-gray-400"
                                ),
                                class_name="ml-3",
                            ),
                            class_name="flex items-start",
                        ),
                        class_name="bg-white rounded-xl border border-gray-200 p-4",
                    ),
                ),
                class_name="col-span-1 lg:col-span-1",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        class_name="h-full overflow-y-auto p-1",
    )