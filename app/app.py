import reflex as rx
import reflex_enterprise as rxe
from app.pages.dashboard import dashboard_page
from app.pages.documents import documents_page
from app.pages.workflows import workflows_page
from app.pages.notifications import notifications_page
from app.pages.audit_logs import audit_page
from app.pages.team import team_page
from app.pages.settings import settings_page
from app.states.audit_state import AuditState

app = rxe.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    ],
    head_components=[rx.el.link(rel="icon", href="/favicon.ico")],
)
app.add_page(dashboard_page, route="/", title="Dashboard | FlowSync")
app.add_page(documents_page, route="/documents", title="Documents | FlowSync")
app.add_page(workflows_page, route="/workflows", title="Workflows | FlowSync")
app.add_page(
    notifications_page, route="/notifications", title="Notifications | FlowSync"
)
app.add_page(
    audit_page,
    route="/audit",
    title="Audit Logs | FlowSync",
    on_load=AuditState.ensure_data,
)
app.add_page(team_page, route="/team", title="Team | FlowSync")
app.add_page(settings_page, route="/settings", title="Settings | FlowSync")