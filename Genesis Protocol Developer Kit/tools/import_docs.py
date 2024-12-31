#!/usr/bin/env python3
"""
Documentation Import Tool

This script helps import and organize existing documentation from project_init_src_docs
into the Genesis Protocol Developer Kit structure.
"""

import os
import shutil
import logging
from pathlib import Path
from typing import Dict, List, Optional

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call(["pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown

# Setup rich console
console = Console()

class DocumentationImporter:
    def __init__(self):
        self.source_dir = Path("project_init_src_docs")
        self.target_dir = Path("docs")
        self.tech_stack_dir = self.target_dir / "tech_stack"
        
        # Setup logging
        logging.basicConfig(
            filename='doc_import.log',
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
    
    def setup_directory_structure(self) -> None:
        """Create necessary directory structure."""
        directories = [
            self.tech_stack_dir / "frameworks",
            self.tech_stack_dir / "libraries",
            self.tech_stack_dir / "apis",
            self.target_dir / "roadmap",
            self.target_dir / "guides"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
        
        self.logger.info("Directory structure created")
    
    def import_tech_stack_docs(self) -> None:
        """Import and organize tech stack documentation."""
        if not self.source_dir.exists():
            console.print("Source directory not found!", style="bold red")
            return
        
        tech_stack_file = self.source_dir / "tech_stack_docs.txt"
        if tech_stack_file.exists():
            # Create organized documentation structure
            frameworks_dir = self.tech_stack_dir / "frameworks"
            libraries_dir = self.tech_stack_dir / "libraries"
            apis_dir = self.tech_stack_dir / "apis"
            
            with open(tech_stack_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Split content into sections and organize
            sections = self._split_into_sections(content)
            
            for section_title, section_content in sections.items():
                if "framework" in section_title.lower():
                    target_dir = frameworks_dir
                elif "library" in section_title.lower():
                    target_dir = libraries_dir
                elif "api" in section_title.lower():
                    target_dir = apis_dir
                else:
                    continue
                
                # Create markdown file for section
                safe_title = "".join(c for c in section_title if c.isalnum() or c in "- ").strip()
                safe_title = safe_title.replace(" ", "_").lower()
                
                with open(target_dir / f"{safe_title}.md", "w", encoding="utf-8") as f:
                    f.write(f"# {section_title}\n\n{section_content}")
            
            self.logger.info("Tech stack documentation imported")
    
    def import_roadmap(self) -> None:
        """Import project roadmap documentation."""
        roadmap_file = self.source_dir / "project_roadmap.txt"
        if roadmap_file.exists():
            target_file = self.target_dir / "roadmap" / "project_roadmap.md"
            
            with open(roadmap_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            with open(target_file, "w", encoding="utf-8") as f:
                f.write("# Project Roadmap\n\n")
                f.write(content)
            
            self.logger.info("Project roadmap imported")
    
    def import_agent_prompts(self) -> None:
        """Import IDE agent initialization prompts."""
        agent_file = self.source_dir / "IDE_agent_init_prompt.txt"
        if agent_file.exists():
            target_file = self.target_dir / "guides" / "ide_agent_setup.md"
            
            with open(agent_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            with open(target_file, "w", encoding="utf-8") as f:
                f.write("# IDE Agent Setup Guide\n\n")
                f.write(content)
            
            self.logger.info("IDE agent prompts imported")
    
    def import_meta_prompts(self) -> None:
        """Import codebase meta prompts."""
        meta_file = self.source_dir / "codebase_meta_prompts.txt"
        if meta_file.exists():
            target_file = self.target_dir / "guides" / "codebase_prompts.md"
            
            with open(meta_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            with open(target_file, "w", encoding="utf-8") as f:
                f.write("# Codebase Interaction Guide\n\n")
                f.write(content)
            
            self.logger.info("Codebase meta prompts imported")
    
    def _split_into_sections(self, content: str) -> Dict[str, str]:
        """Split content into titled sections."""
        sections = {}
        current_title = None
        current_content = []
        
        for line in content.split("\n"):
            if line.startswith("#"):
                if current_title:
                    sections[current_title] = "\n".join(current_content)
                current_title = line.lstrip("#").strip()
                current_content = []
            elif current_title:
                current_content.append(line)
        
        if current_title:
            sections[current_title] = "\n".join(current_content)
        
        return sections
    
    def run(self) -> None:
        """Run the documentation import process."""
        try:
            console.print("\n🚀 Starting documentation import...\n", style="bold blue")
            
            self.setup_directory_structure()
            self.import_tech_stack_docs()
            self.import_roadmap()
            self.import_agent_prompts()
            self.import_meta_prompts()
            
            console.print("\n✨ Documentation import completed successfully!\n", style="bold green")
            
            self.logger.info("Documentation import completed")
        
        except Exception as e:
            self.logger.error(f"Error during import: {str(e)}")
            console.print(f"\n❌ An error occurred: {str(e)}\n", style="bold red")
            raise

if __name__ == "__main__":
    importer = DocumentationImporter()
    importer.run() 