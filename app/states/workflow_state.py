import reflex as rx
import reflex_enterprise as rxe
from reflex_enterprise.components.flow.types import Edge, Node
from typing import TypedDict, Any
import random
from datetime import datetime


class Workflow(TypedDict):
    id: str
    name: str
    description: str
    status: str
    last_run: str
    nodes: list[Node]
    edges: list[Edge]
    runs: int
    success_rate: str


class WorkflowState(rx.State):
    """State for managing workflows and the flow builder."""

    active_nodes: list[Node] = []
    active_edges: list[Edge] = []
    active_workflow_id: str = ""
    is_editing: bool = False
    is_running: bool = False
    execution_log: list[str] = []
    workflows: list[Workflow] = [
        {
            "id": "wf_001",
            "name": "Contract Approval Pipeline",
            "description": "Automated review process for new service agreements.",
            "status": "Active",
            "last_run": "2 hours ago",
            "runs": 142,
            "success_rate": "98%",
            "nodes": [
                {
                    "id": "1",
                    "type": "input",
                    "data": {"label": "New Contract Uploaded"},
                    "position": {"x": 250, "y": 50},
                    "style": {
                        "background": "#ecfdf5",
                        "color": "#047857",
                        "border": "1px solid #10b981",
                    },
                },
                {
                    "id": "2",
                    "data": {"label": "Identify Value > $10k"},
                    "position": {"x": 250, "y": 150},
                    "style": {
                        "background": "#fffbeb",
                        "color": "#b45309",
                        "border": "1px solid #f59e0b",
                    },
                },
                {
                    "id": "3",
                    "data": {"label": "Legal Review Required"},
                    "position": {"x": 100, "y": 300},
                    "style": {
                        "background": "#eff6ff",
                        "color": "#1d4ed8",
                        "border": "1px solid #3b82f6",
                    },
                },
                {
                    "id": "4",
                    "data": {"label": "Auto-Approve"},
                    "position": {"x": 400, "y": 300},
                    "style": {
                        "background": "#eff6ff",
                        "color": "#1d4ed8",
                        "border": "1px solid #3b82f6",
                    },
                },
                {
                    "id": "5",
                    "type": "output",
                    "data": {"label": "Send for Signature"},
                    "position": {"x": 250, "y": 450},
                    "style": {
                        "background": "#f8fafc",
                        "color": "#475569",
                        "border": "1px solid #94a3b8",
                    },
                },
            ],
            "edges": [
                {"id": "e1-2", "source": "1", "target": "2", "animated": True},
                {"id": "e2-3", "source": "2", "target": "3", "label": "Yes"},
                {"id": "e2-4", "source": "2", "target": "4", "label": "No"},
                {"id": "e3-5", "source": "3", "target": "5"},
                {"id": "e4-5", "source": "4", "target": "5"},
            ],
        },
        {
            "id": "wf_002",
            "name": "New Client Onboarding",
            "description": "Sequence of emails and account creation tasks.",
            "status": "Paused",
            "last_run": "2 days ago",
            "runs": 45,
            "success_rate": "100%",
            "nodes": [
                {
                    "id": "1",
                    "type": "input",
                    "data": {"label": "Client Signed Up"},
                    "position": {"x": 250, "y": 50},
                    "style": {
                        "background": "#ecfdf5",
                        "color": "#047857",
                        "border": "1px solid #10b981",
                    },
                },
                {
                    "id": "2",
                    "data": {"label": "Send Welcome Email"},
                    "position": {"x": 250, "y": 150},
                    "style": {
                        "background": "#eff6ff",
                        "color": "#1d4ed8",
                        "border": "1px solid #3b82f6",
                    },
                },
                {
                    "id": "3",
                    "type": "output",
                    "data": {"label": "Create Slack Channel"},
                    "position": {"x": 250, "y": 250},
                    "style": {
                        "background": "#f8fafc",
                        "color": "#475569",
                        "border": "1px solid #94a3b8",
                    },
                },
            ],
            "edges": [
                {"id": "e1-2", "source": "1", "target": "2", "animated": True},
                {"id": "e2-3", "source": "2", "target": "3", "animated": True},
            ],
        },
    ]

    @rx.var
    def active_workflow(self) -> Workflow:
        for wf in self.workflows:
            if wf["id"] == self.active_workflow_id:
                return wf
        return {
            "id": "",
            "name": "Untitled",
            "description": "",
            "status": "Draft",
            "last_run": "-",
            "nodes": [],
            "edges": [],
            "runs": 0,
            "success_rate": "0%",
        }

    @rx.event
    def set_nodes(self, nodes: list[Node]):
        self.active_nodes = nodes

    @rx.event
    def set_edges(self, edges: list[Edge]):
        self.active_edges = edges

    @rx.event
    def on_connect(self, connection: dict):
        source = connection["source"]
        target = connection["target"]
        source_handle = connection.get("sourceHandle")
        target_handle = connection.get("targetHandle")
        new_id = f"e_{source}_{target}"
        if source_handle:
            new_id += f"_{source_handle}"
        if target_handle:
            new_id += f"_{target_handle}"
        new_edge: Edge = {
            "id": new_id,
            "source": source,
            "target": target,
            "sourceHandle": source_handle,
            "targetHandle": target_handle,
            "animated": True,
        }
        self.active_edges.append(new_edge)

    @rx.event
    def edit_workflow(self, wf_id: str):
        self.active_workflow_id = wf_id
        wf = next((w for w in self.workflows if w["id"] == wf_id), None)
        if wf:
            self.active_nodes = wf["nodes"]
            self.active_edges = wf["edges"]
        self.is_editing = True
        self.execution_log = []

    @rx.event
    def create_workflow(self):
        new_id = f"wf_{random.randint(1000, 9999)}"
        new_wf: Workflow = {
            "id": new_id,
            "name": "New Workflow",
            "description": "Draft workflow",
            "status": "Draft",
            "last_run": "Never",
            "runs": 0,
            "success_rate": "-",
            "nodes": [
                {
                    "id": "1",
                    "type": "input",
                    "data": {"label": "Start Trigger"},
                    "position": {"x": 250, "y": 50},
                    "style": {
                        "background": "#ecfdf5",
                        "color": "#047857",
                        "border": "1px solid #10b981",
                    },
                }
            ],
            "edges": [],
        }
        self.workflows.insert(0, new_wf)
        self.edit_workflow(new_id)

    @rx.event
    def save_workflow(self):
        new_workflows = []
        for wf in self.workflows:
            if wf["id"] == self.active_workflow_id:
                updated_wf = wf.copy()
                updated_wf["nodes"] = self.active_nodes
                updated_wf["edges"] = self.active_edges
                new_workflows.append(updated_wf)
            else:
                new_workflows.append(wf)
        self.workflows = new_workflows
        return rx.toast("Workflow saved successfully!")

    @rx.event
    def close_editor(self):
        self.is_editing = False
        self.active_workflow_id = ""

    @rx.event
    def add_node(self, type_label: str):
        new_id = str(len(self.active_nodes) + 1 + random.randint(100, 999))
        style = {}
        if type_label == "Trigger":
            style = {
                "background": "#ecfdf5",
                "color": "#047857",
                "border": "1px solid #10b981",
            }
            node_type = "input"
        elif type_label == "Condition":
            style = {
                "background": "#fffbeb",
                "color": "#b45309",
                "border": "1px solid #f59e0b",
            }
            node_type = "default"
        else:
            style = {
                "background": "#eff6ff",
                "color": "#1d4ed8",
                "border": "1px solid #3b82f6",
            }
            node_type = "default"
        new_node = {
            "id": new_id,
            "type": node_type,
            "data": {"label": f"New {type_label}"},
            "position": {
                "x": 250 + random.randint(-50, 50),
                "y": 250 + random.randint(-50, 50),
            },
            "style": style,
        }
        self.active_nodes.append(new_node)

    @rx.event
    async def run_simulation(self):
        self.is_running = True
        self.execution_log = []
        import asyncio

        self.execution_log.append(
            f"[{datetime.now().strftime('%H:%M:%S')}] Initializing workflow engine..."
        )
        yield
        await asyncio.sleep(0.8)
        self.execution_log.append(
            f"[{datetime.now().strftime('%H:%M:%S')}] Workflow '{self.active_workflow['name']}' started."
        )
        yield
        await asyncio.sleep(0.8)
        for node in self.active_nodes:
            self.execution_log.append(
                f"[{datetime.now().strftime('%H:%M:%S')}] Executing node: {node['data']['label']}..."
            )
            yield
            await asyncio.sleep(0.6)
            self.execution_log.append(
                f"[{datetime.now().strftime('%H:%M:%S')}] Node completed successfully."
            )
            yield
            await asyncio.sleep(0.2)
        self.execution_log.append(
            f"[{datetime.now().strftime('%H:%M:%S')}] Workflow completed successfully."
        )
        self.is_running = False
        yield