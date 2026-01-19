import reflex as rx
from app.states.document_state import DocumentState, Document


def status_badge(status: str) -> rx.Component:
    return rx.match(
        status,
        (
            "Signed",
            rx.el.span(
                status,
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800",
            ),
        ),
        (
            "Published",
            rx.el.span(
                status,
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800",
            ),
        ),
        (
            "Review",
            rx.el.span(
                status,
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-100 text-amber-800",
            ),
        ),
        (
            "Draft",
            rx.el.span(
                status,
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800",
            ),
        ),
        rx.el.span(
            status,
            class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800",
        ),
    )


def document_row(doc: Document) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.icon("file-text", class_name="text-indigo-500 shrink-0", size=20),
                rx.el.div(
                    rx.el.p(
                        doc["name"], class_name="text-sm font-medium text-gray-900"
                    ),
                    rx.el.p(
                        f"{doc['type']} • {doc['size']}",
                        class_name="text-xs text-gray-500 md:hidden",
                    ),
                    class_name="ml-3",
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            status_badge(doc["status"]),
            class_name="px-6 py-4 whitespace-nowrap hidden sm:table-cell",
        ),
        rx.el.td(
            rx.el.span(doc["type"], class_name="text-sm text-gray-500"),
            class_name="px-6 py-4 whitespace-nowrap hidden md:table-cell",
        ),
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/7.x/initials/svg?seed={doc['owner']}",
                    class_name="h-6 w-6 rounded-full bg-gray-200 mr-2",
                ),
                rx.el.span(doc["owner"], class_name="text-sm text-gray-500"),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap hidden lg:table-cell",
        ),
        rx.el.td(
            rx.el.span(doc["modified"], class_name="text-sm text-gray-500"),
            class_name="px-6 py-4 whitespace-nowrap hidden xl:table-cell",
        ),
        rx.el.td(
            rx.el.button(
                "View",
                on_click=lambda: DocumentState.select_document(doc["id"]),
                class_name="text-indigo-600 hover:text-indigo-900 text-sm font-medium",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right",
        ),
        class_name="hover:bg-gray-50 transition-colors border-b border-gray-100 last:border-0",
    )


def document_list() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("search", class_name="text-gray-400 ml-3", size=18),
                    rx.el.input(
                        placeholder="Search documents...",
                        on_change=DocumentState.set_search,
                        class_name="w-full border-none focus:ring-0 text-sm text-gray-700 placeholder-gray-400 bg-transparent py-2.5 px-3",
                    ),
                    class_name="flex items-center bg-gray-100 rounded-lg w-full md:w-80",
                )
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("filter", size=18, class_name="mr-2"),
                    "Filter",
                    class_name="flex items-center px-4 py-2 bg-white border border-gray-200 text-gray-700 rounded-lg hover:bg-gray-50 text-sm font-medium transition-colors",
                ),
                rx.upload.root(
                    rx.el.button(
                        rx.cond(
                            DocumentState.is_uploading,
                            rx.spinner(size="1"),
                            rx.icon("cloud_sun", size=18, class_name="mr-2"),
                        ),
                        "Upload",
                        class_name="flex items-center px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 text-sm font-medium transition-colors shadow-sm ml-3",
                    ),
                    id="upload1",
                    on_drop=DocumentState.handle_upload(
                        rx.upload_files(upload_id="upload1")
                    ),
                    class_name="flex",
                ),
                class_name="flex items-center mt-4 md:mt-0",
            ),
            class_name="flex flex-col md:flex-row justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Name",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider hidden sm:table-cell",
                        ),
                        rx.el.th(
                            "Type",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider hidden md:table-cell",
                        ),
                        rx.el.th(
                            "Owner",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider hidden lg:table-cell",
                        ),
                        rx.el.th(
                            "Last Modified",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider hidden xl:table-cell",
                        ),
                        rx.el.th("", class_name="px-6 py-3 relative"),
                    ),
                    class_name="bg-gray-50 border-b border-gray-200",
                ),
                rx.el.tbody(
                    rx.foreach(DocumentState.filtered_documents, document_row),
                    class_name="bg-white divide-y divide-gray-100",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="overflow-x-auto rounded-xl border border-gray-200 shadow-sm bg-white",
        ),
    )