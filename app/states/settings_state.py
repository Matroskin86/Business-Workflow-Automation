import reflex as rx


class SettingsState(rx.State):
    """State for application settings."""

    email_notifications: bool = True
    push_notifications: bool = True
    weekly_digest: bool = False
    auto_save_workflows: bool = True
    default_approval_timeout: int = 48
    require_2fa_for_signing: bool = True
    theme_mode: str = "light"
    compact_mode: bool = False

    @rx.event
    def toggle_setting(self, setting_key: str):
        current = getattr(self, setting_key)
        setattr(self, setting_key, not current)
        return rx.toast(f"Setting updated")

    @rx.event
    def set_timeout(self, value: str):
        try:
            self.default_approval_timeout = int(value)
        except ValueError as e:
            import logging

            logging.exception(f"Error: {e}")