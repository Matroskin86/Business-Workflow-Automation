import reflex as rx
from app.components.sidebar import page_layout
from app.components.document_list import document_list
from app.components.document_detail import document_detail_view
from app.states.document_state import DocumentState


def documents_content() -> rx.Component:
    return rx.el.div(
        rx.cond(
            DocumentState.selected_doc_id != "",
            rx.el.div(
                rx.el.button(
                    "← Back to Documents",
                    on_click=DocumentState.clear_selection,
                    class_name="text-sm font-medium text-gray-500 hover:text-gray-900 mb-4 inline-block",
                ),
                document_detail_view(),
                class_name="animate-in fade-in slide-in-from-right-4 duration-300",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Documents", class_name="text-2xl font-bold text-gray-900"
                    ),
                    rx.el.p(
                        "Manage and sign your contracts and files",
                        class_name="text-sm text-gray-500 mt-1",
                    ),
                    class_name="mb-8",
                ),
                document_list(),
                class_name="animate-in fade-in duration-300",
            ),
        ),
        class_name="p-8 max-w-7xl mx-auto min-h-full",
    )


def documents_page() -> rx.Component:
    return page_layout(documents_content())