import reflex as rx
from typing import TypedDict
import datetime
from faker import Faker

fake = Faker()


class Document(TypedDict):
    id: str
    name: str
    type: str
    status: str
    owner: str
    modified: str
    size: str
    version: str
    is_signed: bool
    description: str


class DocumentState(rx.State):
    """State for document management and contract workflows."""

    documents: list[Document] = [
        {
            "id": "doc_001",
            "name": "Service Agreement - Acme Corp",
            "type": "Contract",
            "status": "Pending Signature",
            "owner": "Alice Chen",
            "modified": "2024-05-10",
            "size": "2.4 MB",
            "version": "1.2",
            "is_signed": False,
            "description": "Standard service agreement for Q3 deliverables.",
        },
        {
            "id": "doc_002",
            "name": "Q2 Marketing Strategy",
            "type": "Presentation",
            "status": "Draft",
            "owner": "Bob Jones",
            "modified": "2024-05-09",
            "size": "15.8 MB",
            "version": "0.5",
            "is_signed": False,
            "description": "Draft slides for the upcoming board meeting.",
        },
        {
            "id": "doc_003",
            "name": "Employee Handbook 2024",
            "type": "PDF",
            "status": "Published",
            "owner": "HR Dept",
            "modified": "2024-01-15",
            "size": "4.1 MB",
            "version": "2.0",
            "is_signed": False,
            "description": "Updated policies and procedures for all staff.",
        },
        {
            "id": "doc_004",
            "name": "NDA - Vendor X",
            "type": "Contract",
            "status": "Signed",
            "owner": "Legal Team",
            "modified": "2024-04-20",
            "size": "1.2 MB",
            "version": "1.0",
            "is_signed": True,
            "description": "Non-disclosure agreement for new vendor partnership.",
        },
        {
            "id": "doc_005",
            "name": "Project Alpha Budget",
            "type": "Spreadsheet",
            "status": "Review",
            "owner": "Finance",
            "modified": "2024-05-11",
            "size": "850 KB",
            "version": "3.1",
            "is_signed": False,
            "description": "Preliminary budget allocation for Project Alpha.",
        },
    ]
    search_query: str = ""
    selected_doc_id: str = ""
    is_uploading: bool = False

    @rx.var
    def filtered_documents(self) -> list[Document]:
        """Filter documents based on search query."""
        if not self.search_query:
            return self.documents
        query = self.search_query.lower()
        return [
            doc
            for doc in self.documents
            if query in doc["name"].lower() or query in doc["owner"].lower()
        ]

    @rx.var
    def selected_document(self) -> Document:
        """Return the currently selected document object or a default empty one."""
        for doc in self.documents:
            if doc["id"] == self.selected_doc_id:
                return doc
        return {
            "id": "",
            "name": "",
            "type": "",
            "status": "",
            "owner": "",
            "modified": "",
            "size": "",
            "version": "",
            "is_signed": False,
            "description": "",
        }

    @rx.var
    def is_contract(self) -> bool:
        """Check if selected document is a contract."""
        return self.selected_document["type"] == "Contract"

    @rx.event
    def select_document(self, doc_id: str):
        self.selected_doc_id = doc_id

    @rx.event
    def clear_selection(self):
        self.selected_doc_id = ""

    @rx.event
    def set_search(self, query: str):
        self.search_query = query

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle file upload simulation."""
        self.is_uploading = True
        import asyncio

        await asyncio.sleep(1.5)
        for file in files:
            upload_data = await file.read()
            new_doc: Document = {
                "id": f"doc_{random.randint(1000, 9999)}",
                "name": file.filename,
                "type": "File",
                "status": "Draft",
                "owner": "You",
                "modified": datetime.date.today().isoformat(),
                "size": f"{len(upload_data) / 1024:.1f} KB",
                "version": "1.0",
                "is_signed": False,
                "description": "Newly uploaded file.",
            }
            self.documents.insert(0, new_doc)
        self.is_uploading = False
        return rx.toast("File uploaded successfully")

    @rx.event
    def sign_document(self):
        """Simulate signing the current document."""
        new_docs = []
        for doc in self.documents:
            if doc["id"] == self.selected_doc_id:
                doc["status"] = "Signed"
                doc["is_signed"] = True
                new_docs.append(doc)
            else:
                new_docs.append(doc)
        self.documents = new_docs
        return rx.toast("Contract signed successfully!")