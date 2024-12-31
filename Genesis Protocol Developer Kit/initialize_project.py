#-------------------------------------------------------------------------------------#
# initialize_project.py
#-------------------------------------------------------------------------------------#
# SETUP:
#
# Setup venv and install the requirements
# 1. Create a virtual environment -> python -m venv venv
# 2. Activate the virtual environment -> .\venv\Scripts\Activate
# 3. Install the requirements -> pip install -r requirements.txt
# 4. Run the file -> python initialize_project.py
#
# Git Commands:
# 1. Initialize repository -> git init
# 2. Add files to staging -> git add .
# 3. Commit changes -> git commit -m "your message"
# 4. Create new branch -> git checkout -b branch-name
# 5. Switch branches -> git checkout branch-name
# 6. Push to remote -> git push -u origin branch-name
# 7. Pull latest changes -> git pull origin branch-name
# 8. Check status -> git status
# 9. View commit history -> git log
#-------------------------------------------------------------------------------------#

#!/usr/bin/env python3
"""
Genesis Protocol Project Initializer

This script guides users through the project initialization process,
including project profiling, environment setup, and structure creation.
"""

import os
import json
import shutil
import logging
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

try:
    import questionary
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call(["pip", "install", "questionary", "rich"])
    import questionary
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown

from tools.project_profiler import ProjectProfiler

console = Console()

