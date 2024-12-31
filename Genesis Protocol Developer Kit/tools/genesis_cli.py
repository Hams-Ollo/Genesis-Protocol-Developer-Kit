#!/usr/bin/env python3
"""
Genesis Protocol CLI

A command-line interface for managing Genesis Protocol operations.
"""

import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from typing import Optional, List

# Import Genesis Protocol tools
from .project_profiler import ProjectProfiler
from .tech_stack_manager import TechStackManager
from .import_docs import DocumentationImporter

app = typer.Typer(help="Genesis Protocol CLI - Project Management Tool")
console = Console()

@app.command()
def init(
    name: str = typer.Option(..., prompt=True, help="Project name"),
    path: Path = typer.Option(
        Path.cwd(), help="Project path", file_okay=False, dir_okay=True
    ),
):
    """Initialize a new project using Genesis Protocol."""
    console.print(f"\n🚀 Initializing project: {name}\n", style="bold blue")
    
    # Run project profiler
    profiler = ProjectProfiler()
    profile = profiler.start_profiling()
    
    # Initialize project
    from initialize_project import ProjectInitializer
    initializer = ProjectInitializer()
    initializer.initialize_project()
    
    console.print("\n✨ Project initialized successfully!\n", style="bold green")

@app.command()
def tech_stack(
    action: str = typer.Option(..., help="Action to perform: add/update/list"),
    component: Optional[str] = typer.Option(None, help="Component name"),
):
    """Manage project tech stack."""
    manager = TechStackManager()
    
    if action == "add":
        manager.add_component()
    elif action == "list":
        # Display tech stack components
        table = Table(title="Tech Stack Components")
        table.add_column("Category", style="cyan")
        table.add_column("Components", style="green")
        
        config = manager.load_config()
        for category, components in config["tech_stack"].items():
            table.add_row(category, ", ".join(components))
        
        console.print(table)

@app.command()
def docs(
    action: str = typer.Option(..., help="Action to perform: import/update/generate"),
    source: Optional[Path] = typer.Option(None, help="Source directory for import"),
):
    """Manage project documentation."""
    if action == "import":
        importer = DocumentationImporter()
        importer.run()
    elif action == "generate":
        # Generate project documentation
        console.print("Generating documentation...", style="bold blue")
        # Add documentation generation logic

@app.command()
def validate(
    checks: Optional[List[str]] = typer.Option(
        None, help="Specific checks to run: lint/test/security/all"
    ),
):
    """Validate project against Genesis Protocol standards."""
    console.print("\n🔍 Running validation checks...\n", style="bold blue")
    
    if not checks:
        checks = ["all"]
    
    if "all" in checks or "lint" in checks:
        # Run linting
        console.print("Running linting checks...", style="yellow")
        # Add linting logic
    
    if "all" in checks or "test" in checks:
        # Run tests
        console.print("Running tests...", style="yellow")
        # Add testing logic
    
    if "all" in checks or "security" in checks:
        # Run security checks
        console.print("Running security checks...", style="yellow")
        # Add security check logic

@app.command()
def deploy(
    environment: str = typer.Option(..., help="Deployment environment: dev/staging/prod"),
    dry_run: bool = typer.Option(False, help="Perform a dry run"),
):
    """Deploy project using Genesis Protocol standards."""
    console.print(f"\n🚀 Deploying to {environment}...\n", style="bold blue")
    
    if dry_run:
        console.print("Performing dry run...", style="yellow")
        # Add dry run logic
    else:
        # Add deployment logic
        pass

@app.command()
def status():
    """Show project status and compliance with Genesis Protocol."""
    console.print("\n📊 Project Status\n", style="bold blue")
    
    table = Table(title="Genesis Protocol Compliance")
    table.add_column("Category", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Details", style="yellow")
    
    # Add status checks and display
    table.add_row("Documentation", "✅", "Complete")
    table.add_row("Tests", "✅", "Passing")
    table.add_row("Security", "⚠️", "2 warnings")
    
    console.print(table)

if __name__ == "__main__":
    app() 