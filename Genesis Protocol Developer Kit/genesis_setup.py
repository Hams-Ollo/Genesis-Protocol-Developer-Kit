#-------------------------------------------------------------------------------------#
# genesis_setup.py
#-------------------------------------------------------------------------------------#
# SETUP:
#
# Setup venv and install the requirements
# 1. Create a virtual environment -> python -m venv venv
# 2. Activate the virtual environment -> .\venv\Scripts\Activate
# 3. Install the requirements -> pip install -r requirements.txt
# 4. Run the file -> python genesis_setup.py
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
Genesis Protocol Developer Kit Setup

This script handles the initial setup of the Genesis Protocol Developer Kit,
including installing required dependencies and preparing the environment.
"""

import os
import sys
import subprocess
import logging
from pathlib import Path
from typing import List

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class GenesisSetup:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.requirements_file = self.base_dir / "requirements.txt"

        # Core requirements for the Genesis Kit
        self.core_requirements = [
            "questionary>=2.0.0",
            "rich>=13.0.0",
            "python-dotenv>=1.0.0",
            "pydantic>=2.0.0",
            "colorama>=0.4.6",
            "typer>=0.9.0",
            "click>=8.0.0",
            "jinja2>=3.0.0",
            "pyyaml>=6.0.0",
            "toml>=0.10.0"
        ]

        # Optional tool-specific requirements
        self.tool_requirements = {
            "development": [
                "black>=23.0.0",
                "flake8>=6.0.0",
                "mypy>=1.0.0",
                "pytest>=7.0.0",
                "pytest-cov>=4.0.0",
                "pre-commit>=3.0.0"
            ],
            "documentation": [
                "mkdocs>=1.5.0",
                "mkdocs-material>=9.0.0",
                "mkdocstrings>=0.22.0"
            ],
            "ai_tools": [
                "langchain>=0.1.0",
                "openai>=1.0.0",
                "chromadb>=0.4.0",
                "tiktoken>=0.5.0"
            ]
        }

        # Archetype-specific requirements
        self.archetype_requirements = {
            "alchemist": {
                "core": [
                    "tensorflow>=2.13.0",
                    "torch>=2.0.0",
                    "jupyter>=1.0.0",
                    "scikit-learn>=1.3.0"
                ],
                "optional": [
                    "optuna>=3.3.0",
                    "mlflow>=2.7.0",
                    "wandb>=0.15.0"
                ]
            },
            "sentinel": {
                "core": [
                    "fastapi>=0.100.0",
                    "pydantic>=2.0.0",
                    "authlib>=1.2.0",
                    "cryptography>=41.0.0"
                ],
                "optional": [
                    "bandit>=1.7.5",
                    "safety>=2.3.0",
                    "owasp-dependency-check>=8.4.0"
                ]
            },
            "oracle": {
                "core": [
                    "pandas>=2.0.0",
                    "numpy>=1.24.0",
                    "langchain>=0.0.200",
                    "chromadb>=0.4.0"
                ],
                "optional": [
                    "plotly>=5.16.0",
                    "streamlit>=1.26.0",
                    "great-expectations>=0.17.0"
                ]
            },
            "engineer": {
                "core": [
                    "fastapi>=0.100.0",
                    "sqlalchemy>=2.0.0",
                    "alembic>=1.12.0",
                    "pydantic>=2.0.0"
                ],
                "optional": [
                    "docker>=6.1.0",
                    "kubernetes>=28.1.0",
                    "terraform-provider>=0.5.0"
                ]
            },
            "innovator": {
                "core": [
                    "langchain>=0.0.200",
                    "openai>=0.28.0",
                    "chromadb>=0.4.0",
                    "tiktoken>=0.5.0"
                ],
                "optional": [
                    "anthropic>=0.3.0",
                    "groq>=0.3.0",
                    "mistralai>=0.0.7"
                ]
            },
            "lorekeeper": {
                "core": [
                    "elasticsearch>=8.10.0",
                    "whoosh>=2.7.4",
                    "sqlalchemy>=2.0.0",
                    "fastapi>=0.100.0"
                ],
                "optional": [
                    "sphinx>=7.1.0",
                    "mkdocs>=1.5.0",
                    "mkdocstrings>=0.23.0"
                ]
            }
        }

    def check_python_version(self) -> bool:
        """Check if Python version meets requirements."""
        required_version = (3, 8)
        current_version = sys.version_info[:2]

        if current_version < required_version:
            logger.error(
                f"Python {required_version[0]}.{required_version[1]} or higher is required. "
                f"You are using Python {current_version[0]}.{current_version[1]}"
            )
            return False
        return True

    def create_virtual_environment(self) -> bool:
        """Create a virtual environment for the kit."""
        try:
            venv_path = self.base_dir / "venv"
            if not venv_path.exists():
                logger.info("Creating virtual environment...")
                subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
                logger.info("Virtual environment created successfully")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to create virtual environment: {str(e)}")
            return False

    def get_venv_python(self) -> str:
        """Get the path to the virtual environment Python executable."""
        if sys.platform == "win32":
            return str(self.base_dir / "venv" / "Scripts" / "python.exe")
        return str(self.base_dir / "venv" / "bin" / "python")

    def install_requirements(self, requirements: List[str]) -> bool:
        """Install the specified requirements."""
        try:
            venv_pip = self.get_venv_python()
            process = subprocess.run(
                [venv_pip, "-m", "pip", "install"] + requirements,
                check=True,
                capture_output=True,
                text=True
            )
            logger.info(process.stdout)
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install requirements: {e.stderr}")
            return False

    def generate_requirements_file(self) -> None:
        """Generate requirements.txt with all dependencies."""
        all_requirements = self.core_requirements.copy()
        for category in self.tool_requirements.values():
            all_requirements.extend(category)

        with open(self.requirements_file, "w") as f:
            f.write("\n".join(all_requirements))

        logger.info("Generated requirements.txt")

    def setup_git_hooks(self) -> None:
        """Set up Git hooks for development."""
        try:
            subprocess.run(
                [self.get_venv_python(), "-m", "pre-commit", "install"],
                check=True,
                cwd=self.base_dir
            )
            logger.info("Git hooks installed successfully")
        except subprocess.CalledProcessError as e:
            logger.warning(f"Failed to set up Git hooks: {str(e)}")

    def run_setup(self) -> None:
        """Run the complete setup process."""
        print("\n🚀 Setting up Genesis Protocol Developer Kit...\n")

        # Check Python version
        if not self.check_python_version():
            sys.exit(1)

        # Create virtual environment
        if not self.create_virtual_environment():
            sys.exit(1)

        # Generate requirements.txt
        self.generate_requirements_file()

        # Install core requirements
        print("\n📦 Installing core requirements...")
        if not self.install_requirements(self.core_requirements):
            sys.exit(1)

        # Ask for optional components
        print("\n🎯 Select additional components to install:\n")
        try:
            import questionary
            from rich.console import Console

            console = Console()
            selected_components = questionary.checkbox(
                "Choose additional components:",
                choices=[
                    "Development Tools (black, flake8, pytest, etc.)",
                    "Documentation Tools (mkdocs, mkdocs-material)",
                    "AI Tools (langchain, openai, chromadb)"
                ]
            ).ask()

            # Install selected components
            if "Development Tools" in selected_components:
                print("\n🛠️  Installing development tools...")
                self.install_requirements(self.tool_requirements["development"])
                self.setup_git_hooks()

            if "Documentation Tools" in selected_components:
                print("\n📚 Installing documentation tools...")
                self.install_requirements(self.tool_requirements["documentation"])

            if "AI Tools" in selected_components:
                print("\n🤖 Installing AI tools...")
                self.install_requirements(self.tool_requirements["ai_tools"])

        except ImportError:
            # If questionary isn't available yet, install everything
            print("\n📦 Installing all components...")
            for requirements in self.tool_requirements.values():
                self.install_requirements(requirements)

        print("\n✨ Genesis Protocol Developer Kit setup completed!\n")
        print("Next steps:")
        print("1. Activate the virtual environment:")
        if sys.platform == "win32":
            print("   .\\venv\\Scripts\\activate")
        else:
            print("   source venv/bin/activate")
        print("2. Run the initialization script:")
        print("   python initialize_project.py")
        print("\nHappy developing! 🎮\n")

if __name__ == "__main__":
    setup = GenesisSetup()
    setup.run_setup()
