#!/usr/bin/env python3
"""
Project Profiler - Character Creation System for Projects

This module implements a video game-like character creation system for projects,
helping developers align their project characteristics with their needs and goals.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import shutil

try:
    import questionary
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.table import Table
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call(["pip", "install", "questionary", "rich"])
    import questionary
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.table import Table

console = Console()

class ProjectProfiler:
    def __init__(self):
        self.profile_dir = Path("project_profile")
        self.profile_file = self.profile_dir / "project_character.json"
        self.templates_dir = Path(__file__).parent.parent / "templates"
        
        # Setup logging
        logging.basicConfig(
            filename='project_profiler.log',
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
        
        # Define project attributes
        self.attributes = {
            "scale": {
                "small": "Personal or small team project",
                "medium": "Department or medium organization",
                "large": "Enterprise or large-scale system"
            },
            "complexity": {
                "basic": "Simple, straightforward functionality",
                "moderate": "Multiple integrated features",
                "complex": "Advanced system with many components"
            },
            "innovation": {
                "conventional": "Proven, traditional approaches",
                "progressive": "Modern, evolving technologies",
                "cutting_edge": "Experimental, bleeding-edge tech"
            },
            "time_sensitivity": {
                "relaxed": "Flexible timeline",
                "moderate": "Balanced deadlines",
                "urgent": "Time-critical delivery"
            }
        }
        
        # Define project archetypes
        self.archetypes = {
            "Alchemist": {
                "description": "Experimental ML/AI research projects focused on innovation and discovery",
                "tech_focus": ["ml", "ai", "research"],
                "recommended_traits": ["cutting_edge", "complex", "innovative"]
            },
            "Sentinel": {
                "description": "Security-focused applications with high-performance requirements",
                "tech_focus": ["security", "performance", "monitoring"],
                "recommended_traits": ["complex", "secure", "reliable"]
            },
            "Oracle": {
                "description": "Data-driven applications focused on analytics and insights",
                "tech_focus": ["analytics", "ai", "data"],
                "recommended_traits": ["data_intensive", "scalable", "intelligent"]
            },
            "Engineer": {
                "description": "System architecture and infrastructure projects",
                "tech_focus": ["infrastructure", "devops", "architecture"],
                "recommended_traits": ["maintainable", "scalable", "robust"]
            },
            "Innovator": {
                "description": "Cutting-edge technology exploration and prototyping",
                "tech_focus": ["research", "prototyping", "innovation"],
                "recommended_traits": ["experimental", "innovative", "agile"]
            },
            "Lorekeeper": {
                "description": "Knowledge management and information systems",
                "tech_focus": ["knowledge_base", "search", "organization"],
                "recommended_traits": ["structured", "searchable", "comprehensive"]
            }
        }
    
    def setup(self) -> None:
        """Create necessary directories."""
        self.profile_dir.mkdir(parents=True, exist_ok=True)
        self.logger.info("Project profiler setup complete")
    
    def start_profiling(self) -> Dict:
        """Begin the project character creation process."""
        try:
            console.print("\n🎮 Welcome to Project Character Creation!\n", style="bold blue")
            
            # Gather basic information
            project_info = self._gather_basic_info()
            
            # Determine project attributes
            attributes = self._determine_attributes()
            
            # Suggest project archetype
            archetype = self._suggest_archetype(attributes)
            
            # Get tech stack preferences
            tech_preferences = self._gather_tech_preferences(archetype)
            
            # Compile full profile
            profile = {
                "basic_info": project_info,
                "attributes": attributes,
                "archetype": archetype,
                "tech_preferences": tech_preferences,
                "created_at": datetime.now().isoformat()
            }
            
            # Save profile
            self._save_profile(profile)
            
            # Display summary
            self._display_profile_summary(profile)
            
            # Generate project structure
            if questionary.confirm("Would you like to generate the project structure now?").ask():
                self.generate_project_structure(profile)
            
            return profile
            
        except Exception as e:
            self.logger.error(f"Error during profiling: {str(e)}")
            console.print(f"\n❌ An error occurred: {str(e)}\n", style="bold red")
            raise
    
    def _gather_basic_info(self) -> Dict:
        """Gather basic project information."""
        return {
            "name": questionary.text("What is your project's name?").ask(),
            "vision": questionary.text("What is your project's vision?").ask(),
            "primary_goal": questionary.text("What is the primary goal of your project?").ask(),
            "target_users": questionary.text("Who are your target users?").ask(),
            "organization_type": questionary.select(
                "What type of organization is this for?",
                choices=["Personal", "Startup", "Enterprise", "Academic", "Non-profit"]
            ).ask()
        }
    
    def _determine_attributes(self) -> Dict:
        """Determine project attributes through interactive questions."""
        attributes = {}
        
        for attr, levels in self.attributes.items():
            choice = questionary.select(
                f"Choose your project's {attr} level:",
                choices=[{
                    'name': f"{level}: {desc}",
                    'value': level
                } for level, desc in levels.items()]
            ).ask()
            attributes[attr] = choice
        
        return attributes
    
    def _suggest_archetype(self, attributes: Dict) -> str:
        """Suggest a project archetype based on attributes."""
        # Simple matching algorithm
        scores = {name: 0 for name in self.archetypes.keys()}
        
        for archetype, details in self.archetypes.items():
            for trait in details["recommended_traits"]:
                if trait in attributes.values():
                    scores[archetype] += 1
        
        # Get top matches
        top_archetypes = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:2]
        
        # Let user choose from top matches
        choice = questionary.select(
            "Based on your choices, these archetypes suit your project best. Choose one:",
            choices=[
                f"{name}: {self.archetypes[name]['description']}"
                for name, _ in top_archetypes
            ]
        ).ask()
        
        return choice.split(":")[0]
    
    def _gather_tech_preferences(self, archetype: str) -> Dict:
        """Gather technology preferences based on archetype."""
        tech_focus = self.archetypes[archetype]["tech_focus"]
        
        # Load framework descriptions
        self.tech_preferences = {
            "ml_frameworks": [
                "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "XGBoost",
                "JAX", "Flax", "Pyro", "GLM-PyTorch"
            ],
            "ai_frameworks": [
                "LangChain", "LangGraph", "LlamaIndex", "Pydantic AI",
                "Hugging Face Transformers", "Groq", "OpenAI", "Anthropic",
                "Mistral AI", "Haystack"
            ],
            # ... [rest of the framework lists remain the same]
        }
        
        preferences = {
            "project_type": questionary.select(
                "What type of project are you building?",
                choices=[
                    "Web Application",
                    "API Service",
                    "AI/ML Application",
                    "Data Processing Pipeline",
                    "Social Media Management",
                    "Knowledge Management System",
                    "Hybrid (Multiple Types)"
                ]
            ).ask(),
        }
        
        # For each category, use the framework descriptions
        for category, frameworks in self.tech_preferences.items():
            choices = self._get_framework_choices(category)
            if choices:
                selections = questionary.checkbox(
                    f"Select {category.replace('_', ' ').title()}:",
                    choices=choices
                ).ask()
                preferences[category] = selections
        
        return preferences
    
    def _save_profile(self, profile: Dict) -> None:
        """Save the project profile to file."""
        with open(self.profile_file, "w") as f:
            json.dump(profile, f, indent=2)
        self.logger.info("Project profile saved")
    
    def _display_profile_summary(self, profile: Dict) -> None:
        """Display a summary of the project profile."""
        console.print("\n✨ Your Project Character Sheet ✨\n", style="bold green")
        
        # Basic Info
        console.print(Panel(
            f"Project: {profile['basic_info']['name']}\n"
            f"Vision: {profile['basic_info']['vision']}\n"
            f"Goal: {profile['basic_info']['primary_goal']}\n"
            f"Users: {profile['basic_info']['target_users']}\n"
            f"Organization: {profile['basic_info']['organization_type']}",
            title="Basic Information"
        ))
        
        # Project Type and Requirements
        console.print(Panel(
            f"Project Type: {profile['tech_preferences']['project_type']}\n"
            f"Core Requirements: {', '.join(profile['tech_preferences']['core_requirements'])}",
            title="Project Requirements"
        ))
        
        # Attributes
        attr_table = Table(title="Project Attributes")
        attr_table.add_column("Attribute", style="cyan")
        attr_table.add_column("Level", style="green")
        
        for attr, value in profile['attributes'].items():
            attr_table.add_row(attr.title(), value.title())
        
        console.print(attr_table)
        
        # Archetype
        console.print(Panel(
            f"Archetype: {profile['archetype']}\n"
            f"Description: {self.archetypes[profile['archetype']]['description']}",
            title="Project Archetype"
        ))
        
        # Tech Stack - Core Components
        core_tech_table = Table(title="Core Technology Stack")
        core_tech_table.add_column("Category", style="cyan")
        core_tech_table.add_column("Selections", style="green", no_wrap=False)
        
        core_categories = [
            "ml_frameworks",
            "ai_frameworks",
            "nlp_libraries",
            "computer_vision",
            "data_processing"
        ]
        
        for category in core_categories:
            if profile['tech_preferences'].get(category):
                core_tech_table.add_row(
                    category.replace('_', ' ').title(),
                    ", ".join(profile['tech_preferences'][category])
                )
        
        console.print(core_tech_table)
        
        # Tech Stack - Infrastructure
        infra_tech_table = Table(title="Infrastructure & Tools")
        infra_tech_table.add_column("Category", style="cyan")
        infra_tech_table.add_column("Selections", style="green", no_wrap=False)
        
        infra_categories = [
            "databases",
            "vector_databases",
            "workflow_orchestration",
            "model_serving",
            "deployment_platforms",
            "monitoring_logging"
        ]
        
        for category in infra_categories:
            if profile['tech_preferences'].get(category):
                infra_tech_table.add_row(
                    category.replace('_', ' ').title(),
                    ", ".join(profile['tech_preferences'][category])
                )
        
        console.print(infra_tech_table)
        
        # Tech Stack - Development Tools
        dev_tech_table = Table(title="Development & Testing Tools")
        dev_tech_table.add_column("Category", style="cyan")
        dev_tech_table.add_column("Selections", style="green", no_wrap=False)
        
        dev_categories = [
            "testing_tools",
            "security_auth",
            "visualization",
            "audio_voice"
        ]
        
        for category in dev_categories:
            if profile['tech_preferences'].get(category):
                dev_tech_table.add_row(
                    category.replace('_', ' ').title(),
                    ", ".join(profile['tech_preferences'][category])
                )
        
        console.print(dev_tech_table)
        
        # Next Steps and Recommendations
        console.print("\n📝 Next Steps:", style="bold blue")
        console.print("1. Review the generated project structure")
        console.print("2. Configure selected technologies")
        console.print("3. Set up development environment")
        console.print("4. Initialize version control")
        
        # Additional Recommendations based on project type
        if profile['tech_preferences']['project_type'] == "AI/ML Application":
            console.print("\n🤖 AI/ML Specific Recommendations:", style="bold magenta")
            console.print("- Set up model versioning and experiment tracking")
            console.print("- Configure model serving infrastructure")
            console.print("- Implement monitoring for model performance")
        
        console.print("\n📚 Documentation will be generated for your specific tech stack")

    def generate_project_structure(self, profile: Dict) -> None:
        """Generate the actual project structure based on the profile."""
        try:
            # Get project name and create project directory in parent folder
            project_name = profile['basic_info']['name']
            project_dir = Path(__file__).parent.parent.parent / project_name
            
            if project_dir.exists():
                if not questionary.confirm(
                    f"Directory {project_name} already exists. Overwrite?"
                ).ask():
                    raise Exception("Project directory already exists")
                shutil.rmtree(project_dir)
            
            project_dir.mkdir(parents=True)
            self.logger.info(f"Created project directory: {project_dir}")

            # Create basic project structure
            base_dirs = [
                "src",
                "tests",
                "docs",
                "config",
                "scripts",
                "data",
                "logs"
            ]

            # Add specialized directories based on project type
            if profile['tech_preferences']['project_type'] == "AI/ML Application":
                base_dirs.extend([
                    "models",
                    "notebooks",
                    "experiments",
                    "datasets"
                ])
            elif profile['tech_preferences']['project_type'] == "Knowledge Management System":
                base_dirs.extend([
                    "knowledge_base",
                    "indices",
                    "templates",
                    "assets"
                ])

            # Create directories
            for dir_name in base_dirs:
                (project_dir / dir_name).mkdir(parents=True, exist_ok=True)

            # Generate configuration files
            self._generate_config_files(project_dir, profile)
            
            # Generate requirements.txt
            self._generate_requirements(project_dir, profile)
            
            # Generate README.md
            self._generate_readme(project_dir, profile)
            
            # Generate documentation
            self._generate_documentation(project_dir, profile)
            
            # Initialize git repository
            self._initialize_git(project_dir)
            
            console.print(f"\n✨ Project structure generated at: {project_dir}", style="bold green")
            
        except Exception as e:
            self.logger.error(f"Error generating project structure: {str(e)}")
            raise

    def _generate_config_files(self, project_dir: Path, profile: Dict) -> None:
        """Generate configuration files for the project."""
        # Generate .env file
        env_content = [
            "# Environment Configuration",
            f"PROJECT_NAME={profile['basic_info']['name']}",
            "ENVIRONMENT=development",
            "DEBUG=true",
            "",
            "# API Configuration",
            "API_VERSION=v1",
            "HOST=0.0.0.0",
            "PORT=8000",
            "",
            "# Database Configuration",
            self._get_database_config(profile),
            "",
            "# Security",
            "SECRET_KEY=your-secret-key-here",
            "",
            "# Logging",
            "LOG_LEVEL=DEBUG",
            "LOG_DIR=logs"
        ]
        
        with open(project_dir / ".env", "w") as f:
            f.write("\n".join(env_content))
        
        # Copy .env.example
        shutil.copy(project_dir / ".env", project_dir / ".env.example")

    def _generate_requirements(self, project_dir: Path, profile: Dict) -> None:
        """Generate requirements.txt based on selected technologies."""
        requirements = set()
        
        # Add core Python packages
        requirements.add("python-dotenv>=1.0.0")
        requirements.add("pydantic>=2.0.0")
        
        # Add selected packages based on tech preferences
        for category, selections in profile['tech_preferences'].items():
            if isinstance(selections, list):  # Skip non-list items like project_type
                for tech in selections:
                    pkg_name = self._get_package_name(tech)
                    if pkg_name:
                        requirements.add(pkg_name)
        
        # Write requirements.txt
        with open(project_dir / "requirements.txt", "w") as f:
            f.write("\n".join(sorted(requirements)))

    def _get_package_name(self, tech: str) -> Optional[str]:
        """Convert technology name to pip package name."""
        # Mapping of technology names to pip package names
        package_map = {
            "FastAPI": "fastapi>=0.100.0",
            "LangChain": "langchain>=0.0.200",
            "Groq": "groq>=0.3.0",
            "ChromaDB": "chromadb>=0.4.0",
            "Pydantic AI": "pydantic-ai>=1.0.0",
            "PyTorch": "torch>=2.0.0",
            "TensorFlow": "tensorflow>=2.13.0",
            # Add more mappings as needed
        }
        return package_map.get(tech)

    def _get_database_config(self, profile: Dict) -> str:
        """Generate database configuration based on selected databases."""
        db_config = []
        if "PostgreSQL" in profile['tech_preferences'].get('databases', []):
            db_config.append("DATABASE_URL=postgresql://localhost:5432/db_name")
        if "MongoDB" in profile['tech_preferences'].get('databases', []):
            db_config.append("MONGODB_URL=mongodb://localhost:27017/db_name")
        if "Redis" in profile['tech_preferences'].get('databases', []):
            db_config.append("REDIS_URL=redis://localhost:6379/0")
        
        return "\n".join(db_config) or "DATABASE_URL=sqlite:///./app.db"

    def _get_framework_choices(self, category: str) -> List[Dict]:
        """Get framework choices with descriptions."""
        framework_descriptions = {
            "TensorFlow": "Google's open-source ML framework for production-grade ML systems",
            "PyTorch": "Facebook's ML framework focused on research and flexibility",
            "Keras": "High-level neural network library running on TensorFlow",
            "Scikit-learn": "Simple and efficient ML library for data mining and analysis",
            "XGBoost": "Optimized gradient boosting library for structured data",
            "JAX": "Google's high-performance numerical computing library",
            "LangChain": "Framework for developing LLM-powered applications",
            "LangGraph": "Graph-based orchestration for LLM workflows",
            "LlamaIndex": "Data framework for LLM applications",
            "Pydantic AI": "Data validation for AI/ML applications",
            "Groq": "High-performance AI inference engine",
            "ChromaDB": "Open-source embedding database for AI applications",
            "Weaviate": "Vector search engine with semantic search capabilities",
            "FastAPI": "Modern, fast web framework for building APIs",
            "Celery": "Distributed task queue for async job processing",
            "PostgreSQL": "Advanced open-source relational database",
            "MongoDB": "Document-based NoSQL database",
            "Redis": "In-memory data structure store and cache",
            "Eleven Labs": "Advanced text-to-speech with voice customization",
            "Whisper": "OpenAI's speech recognition system",
            "Pytest": "Feature-rich Python testing framework",
            "Docker": "Container platform for application packaging",
            "Kubernetes": "Container orchestration platform",
            "Grafana": "Analytics and monitoring solution",
            "Logfire": "Advanced logging and monitoring platform"
        }
        
        choices = []
        for tech in self.tech_preferences.get(category, []):
            choices.append({
                'name': f"{tech}: {framework_descriptions.get(tech, 'No description available')}",
                'value': tech
            })
        return choices

if __name__ == "__main__":
    profiler = ProjectProfiler()
    profiler.setup()
    profiler.start_profiling() 