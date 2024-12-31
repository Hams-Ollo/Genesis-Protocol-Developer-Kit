# Technology Stack Documentation

## Archetype-Specific Tech Stacks

### Alchemist Class Stack

```yaml
core_ml:
  - TensorFlow/PyTorch: Deep learning frameworks
  - Scikit-learn: Traditional ML algorithms
  - XGBoost: Gradient boosting
  - Optuna: Hyperparameter optimization

experiment_management:
  - MLflow: Experiment tracking
  - DVC: Data version control
  - Weights & Biases: Experiment visualization
  - Sacred: Experiment organization

development:
  - Jupyter: Interactive development
  - VS Code: IDE with ML extensions
  - Git LFS: Large file storage
  - Docker: Containerization
```

### Sentinel Class Stack

```yaml
security:
  - OWASP ZAP: Security testing
  - Snyk: Dependency scanning
  - Vault: Secrets management
  - Keycloak: Authentication

monitoring:
  - Prometheus: Metrics collection
  - Grafana: Visualization
  - ELK Stack: Log management
  - New Relic: APM

infrastructure:
  - Kubernetes: Container orchestration
  - Istio: Service mesh
  - Terraform: Infrastructure as code
  - Ansible: Configuration management
```

### Oracle Class Stack

```yaml
data_processing:
  - Apache Spark: Large-scale processing
  - Pandas: Data manipulation
  - NumPy: Numerical computing
  - Dask: Parallel computing

analytics:
  - Tableau: Business intelligence
  - PowerBI: Data visualization
  - Streamlit: Data apps
  - Plotly: Interactive plots

storage:
  - PostgreSQL: Relational database
  - MongoDB: Document store
  - Redis: Cache layer
  - MinIO: Object storage
```

### Engineer Class Stack

```yaml
backend:
  - FastAPI: API framework
  - SQLAlchemy: ORM
  - Celery: Task queue
  - RabbitMQ: Message broker

devops:
  - GitHub Actions: CI/CD
  - ArgoCD: GitOps
  - Prometheus: Monitoring
  - Grafana: Dashboards

infrastructure:
  - AWS/GCP/Azure: Cloud platforms
  - Terraform: IaC
  - Docker: Containerization
  - Kubernetes: Orchestration
```

### Innovator Class Stack

```yaml
ai_services:
  - LangChain: LLM framework
  - OpenAI: GPT integration
  - Hugging Face: Model hub
  - Vertex AI: ML platform

prototyping:
  - Streamlit: Rapid UI
  - FastAPI: Quick APIs
  - SQLite: Local database
  - Redis: Caching

monitoring:
  - Weights & Biases: ML monitoring
  - Grafana: Dashboards
  - Sentry: Error tracking
  - DataDog: APM
```

### Lorekeeper Class Stack

```yaml
search:
  - Elasticsearch: Search engine
  - MeiliSearch: Fast search
  - Algolia: Search as service
  - Typesense: Instant search

knowledge_management:
  - Neo4j: Graph database
  - Apache Jena: RDF store
  - GraphQL: API layer
  - D3.js: Visualization

content:
  - GitBook: Documentation
  - MkDocs: Technical docs
  - Confluence: Team wiki
  - Docusaurus: Developer portal
```

## Common Infrastructure

### Development Tools

```yaml
ide:
  - VS Code
  - PyCharm
  - Jupyter Lab

version_control:
  - Git
  - GitHub/GitLab
  - Pre-commit hooks

quality:
  - Black: Formatting
  - Ruff: Linting
  - MyPy: Type checking
  - Pytest: Testing
```

### Deployment

```yaml
containers:
  - Docker
  - Kubernetes
  - Helm

ci_cd:
  - GitHub Actions
  - Jenkins
  - GitLab CI

monitoring:
  - Prometheus
  - Grafana
  - ELK Stack
```

### Security

```yaml
authentication:
  - OAuth 2.0
  - JWT
  - OIDC

tools:
  - OWASP ZAP
  - SonarQube
  - Snyk
  - Trivy
```

## Version Requirements

### Python Dependencies

```yaml
core:
  python: ">=3.8"
  pip: ">=21.0"
  virtualenv: ">=20.0"

frameworks:
  fastapi: ">=0.100.0"
  pydantic: ">=2.0.0"
  sqlalchemy: ">=2.0.0"
  
ml:
  tensorflow: ">=2.13.0"
  pytorch: ">=2.0.0"
  scikit-learn: ">=1.3.0"
```

### Infrastructure

```yaml
containers:
  docker: ">=24.0"
  kubernetes: ">=1.27"
  helm: ">=3.12"

databases:
  postgresql: ">=15.0"
  mongodb: ">=6.0"
  redis: ">=7.0"
```
