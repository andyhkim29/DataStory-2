from pathlib import Path

from nbclient import NotebookClient
from nbformat import read


def test_notebook_executes_from_clean_kernel(project_root: Path):
    notebook_path = project_root / "notebook.ipynb"
    with notebook_path.open(encoding="utf-8") as handle:
        notebook = read(handle, as_version=4)
    client = NotebookClient(notebook, timeout=120, kernel_name="python3")
    client.execute()

