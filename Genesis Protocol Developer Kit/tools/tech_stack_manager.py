#!/usr/bin/env python3
"""
Tech Stack Documentation Manager

This script helps manage and update tech stack documentation for the Genesis Protocol.
It provides tools to add, update, and organize documentation for frameworks, libraries, and APIs.
"""

import os
import json
import shutil
import logging
from pathlib import Path
from typing import Dict, List, Optional
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

# Setup rich console
console = Console()

class TechStackManager:
    def __init__(self):
        self.base_dir = Path("docs/tech_stack")
        self.config_file = Path("project_config.json")
        self.categories = ["frameworks", "libraries", "apis"]
        
        # Setup logging
        logging.basicConfig(
            filename='tech_stack_manager.log',
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
    
    def setup_directory_structure(self) -> None:
        """Create the initial directory structure."""
        for category in self.categories:
            (self.base_dir / category).mkdir(parents=True, exist_ok=True)
        self.logger.info("Directory structure created")
    
    def create_component_docs(self, category: str, name: str) -> None:
        """Create documentation structure for a new component."""
        component_dir = self.base_dir / category / name
        component_dir.mkdir(parents=True, exist_ok=True)
        
        # Create documentation files based on category
        if category == "frameworks":
            files = {
                "overview.md": self._get_framework_overview_template(name),
                "best_practices.md": self._get_best_practices_template(name),
                "integration_guides.md": self._get_integration_guide_template(name)
            }
        elif category == "libraries":
            files = {
                "overview.md": self._get_library_overview_template(name),
                "usage_guides.md": self._get_usage_guide_template(name),
                "examples.md": self._get_examples_template(name)
            }
        else:  # APIs
            files = {
                "documentation.md": self._get_api_documentation_template(name),
                "endpoints.md": self._get_endpoints_template(name),
                "examples.md": self._get_examples_template(name)
            }
        
        # Create files
        for filename, content in files.items():
            with open(component_dir / filename, "w") as f:
                f.write(content)
        
        self.logger.info(f"Created documentation for {category}/{name}")
    
    def update_project_config(self, config_updates: Dict) -> None:
        """Update the project configuration file."""
        if self.config_file.exists():
            with open(self.config_file, "r") as f:
                config = json.load(f)
        else:
            config = {
                "project_name": "",
                "tech_stack": {
                    "frameworks": [],
                    "libraries": [],
                    "apis": []
                },
                "documentation_paths": {
                    "framework_docs": [],
                    "library_docs": [],
                    "api_docs": []
                }
            }
        
        # Update config with new values
        for key, value in config_updates.items():
            if isinstance(value, dict):
                config[key].update(value)
            else:
                config[key] = value
        
        # Write updated config
        with open(self.config_file, "w") as f:
            json.dump(config, f, indent=2)
        
        self.logger.info("Project configuration updated")
    
    def add_component(self) -> None:
        """Interactive prompt to add a new component."""
        category = questionary.select(
            "Select component category:",
            choices=self.categories
        ).ask()
        
        name = questionary.text(
            f"Enter {category[:-1]} name:"
        ).ask()
        
        version = questionary.text(
            f"Enter {name} version:"
        ).ask()
        
        description = questionary.text(
            f"Enter brief description for {name}:"
        ).ask()
        
        # Create documentation
        self.create_component_docs(category, name)
        
        # Update config
        config_updates = {
            "tech_stack": {
                category: [name]
            },
            "documentation_paths": {
                f"{category[:-1]}_docs": [
                    str(self.base_dir / category / name)
                ]
            }
        }
        self.update_project_config(config_updates)
        
        console.print(f"\n✨ Added {name} to {category}\n", style="bold green")
    
    def _get_framework_overview_template(self, name: str) -> str:
        return f"""# {name} Framework Overview

## Introduction
[Brief introduction to {name}]

## Key Features
- Feature 1
- Feature 2

## Installation
```bash
# Installation commands
```

## Basic Usage
```python
# Basic usage example
```

## Configuration
[Configuration details]

## Version Information
- Current Version: [version]
- Release Date: {datetime.now().strftime('%Y-%m-%d')}
- Compatibility: [compatibility info]

## Resources
- [Official Documentation]
- [GitHub Repository]
- [Community Resources]
"""
    
    def _get_best_practices_template(self, name: str) -> str:
        return f"""# {name} Best Practices

## Code Organization
[Code organization guidelines]

## Performance Optimization
[Performance best practices]

## Security Considerations
[Security guidelines]

## Error Handling
[Error handling patterns]

## Testing
[Testing best practices]

## Deployment
[Deployment considerations]

## Maintenance
[Maintenance guidelines]
"""
    
    def _get_integration_guide_template(self, name: str) -> str:
        return f"""# {name} Integration Guide

## Prerequisites
[List prerequisites]

## Setup Steps
1. [Step 1]
2. [Step 2]

## Configuration
[Configuration details]

## Common Integration Patterns
[Common patterns]

## Troubleshooting
[Troubleshooting guide]

## Examples
[Integration examples]
"""
    
    def _get_library_overview_template(self, name: str) -> str:
        return f"""# {name} Library Overview

## Purpose
[Library purpose]

## Features
[Key features]

## Installation
[Installation guide]

## Basic Usage
[Usage examples]

## API Reference
[API documentation]
"""
    
    def _get_usage_guide_template(self, name: str) -> str:
        return f"""# {name} Usage Guide

## Getting Started
[Getting started guide]

## Common Use Cases
[Common use cases]

## Advanced Usage
[Advanced usage patterns]

## Best Practices
[Best practices]
"""
    
    def _get_examples_template(self, name: str) -> str:
        return f"""# {name} Examples

## Basic Examples
[Basic usage examples]

## Advanced Examples
[Advanced usage examples]

## Integration Examples
[Integration examples]

## Common Patterns
[Common usage patterns]
"""
    
    def _get_api_documentation_template(self, name: str) -> str:
        return f"""# {name} API Documentation

## Overview
[API overview]

## Authentication
[Authentication details]

## Rate Limiting
[Rate limiting info]

## Endpoints
[Endpoint list]

## Error Handling
[Error handling]
"""
    
    def _get_endpoints_template(self, name: str) -> str:
        return f"""# {name} API Endpoints

## Base URL
[Base URL information]

## Available Endpoints

### Endpoint 1
- Method: [HTTP method]
- Path: [endpoint path]
- Description: [description]
- Parameters: [parameters]
- Response: [response format]

### Endpoint 2
[Additional endpoints]
"""

if __name__ == "__main__":
    manager = TechStackManager()
    
    # Setup initial structure
    manager.setup_directory_structure()
    
    # Interactive menu
    while True:
        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Add new component",
                "Update existing component",
                "View documentation",
                "Exit"
            ]
        ).ask()
        
        if action == "Add new component":
            manager.add_component()
        elif action == "Update existing component":
            console.print("Feature coming soon!", style="yellow")
        elif action == "View documentation":
            console.print("Feature coming soon!", style="yellow")
        else:
            break 