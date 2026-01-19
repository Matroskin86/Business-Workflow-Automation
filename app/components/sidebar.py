import reflex as rx


def sidebar_item(icon: str, text: str, href: str, active: bool = False) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(
                icon,
                class_name=rx.cond(active, "text-indigo-600", "text-gray-500"),
                size=20,
            ),
            rx.el.span(
                text,
                class_name=rx.cond(
                    active,
                    "font-semibold text-indigo-900",
                    "font-medium text-gray-600 group-hover:text-gray-900",
                ),
            ),
            class_name=rx.cond(
                active,
                "flex items-center gap-3 px-3 py-2.5 rounded-lg bg-indigo-50 transition-colors w-full",
                "flex items-center gap-3 px-3 py-2.5 rounded-lg hover:bg-gray-50 transition-colors w-full group",
            ),
        ),
        href=href,
        class_name="w-full",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("layers", class_name="text-white", size=24),
                    class_name="h-10 w-10 bg-gradient-to-br from-indigo-600 to-violet-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-200",
                ),
                rx.el.span(
                    "FlowSync",
                    class_name="text-xl font-bold text-gray-900 tracking-tight",
                ),
                class_name="flex items-center gap-3 px-2 mb-8",
            ),
            rx.el.nav(
                rx.el.div(
                    rx.el.p(
                        "MAIN",
                        class_name="text-xs font-semibold text-gray-400 mb-2 px-3 tracking-wider",
                    ),
                    rx.el.div(
                        sidebar_item("layout-dashboard", "Dashboard", "/"),
                        sidebar_item("files", "Documents", "/documents"),
                        sidebar_item("git-branch", "Workflows", "/workflows"),
                        class_name="space-y-1",
                    ),
                    class_name="mb-8",
                ),
                rx.el.div(
                    rx.el.p(
                        "WORKSPACE",
                        class_name="text-xs font-semibold text-gray-400 mb-2 px-3 tracking-wider",
                    ),
                    rx.el.div(
                        sidebar_item("bell", "Notifications", "/notifications"),
                        sidebar_item("history", "Audit Logs", "/audit"),
                        sidebar_item("users", "Team", "/team"),
                        class_name="space-y-1",
                    ),
                ),
                class_name="flex flex-col flex-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src="https://api.dicebear.com/7.x/notionists/svg?seed=Felix",
                        class_name="h-9 w-9 rounded-full bg-gray-100",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Alex Morgan",
                            class_name="text-sm font-semibold text-gray-900",
                        ),
                        rx.el.p("Admin Workspace", class_name="text-xs text-gray-500"),
                        class_name="flex flex-col",
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.icon("settings", class_name="text-gray-500", size=18),
                        class_name="p-2 hover:bg-gray-100 rounded-lg transition-colors",
                    ),
                    href="/settings",
                ),
                class_name="mt-auto border-t border-gray-100 pt-4 flex items-center justify-between",
            ),
            class_name="flex flex-col h-full px-4 py-6",
        ),
        class_name="w-64 h-screen bg-white border-r border-gray-200 shrink-0 hidden md:block sticky top-0",
    )


def page_layout(content: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            content, class_name="flex-1 min-w-0 bg-gray-50 h-screen overflow-y-auto"
        ),
        class_name="flex h-screen w-full font-['Inter']",
    )