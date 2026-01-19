import reflex as rx
from app.states.team_state import TeamState, TeamMember


def team_member_row(member: TeamMember) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/7.x/initials/svg?seed={member['email']}",
                    class_name="h-10 w-10 rounded-full bg-indigo-100 mr-3",
                ),
                rx.el.div(
                    rx.el.p(
                        member["name"], class_name="text-sm font-semibold text-gray-900"
                    ),
                    rx.el.p(member["email"], class_name="text-xs text-gray-500"),
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(
                member["role"],
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-50 text-indigo-700 border border-indigo-100",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.match(
                member["status"],
                (
                    "Active",
                    rx.el.span(
                        "Active",
                        class_name="text-xs font-medium text-emerald-600 bg-emerald-50 px-2 py-1 rounded-full",
                    ),
                ),
                (
                    "Pending",
                    rx.el.span(
                        "Pending",
                        class_name="text-xs font-medium text-amber-600 bg-amber-50 px-2 py-1 rounded-full",
                    ),
                ),
                rx.el.span(
                    "Inactive",
                    class_name="text-xs font-medium text-gray-600 bg-gray-100 px-2 py-1 rounded-full",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(member["last_active"], class_name="text-sm text-gray-500"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon("trash-2", size=16),
                on_click=lambda: TeamState.remove_member(member["id"]),
                class_name="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors",
                title="Remove member",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right",
        ),
        class_name="hover:bg-gray-50 transition-colors border-b border-gray-100 last:border-0",
    )


def invite_modal() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Invite New Member", class_name="text-lg font-bold text-gray-900 mb-4"
        ),
        rx.el.div(
            rx.el.label(
                "Email Address",
                class_name="block text-sm font-medium text-gray-700 mb-1",
            ),
            rx.el.input(
                placeholder="colleague@company.com",
                on_change=TeamState.set_invite_email,
                class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500",
                default_value=TeamState.invite_email,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Role", class_name="block text-sm font-medium text-gray-700 mb-1"
            ),
            rx.el.select(
                rx.el.option("Admin", value="Admin"),
                rx.el.option("Editor", value="Editor"),
                rx.el.option("Viewer", value="Viewer"),
                value=TeamState.invite_role,
                on_change=TeamState.set_invite_role,
                class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500",
            ),
            class_name="mb-6",
        ),
        rx.el.button(
            rx.cond(
                TeamState.is_inviting,
                rx.spinner(size="1", class_name="mr-2"),
                rx.icon("mail", size=16, class_name="mr-2"),
            ),
            "Send Invitation",
            on_click=TeamState.invite_member,
            disabled=TeamState.is_inviting,
            class_name="w-full flex items-center justify-center px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 font-medium transition-colors disabled:opacity-50",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm h-fit",
    )


def team_list() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "Member",
                        class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                    ),
                    rx.el.th(
                        "Role",
                        class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                    ),
                    rx.el.th(
                        "Status",
                        class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                    ),
                    rx.el.th(
                        "Last Active",
                        class_name="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                    ),
                    rx.el.th("", class_name="px-6 py-3 relative"),
                ),
                class_name="bg-gray-50 border-b border-gray-200",
            ),
            rx.el.tbody(
                rx.foreach(TeamState.members, team_member_row),
                class_name="bg-white divide-y divide-gray-100",
            ),
            class_name="min-w-full divide-y divide-gray-200",
        ),
        class_name="overflow-x-auto rounded-xl border border-gray-200 shadow-sm bg-white",
    )