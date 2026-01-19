import reflex as rx
from app.states.settings_state import SettingsState


def toggle_setting(label: str, description: str, key: str, value: bool) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(label, class_name="text-sm font-medium text-gray-900"),
            rx.el.p(description, class_name="text-xs text-gray-500"),
        ),
        rx.el.button(
            rx.el.div(
                class_name=rx.cond(
                    value,
                    "h-4 w-4 rounded-full bg-white shadow-sm transform translate-x-3.5 transition-transform",
                    "h-4 w-4 rounded-full bg-white shadow-sm transform translate-x-0.5 transition-transform",
                )
            ),
            on_click=lambda: SettingsState.toggle_setting(key),
            class_name=rx.cond(
                value,
                "h-5 w-9 rounded-full bg-indigo-600 transition-colors",
                "h-5 w-9 rounded-full bg-gray-300 transition-colors",
            ),
        ),
        class_name="flex items-center justify-between py-4 border-b border-gray-100 last:border-0",
    )


def section_header(title: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, size=20, class_name="text-indigo-600 mr-2"),
        rx.el.h3(title, class_name="text-lg font-bold text-gray-900"),
        class_name="flex items-center mb-6",
    )


def settings_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                section_header("Notifications", "bell"),
                toggle_setting(
                    "Email Notifications",
                    "Receive updates via email",
                    "email_notifications",
                    SettingsState.email_notifications,
                ),
                toggle_setting(
                    "Push Notifications",
                    "Receive in-app notifications",
                    "push_notifications",
                    SettingsState.push_notifications,
                ),
                toggle_setting(
                    "Weekly Digest",
                    "Receive a summary of activity every Monday",
                    "weekly_digest",
                    SettingsState.weekly_digest,
                ),
                class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm mb-6",
            ),
            rx.el.div(
                section_header("Workflow Defaults", "git-branch"),
                toggle_setting(
                    "Auto-save Workflows",
                    "Save changes automatically while editing",
                    "auto_save_workflows",
                    SettingsState.auto_save_workflows,
                ),
                toggle_setting(
                    "Require 2FA for Signing",
                    "Enforce two-factor auth for contract signatures",
                    "require_2fa_for_signing",
                    SettingsState.require_2fa_for_signing,
                ),
                rx.el.div(
                    rx.el.label(
                        "Default Approval Timeout (hours)",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.input(
                        type="number",
                        on_change=SettingsState.set_timeout,
                        class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500",
                        default_value=SettingsState.default_approval_timeout,
                    ),
                    class_name="mt-4",
                ),
                class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm mb-6",
            ),
            class_name="col-span-1 lg:col-span-2",
        ),
        rx.el.div(
            rx.el.div(
                section_header("Account", "user"),
                rx.el.div(
                    rx.image(
                        src="https://api.dicebear.com/7.x/notionists/svg?seed=Felix",
                        class_name="h-20 w-20 rounded-full bg-gray-100 mx-auto mb-4",
                    ),
                    rx.el.h4(
                        "Alex Morgan", class_name="text-center font-bold text-gray-900"
                    ),
                    rx.el.p(
                        "Admin Workspace",
                        class_name="text-center text-sm text-gray-500 mb-6",
                    ),
                    rx.el.button(
                        "Edit Profile",
                        class_name="w-full py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 mb-2",
                    ),
                    rx.el.button(
                        "Change Password",
                        class_name="w-full py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50",
                    ),
                    class_name="flex flex-col",
                ),
                class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm mb-6",
            ),
            rx.el.div(
                section_header("Theme", "monitor"),
                toggle_setting(
                    "Compact Mode",
                    "Reduce spacing for higher data density",
                    "compact_mode",
                    SettingsState.compact_mode,
                ),
                rx.el.div(
                    rx.el.p(
                        "Theme Mode",
                        class_name="text-sm font-medium text-gray-900 mb-3",
                    ),
                    rx.el.div(
                        rx.el.button(
                            rx.icon("sun", size=20, class_name="mb-1 text-amber-500"),
                            "Light",
                            class_name="flex-1 flex flex-col items-center justify-center p-3 rounded-lg bg-indigo-50 border border-indigo-200 text-indigo-700",
                        ),
                        rx.el.button(
                            rx.icon("moon", size=20, class_name="mb-1 text-gray-400"),
                            "Dark",
                            class_name="flex-1 flex flex-col items-center justify-center p-3 rounded-lg border border-gray-200 text-gray-500 hover:bg-gray-50",
                        ),
                        class_name="flex gap-3",
                    ),
                    class_name="mt-4",
                ),
                class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
            ),
            class_name="col-span-1",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
    )