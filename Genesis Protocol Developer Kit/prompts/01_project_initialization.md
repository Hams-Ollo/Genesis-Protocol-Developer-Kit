# Project Initialization Prompts

## Character Creation System

### Archetype Selection

When guiding users through archetype selection, consider these aspects:

#### Alchemist Class

```yaml
focus: "Experimental ML/AI Research"
traits:
  - Innovation-driven
  - Research-oriented
  - Experimental mindset
questions:
  - "What type of ML/AI research are you focusing on?"
  - "Do you need experiment tracking capabilities?"
  - "Will you be working with multiple ML frameworks?"
```

#### Sentinel Class

```yaml
focus: "Security and Performance"
traits:
  - Security-conscious
  - Performance-critical
  - Compliance-focused
questions:
  - "What security standards must you comply with?"
  - "What are your performance requirements?"
  - "Do you need real-time monitoring?"
```

#### Oracle Class

```yaml
focus: "Data Analytics and Insights"
traits:
  - Data-driven
  - Analytics-focused
  - Insight-generating
questions:
  - "What types of data will you be analyzing?"
  - "Do you need real-time analytics capabilities?"
  - "Will you be implementing AI agents?"
```

#### Engineer Class

```yaml
focus: "System Architecture"
traits:
  - Infrastructure-focused
  - Scalability-oriented
  - DevOps-driven
questions:
  - "What cloud platforms will you be using?"
  - "Do you need multi-region deployment?"
  - "What CI/CD pipelines are required?"
```

#### Innovator Class

```yaml
focus: "Cutting-Edge Technology"
traits:
  - Forward-thinking
  - Prototype-driven
  - Technology-exploring
questions:
  - "What emerging technologies are you exploring?"
  - "Do you need rapid prototyping capabilities?"
  - "How will you measure innovation success?"
```

#### Lorekeeper Class

```yaml
focus: "Knowledge Management"
traits:
  - Information-organizing
  - Knowledge-preserving
  - Search-optimizing
questions:
  - "What type of knowledge are you managing?"
  - "Do you need advanced search capabilities?"
  - "Will you implement taxonomies?"
```

### Technology Selection

For each archetype, consider these technology categories:

```yaml
core_technologies:
  - Development frameworks
  - Database systems
  - API integrations
  - Testing tools

ai_capabilities:
  - ML frameworks
  - NLP tools
  - Vector databases
  - Model serving

infrastructure:
  - Cloud platforms
  - Containerization
  - Orchestration
  - Monitoring

security:
  - Authentication
  - Authorization
  - Encryption
  - Compliance tools
```

### Project Structure Generation

Generate appropriate directory structures based on archetype:

```yaml
common_directories:
  - src/
  - tests/
  - docs/
  - config/
  - scripts/

archetype_specific:
  alchemist:
    - experiments/
    - research/
    - models/
  sentinel:
    - security/
    - monitoring/
    - compliance/
  oracle:
    - analytics/
    - insights/
    - vectors/
  engineer:
    - architecture/
    - infrastructure/
    - workflows/
  innovator:
    - prototypes/
    - labs/
    - showcase/
  lorekeeper:
    - archives/
    - indices/
    - taxonomies/
```

### Configuration Templates

Provide archetype-specific configuration templates:

```yaml
config_files:
  - .env
  - requirements.txt
  - docker-compose.yml
  - README.md
  - setup.py
```

### Next Steps Guidance

Provide archetype-specific next steps:

```yaml
next_steps:
  alchemist:
    - Set up experiment tracking
    - Configure ML pipelines
    - Initialize notebooks
  sentinel:
    - Configure security scanning
    - Set up monitoring
    - Implement compliance checks
  oracle:
    - Set up data pipelines
    - Configure analytics
    - Initialize AI agents
  engineer:
    - Set up infrastructure
    - Configure CI/CD
    - Initialize monitoring
  innovator:
    - Set up development environment
    - Configure prototyping tools
    - Initialize benchmarking
  lorekeeper:
    - Set up knowledge base
    - Configure search
    - Initialize taxonomies
```