class ProjectInitializer:
    def __init__(self):
        # Get the Genesis Kit directory (where this script is located)
        self.genesis_kit_dir = Path(__file__).parent.absolute()
        # Set base_dir to the parent directory of Genesis Kit
        self.base_dir = self.genesis_kit_dir.parent
        self.templates_dir = self.genesis_kit_dir / "templates"
        self.project_dir = None
        self.project_profile = None
        
        # Setup logging
        logging.basicConfig(
            filename='project_init.log',
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
        
        # Define valid archetypes
        self.valid_archetypes = {
            "alchemist": {
                "description": "Experimental ML/AI research projects focused on innovation and discovery",
                "directories": ["experiments", "research", "synthesis", "notebooks", "models"]
            },
            "sentinel": {
                "description": "Security-focused applications with high-performance requirements",
                "directories": ["security", "performance", "monitoring", "tests", "compliance"]
            },
            "oracle": {
                "description": "Data-driven applications focused on analytics and insights",
                "directories": ["knowledge_base", "analytics", "insights", "vectors", "agents"]
            },
            "engineer": {
                "description": "System architecture and infrastructure projects",
                "directories": ["architecture", "components", "infrastructure", "workflows", "docs"]
            },
            "innovator": {
                "description": "Cutting-edge technology exploration and prototyping",
                "directories": ["prototypes", "labs", "research", "benchmarks", "showcase"]
            },
            "lorekeeper": {
                "description": "Knowledge management and information systems",
                "directories": ["archives", "indices", "taxonomies", "interfaces", "visualizations"]
            }
        }

        # Define archetype-specific configurations
        self.archetype_configs = {
            "alchemist": {
                "dependencies": ["tensorflow", "pytorch", "jupyter", "scikit-learn"],
                "dev_tools": ["pytest", "black", "mypy"]
            },
            "sentinel": {
                "dependencies": ["fastapi", "pydantic", "authlib", "cryptography"],
                "dev_tools": ["pytest", "bandit", "safety"]
            },
            "oracle": {
                "dependencies": ["pandas", "numpy", "langchain", "chromadb"],
                "dev_tools": ["pytest", "black", "mypy"]
            },
            "engineer": {
                "dependencies": ["fastapi", "sqlalchemy", "alembic", "pydantic"],
                "dev_tools": ["pytest", "black", "mypy", "pre-commit"]
            },
            "innovator": {
                "dependencies": ["langchain", "openai", "chromadb", "tiktoken"],
                "dev_tools": ["pytest", "black", "mypy"]
            },
            "lorekeeper": {
                "dependencies": ["elasticsearch", "whoosh", "sqlalchemy", "fastapi"],
                "dev_tools": ["pytest", "sphinx", "mkdocs"]
            }
        }
    
    def initialize_project(self) -> None:
        """Run the project initialization process."""
        try:
            console.print("\n🚀 Welcome to the Genesis Protocol Project Initializer!\n", style="bold blue")
            
            # Start with project profiling
            profiler = ProjectProfiler()
            profiler.setup()
            self.project_profile = profiler.start_profiling()
            
            # Create project directory
            self.project_dir = self._create_project_directory()
            
            # Generate project structure
            self._generate_project_structure()
            
            # Create environment files
            self._create_env_files()
            
            # Generate documentation
            self._generate_documentation()
            
            # Initialize git repository
            self._initialize_git()
            
            console.print("\n✨ Project initialization completed successfully!\n", style="bold green")
            self._display_next_steps()
            
        except Exception as e:
            self.logger.error(f"Error during initialization: {str(e)}")
            console.print(f"\n❌ An error occurred: {str(e)}\n", style="bold red")
            raise
    
    def _create_project_directory(self) -> Path:
        """Create the project directory."""
        project_name = self.project_profile["basic_info"]["name"]
        project_dir = self.base_dir / project_name
        
        if project_dir.exists():
            if not questionary.confirm(
                f"Directory {project_name} already exists. Overwrite?"
            ).ask():
                raise Exception("Project directory already exists")
            shutil.rmtree(project_dir)
        
        project_dir.mkdir(parents=True)
        self.logger.info(f"Created project directory: {project_dir}")
        return project_dir
    
    def _generate_project_structure(self) -> None:
        """Generate project directory structure based on profile."""
        # Base directories
        directories = [
            "src",
            "tests",
            "docs",
            "config",
            "scripts",
            "data",
            "logs"
        ]
        
        # Add archetype-specific directories
        archetype = self.project_profile["archetype"]
        if archetype == "Pioneer":
            directories.extend(["research", "experiments", "prototypes"])
        elif archetype == "Warrior":
            directories.extend(["monitoring", "security", "performance"])
        elif archetype == "Sage":
            directories.extend(["analytics", "models", "datasets"])
        elif archetype == "Craftsman":
            directories.extend(["components", "templates", "assets"])
        
        # Create directories
        for directory in directories:
            (self.project_dir / directory).mkdir(parents=True, exist_ok=True)
        
        self.logger.info("Project structure generated")
    
    def _create_env_files(self) -> None:
        """Create environment configuration files."""
        # Copy .env.example template
        env_example = self.templates_dir / ".env.example"
        if env_example.exists():
            shutil.copy(env_example, self.project_dir / ".env.example")
        
        # Create .env with basic configuration
        env_content = [
            "# Environment Configuration",
            f"APP_NAME={self.project_profile['basic_info']['name']}",
            "ENVIRONMENT=development",
            "DEBUG=true",
            f"API_VERSION=v0.1.0",
            "",
            "# Server Settings",
            "HOST=0.0.0.0",
            "PORT=8000",
            "",
            "# Database Configuration",
            "DATABASE_URL=postgresql://localhost:5432/db_name",
            "",
            "# Security",
            "SECRET_KEY=generate_secure_key_here",
            "",
            "# Logging",
            "LOG_LEVEL=DEBUG",
            "LOG_DIR=logs",
            ""
        ]
        
        with open(self.project_dir / ".env", "w") as f:
            f.write("\n".join(env_content))
        
        self.logger.info("Environment files created")
    
    def _generate_documentation(self) -> None:
        """Generate project documentation."""
        docs_dir = self.project_dir / "docs"
        
        # Generate README.md
        readme_template = self.templates_dir / "README_template.md"
        if readme_template.exists():
            with open(readme_template, "r") as f:
                content = f.read()
            
            # Replace placeholders
            content = content.replace("{{project_name}}", self.project_profile["basic_info"]["name"])
            content = content.replace("{{project_vision}}", self.project_profile["basic_info"]["vision"])
            content = content.replace("{{project_goal}}", self.project_profile["basic_info"]["primary_goal"])
            
            with open(self.project_dir / "README.md", "w") as f:
                f.write(content)
        
        # Generate technical documentation
        tech_doc_template = self.templates_dir / "technical_docs_template.md"
        if tech_doc_template.exists():
            shutil.copy(tech_doc_template, docs_dir / "technical_documentation.md")
        
        # Save project profile
        with open(docs_dir / "project_profile.json", "w") as f:
            json.dump(self.project_profile, f, indent=2)
        
        self.logger.info("Project documentation generated")
    
    def _initialize_git(self) -> None:
        """Initialize git repository."""
        try:
            import subprocess
            
            # Initialize git
            subprocess.run(["git", "init"], cwd=self.project_dir, check=True)
            
            # Copy gitignore template
            gitignore_template = self.templates_dir / "gitignore_template"
            if gitignore_template.exists():
                shutil.copy(gitignore_template, self.project_dir / ".gitignore")
            
            # Initial commit
            subprocess.run(["git", "add", "."], cwd=self.project_dir, check=True)
            subprocess.run(
                ["git", "commit", "-m", "Initial commit: Project initialized with Genesis Protocol"],
                cwd=self.project_dir,
                check=True
            )
            
            self.logger.info("Git repository initialized")
            
        except Exception as e:
            self.logger.warning(f"Git initialization failed: {str(e)}")
            console.print("\n⚠️  Git initialization failed. Please initialize manually.\n", style="yellow")
    
    def _display_next_steps(self) -> None:
        """Display next steps for the user."""
        console.print("\n📋 Next Steps:\n", style="bold blue")
        
        steps = [
            f"1. cd {self.project_profile['basic_info']['name']}",
            "2. Create and activate a virtual environment:",
            "   python -m venv venv",
            "   source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate",
            "3. Install dependencies:",
            "   pip install -r requirements.txt",
            "4. Configure your .env file with your specific settings",
            "5. Start developing according to your project profile!",
            "",
            "📚 Documentation can be found in the docs/ directory",
            "🎮 Your project profile is saved in docs/project_profile.json"
        ]
        
        for step in steps:
            console.print(step)

if __name__ == "__main__":
    initializer = ProjectInitializer()
    initializer.initialize_project() 