# Centralized Online Learning Platform - Comprehensive 42 Curated Courses Data

COURSES_DATA = [
    # 1. DevOps & Cloud (Courses 1 - 8)
    {
        "title": "DevOps Engineering & Automated CI/CD Pipelines",
        "category": "Cloud & DevOps",
        "instructor": "Dr. Arvind Ramesh",
        "duration": "8 Weeks (40 Hours)",
        "description": "Master continuous integration and continuous deployment pipelines using Git, Jenkins, Docker, and Ansible. Designed for software engineers transitioning to cloud infrastructure.",
        "learning_objectives": "- Understand Version Control and Git branching strategies\n- Build automated CI pipelines using Jenkins\n- Containerize multi-tier applications with Docker\n- Automate server configuration with Ansible\n- Monitor production infrastructure and deployment logs",
        "is_published": True,
        "lessons": [
            {
                "title": "Introduction to Modern DevOps Culture & Lifecycle",
                "content": "DevOps combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality.\n\nKey pillars include shared responsibility, pervasive automation, and continuous feedback loops.",
                "resource_url": "https://www.atlassian.com/devops"
            },
            {
                "title": "Version Control Architecture & Git Branching Workflows",
                "content": "Version control is the bedrock of automated CI/CD. In this lesson, we study trunk-based development versus GitFlow.\n\nFeature branches allow isolated development before merging into the main branch via code reviews and automated tests.",
                "resource_url": "https://git-scm.com/book/en/v2"
            },
            {
                "title": "Containerization Fundamentals with Docker",
                "content": "Docker packages applications with their exact dependencies into lightweight, isolated containers. This eliminates the 'works on my machine' issue across test and production environments.",
                "resource_url": "https://docs.docker.com/get-started/"
            },
            {
                "title": "Jenkins Pipeline as Code (Jenkinsfile)",
                "content": "Declarative Jenkinsfiles define automated build, test, and deploy stages directly inside the repository alongside application source code.\n\nStages include checkout, build, pytest execution, and deployment triggers.",
                "resource_url": "https://www.jenkins.io/doc/book/pipeline/"
            },
            {
                "title": "Configuration Management & Automation with Ansible",
                "content": "Ansible allows declarative infrastructure automation via agentless SSH connections. Playbooks written in YAML configure target servers, install packages, and ensure desired runtime states repeatably.",
                "resource_url": "https://docs.ansible.com/"
            }
        ]
    },
    {
        "title": "Kubernetes Microservices Architecture & Orchestration",
        "category": "Cloud & DevOps",
        "instructor": "Kelsey Hightower",
        "duration": "7 Weeks (35 Hours)",
        "description": "Learn production container orchestration using Kubernetes. Master Deployments, Pods, Services, Ingress Controllers, ConfigMaps, and Helm package management.",
        "learning_objectives": "- Deploy containerized microservices to Kubernetes clusters\n- Configure ClusterIP, NodePort, and LoadBalancer services\n- Manage environment configs using ConfigMaps and Secrets\n- Package applications using Helm charts\n- Perform zero-downtime rolling updates and rollbacks",
        "is_published": True,
        "lessons": [
            {
                "title": "Kubernetes Architecture: Control Plane and Worker Nodes",
                "content": "Kubernetes cluster architecture consists of the Control Plane (API server, etcd, scheduler, controller manager) and Worker Nodes running kubelet, kube-proxy, and the container runtime engine.",
                "resource_url": "https://kubernetes.io/docs/concepts/overview/components/"
            },
            {
                "title": "Pods, Deployments, and ReplicaSets",
                "content": "Pods are the smallest deployable units in Kubernetes. Deployments manage declarative updates for Pods and ReplicaSets, enabling self-healing applications and smooth horizontal scaling.",
                "resource_url": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/"
            },
            {
                "title": "Networking: Services and Ingress Controllers",
                "content": "Services provide stable IP addressing and load balancing across dynamic ephemeral pods. Ingress controllers expose HTTP/HTTPS routes from outside the cluster to internal services.",
                "resource_url": "https://kubernetes.io/docs/concepts/services-networking/service/"
            },
            {
                "title": "Helm Package Manager for Kubernetes",
                "content": "Helm simplifies deploying complex multi-tier applications by bundling YAML definitions into reusable, versioned charts with configurable values files.",
                "resource_url": "https://helm.sh/docs/"
            }
        ]
    },
    {
        "title": "Infrastructure as Code with Terraform",
        "category": "Cloud & DevOps",
        "instructor": "Dr. Martin Odersky",
        "duration": "5 Weeks (25 Hours)",
        "description": "Automate cloud provisioning on AWS, Azure, and GCP using HashiCorp Terraform. Learn declarative syntax, state management, modules, and CI/CD automation.",
        "learning_objectives": "- Write HCL (HashiCorp Configuration Language) templates\n- Manage remote state backends with S3 and DynamoDB locking\n- Build reusable modular infrastructure components\n- Integrate Terraform with automated pull request pipelines",
        "is_published": True,
        "lessons": [
            {
                "title": "Introduction to Infrastructure as Code and Terraform",
                "content": "Infrastructure as Code treats server and network provisioning like software code. Terraform allows declarative resource creation using providers and state files.",
                "resource_url": "https://developer.hashicorp.com/terraform/intro"
            },
            {
                "title": "Terraform State Management and Locking",
                "content": "Terraform keeps track of real-world resources in a state file. In collaborative teams, state files are stored in remote backends like AWS S3 with state locking via DynamoDB to prevent concurrent collision.",
                "resource_url": "https://developer.hashicorp.com/terraform/language/state"
            },
            {
                "title": "Reusable Infrastructure Modules",
                "content": "Modules are containers for multiple resources that are used together. Creating custom modules promotes DRY principles and standardization across engineering teams.",
                "resource_url": "https://developer.hashicorp.com/terraform/language/modules"
            }
        ]
    },
    {
        "title": "AWS Cloud Solutions Architect Practitioner",
        "category": "Cloud & DevOps",
        "instructor": "Stephane Maarek",
        "duration": "8 Weeks (40 Hours)",
        "description": "Comprehensive preparation for designing resilient, high-performing, and cost-optimized architectures on Amazon Web Services.",
        "learning_objectives": "- Design scalable architectures with EC2, Auto Scaling, and ALB\n- Configure secure Virtual Private Clouds (VPC), Subnets, and Gateways\n- Store data efficiently using S3, EBS, and RDS\n- Implement Identity and Access Management (IAM) policies",
        "is_published": True,
        "lessons": [
            {
                "title": "AWS Global Infrastructure and IAM",
                "content": "Explore AWS Regions, Availability Zones, and Edge Locations. Configure IAM users, roles, and least-privilege security policies.",
                "resource_url": "https://aws.amazon.com/about-aws/global-infrastructure/"
            },
            {
                "title": "Virtual Private Cloud (VPC) Architecture",
                "content": "Design isolated virtual networks in the cloud. Create public/private subnets, internet gateways, NAT gateways, route tables, and network security groups.",
                "resource_url": "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html"
            },
            {
                "title": "Compute, Elastic Load Balancing, and Auto Scaling",
                "content": "Deploy scalable applications using Amazon EC2 instances fronted by Application Load Balancers and managed by Auto Scaling Groups that respond to CloudWatch metrics.",
                "resource_url": "https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html"
            }
        ]
    },
    {
        "title": "GitLab CI/CD & Automated Testing Pipelines",
        "category": "Cloud & DevOps",
        "instructor": "Nadia Eghbal",
        "duration": "4 Weeks (20 Hours)",
        "description": "Build end-to-end continuous integration pipelines using GitLab CI. Configure runners, cache dependencies, run Docker-in-Docker, and deploy to staging environments.",
        "learning_objectives": "- Write .gitlab-ci.yml configuration pipelines\n- Register and optimize self-hosted GitLab Runners\n- Configure artifact caching to accelerate build speeds\n- Implement security scanning and linting stages",
        "is_published": True,
        "lessons": [
            {
                "title": "GitLab CI Pipeline Basics and YAML Syntax",
                "content": "Learn how the .gitlab-ci.yml file defines stages, jobs, scripts, and variables to execute automated checks on every commit or pull request.",
                "resource_url": "https://docs.gitlab.com/ee/ci/yaml/"
            },
            {
                "title": "GitLab Runners and Execution Environments",
                "content": "Understand shared versus specific runners, executor types (Shell, Docker, Kubernetes), and concurrency management.",
                "resource_url": "https://docs.gitlab.com/runner/"
            },
            {
                "title": "Caching, Artifacts, and Environment Deployments",
                "content": "Differentiate between build caches (persisted between jobs) and downloadable artifacts. Configure automated deployments to review apps and staging servers.",
                "resource_url": "https://docs.gitlab.com/ee/ci/caching/"
            }
        ]
    },
    {
        "title": "Site Reliability Engineering (SRE) & Chaos Engineering",
        "category": "Cloud & DevOps",
        "instructor": "Benjamin Treynor Sloss",
        "duration": "6 Weeks (30 Hours)",
        "description": "Adopt Google's SRE principles. Learn Service Level Objectives (SLOs), Service Level Indicators (SLIs), Error Budgets, and chaos engineering simulations.",
        "learning_objectives": "- Define quantifiable SLIs and SLOs for production services\n- Manage error budgets to balance reliability and velocity\n- Perform blameless postmortems after system outages\n- Simulate failures using Chaos Mesh and Gremlin",
        "is_published": True,
        "lessons": [
            {
                "title": "SLIs, SLOs, and Error Budget Management",
                "content": "Learn how SREs quantify acceptable system unreliability. Error budgets align software development velocity with business reliability targets.",
                "resource_url": "https://sre.google/sre-book/service-level-objectives/"
            },
            {
                "title": "Incident Management and Blameless Postmortems",
                "content": "Establish effective on-call rotations, incident command hierarchies, and blameless retrospectives that focus on systemic resilience rather than human error.",
                "resource_url": "https://sre.google/sre-book/postmortem-culture/"
            },
            {
                "title": "Principles of Chaos Engineering",
                "content": "Proactively test distributed systems by injecting controlled latency, packet loss, and pod termination to ensure graceful degradation.",
                "resource_url": "https://principlesofchaos.org/"
            }
        ]
    },
    {
        "title": "Prometheus & Grafana Cloud Observability",
        "category": "Cloud & DevOps",
        "instructor": "Julius Volz",
        "duration": "5 Weeks (25 Hours)",
        "description": "Build real-time monitoring and alerting stacks for cloud services. Master PromQL queries, Node Exporter, custom metrics instrumentation, and Grafana dashboards.",
        "learning_objectives": "- Instrument Python and Go applications with Prometheus client libraries\n- Write PromQL queries for rates, histograms, and percentiles\n- Build executive and operations dashboards in Grafana\n- Configure Alertmanager with Slack and PagerDuty integration",
        "is_published": True,
        "lessons": [
            {
                "title": "Prometheus Time-Series Architecture",
                "content": "Prometheus collects metrics from target systems via pull-based HTTP scrapers, storing multidimensional time-series data indexed by metric name and key-value labels.",
                "resource_url": "https://prometheus.io/docs/introduction/overview/"
            },
            {
                "title": "Mastering PromQL (Prometheus Query Language)",
                "content": "Construct PromQL queries to calculate rates of change, percentiles, error rates, and CPU utilization across clusters.",
                "resource_url": "https://prometheus.io/docs/prometheus/latest/querying/basics/"
            },
            {
                "title": "Designing Rich Grafana Dashboards",
                "content": "Connect Prometheus data sources to Grafana. Build interactive panels, time-series graphs, and alerting notification rules.",
                "resource_url": "https://grafana.com/docs/grafana/latest/"
            }
        ]
    },
    {
        "title": "Serverless Architecture on AWS Lambda & API Gateway",
        "category": "Cloud & DevOps",
        "instructor": "Yan Cui",
        "duration": "4 Weeks (20 Hours)",
        "description": "Design event-driven, cost-effective serverless backends using AWS Lambda, DynamoDB, Amazon EventBridge, and the Serverless Framework.",
        "learning_objectives": "- Build micro-services without provisioning servers\n- Configure synchronous and asynchronous event triggers\n- Optimize cold starts and memory allocation\n- Implement distributed tracing with AWS X-Ray",
        "is_published": True,
        "lessons": [
            {
                "title": "Event-Driven Serverless Fundamentals",
                "content": "Learn how serverless architectures run stateless compute functions in response to HTTP requests, database stream updates, or message queue events.",
                "resource_url": "https://aws.amazon.com/serverless/"
            },
            {
                "title": "AWS Lambda and API Gateway Integration",
                "content": "Expose REST endpoints using API Gateway backed by Python Lambda functions. Handle authorization, CORS, and response formatting.",
                "resource_url": "https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html"
            },
            {
                "title": "State Management with Amazon DynamoDB",
                "content": "Model single-table NoSQL schemas in DynamoDB for high-throughput, low-latency persistence in serverless applications.",
                "resource_url": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html"
            }
        ]
    },

    # 2. Web Development (Courses 9 - 16)
    {
        "title": "Full-Stack Python Web Development with Flask & SQLite",
        "category": "Web Development",
        "instructor": "Prof. Sarah Jenkins",
        "duration": "6 Weeks (30 Hours)",
        "description": "Learn how to build production-grade web applications from scratch using Python Flask, SQLAlchemy ORM, WTForms, secure session management, and responsive Bootstrap UI.",
        "learning_objectives": "- Architect modular Flask applications with Blueprints and Application Factories\n- Model relational databases using SQLAlchemy ORM\n- Implement secure authentication and role-based access control\n- Build responsive frontend interfaces with Bootstrap 5\n- Write unit and integration test suites using Pytest",
        "is_published": True,
        "lessons": [
            {
                "title": "Flask Application Architecture & Factory Pattern",
                "content": "The application factory pattern allows creating multiple instances of a Flask app with distinct configurations (Development, Testing, Production).",
                "resource_url": "https://flask.palletsprojects.com/en/latest/patterns/appfactories/"
            },
            {
                "title": "Relational Modeling with Flask-SQLAlchemy",
                "content": "SQLAlchemy abstracts database interactions using Object-Relational Mapping (ORM). Map Python classes to SQL tables and execute parameterized queries.",
                "resource_url": "https://flask-sqlalchemy.palletsprojects.com/"
            },
            {
                "title": "User Authentication & Session Security",
                "content": "Security is paramount. Hash passwords using Werkzeug PBKDF2/scrypt and protect cookies using HttpOnly and SameSite flags.",
                "resource_url": "https://owasp.org/www-project-top-ten/"
            },
            {
                "title": "Responsive UI Design with Bootstrap 5 & Chart.js",
                "content": "Design modern user interfaces using Bootstrap 5 grid systems and embed interactive Chart.js graphs for visual analytics.",
                "resource_url": "https://getbootstrap.com/docs/5.3/"
            }
        ]
    },
    {
        "title": "FastAPI: High-Performance Modern Python Web APIs",
        "category": "Web Development",
        "instructor": "Tiangolo Ramirez",
        "duration": "5 Weeks (25 Hours)",
        "description": "Build asynchronous, high-throughput REST APIs using Python FastAPI, Pydantic data validation, async SQLAlchemy, and automatic OpenAPI Swagger documentation.",
        "learning_objectives": "- Leverage asynchronous Python (async/await) for high I/O throughput\n- Validate request payloads with Pydantic schemas\n- Implement JWT token authorization\n- Generate interactive Swagger and ReDoc documentation",
        "is_published": True,
        "lessons": [
            {
                "title": "Getting Started with FastAPI and Pydantic",
                "content": "FastAPI is a modern, fast web framework for building APIs with Python 3.8+ based on standard Python type hints and Pydantic validation.",
                "resource_url": "https://fastapi.tiangolo.com/"
            },
            {
                "title": "Dependency Injection and Security with OAuth2 & JWT",
                "content": "Implement modular authentication using FastAPI's built-in dependency injection system and signed JSON Web Tokens.",
                "resource_url": "https://fastapi.tiangolo.com/tutorial/security/"
            },
            {
                "title": "Asynchronous Database Access with asyncpg",
                "content": "Connect asynchronous endpoints to PostgreSQL using async SQLAlchemy to achieve maximum concurrent request throughput.",
                "resource_url": "https://fastapi.tiangolo.com/tutorial/sql-databases/"
            }
        ]
    },
    {
        "title": "Django Enterprise Web Framework Mastery",
        "category": "Web Development",
        "instructor": "William S. Vincent",
        "duration": "8 Weeks (40 Hours)",
        "description": "The batteries-included Python web framework. Master Django ORM, Admin interface, Class-Based Views, middleware, form validation, and caching layers.",
        "learning_objectives": "- Structure scalable Django applications\n- Utilize the Django Admin portal for content management\n- Implement custom middleware and authentication backends\n- Optimize database queries with select_related and prefetch_related",
        "is_published": True,
        "lessons": [
            {
                "title": "The Django MTV (Model-Template-View) Pattern",
                "content": "Understand how Django routes HTTP requests from urls.py to views, queries the database via ORM models, and renders context templates.",
                "resource_url": "https://docs.djangoproject.com/en/stable/intro/tutorial01/"
            },
            {
                "title": "Django ORM Deep Dive and Query Optimization",
                "content": "Prevent N+1 query performance problems using select_related for foreign keys and prefetch_related for many-to-many relationships.",
                "resource_url": "https://docs.djangoproject.com/en/stable/topics/db/optimization/"
            },
            {
                "title": "Django REST Framework (DRF) Serialization",
                "content": "Transform Django models into JSON REST APIs with model serializers, viewsets, and permission classes.",
                "resource_url": "https://www.django-rest-framework.org/"
            }
        ]
    },
    {
        "title": "Modern JavaScript ES6+ & Asynchronous Programming",
        "category": "Web Development",
        "instructor": "Kyle Simpson",
        "duration": "5 Weeks (25 Hours)",
        "description": "Master core JavaScript fundamentals: closures, prototypes, event loops, promises, async/await, modules, and functional programming concepts.",
        "learning_objectives": "- Master the JavaScript event loop and call stack\n- Write clean asynchronous code with Promises and async/await\n- Understand lexical scope, hoisting, and closures\n- Manipulate the DOM securely without security flaws",
        "is_published": True,
        "lessons": [
            {
                "title": "Scope, Closures, and Execution Context",
                "content": "Deep dive into how the JavaScript engine parses scope chains, manages memory closures, and resolves variable bindings.",
                "resource_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures"
            },
            {
                "title": "The JavaScript Event Loop and Asynchronous Execution",
                "content": "Demystify microtasks, macrotasks, Promise resolution, and the browser rendering cycle.",
                "resource_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop"
            },
            {
                "title": "ES6 Modules, Destructuring, and Modern Patterns",
                "content": "Organize frontend architecture using native ES modules, spread operators, optional chaining, and nullish coalescing.",
                "resource_url": "https://javascript.info/modules-intro"
            }
        ]
    },
    {
        "title": "Responsive Web Design with Bootstrap 5 & CSS Grid",
        "category": "Web Development",
        "instructor": "Rachel Andrew",
        "duration": "4 Weeks (20 Hours)",
        "description": "Design accessible, mobile-first responsive web applications using Bootstrap 5 utility classes, flexbox, CSS Grid, and custom CSS variables.",
        "learning_objectives": "- Build responsive mobile-first multi-column layouts\n- Leverage Bootstrap 5 components: modals, cards, navbars, and toasts\n- Implement CSS Grid for complex dimensional UI design\n- Ensure WCAG 2.1 accessibility compliance",
        "is_published": True,
        "lessons": [
            {
                "title": "Mobile-First CSS Grid and Flexbox Layouts",
                "content": "Learn how modern CSS flexbox handles 1D layout distribution while CSS Grid creates powerful 2D responsive matrix layouts.",
                "resource_url": "https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout"
            },
            {
                "title": "Bootstrap 5 Grid System and Breakpoints",
                "content": "Harness Bootstrap's 12-column grid system, container classes, and responsive breakpoint prefixes (sm, md, lg, xl, xxl).",
                "resource_url": "https://getbootstrap.com/docs/5.3/layout/grid/"
            },
            {
                "title": "CSS Custom Properties (Variables) and Theming",
                "content": "Create dark and light themes dynamically using CSS custom properties with smooth transitions and contrast validation.",
                "resource_url": "https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties"
            }
        ]
    },
    {
        "title": "RESTful API Design & OpenAPI Documentation Standards",
        "category": "Web Development",
        "instructor": "Leonard Richardson",
        "duration": "4 Weeks (20 Hours)",
        "description": "Architect clean, scalable RESTful web APIs following Richardson Maturity Model, HTTP status code semantics, pagination, versioning, and OpenAPI 3.0 specs.",
        "learning_objectives": "- Design intuitive URI endpoints adhering to REST principles\n- Select correct HTTP methods and status codes\n- Implement cursor-based and offset-based pagination\n- Document API contracts using OpenAPI specification",
        "is_published": True,
        "lessons": [
            {
                "title": "The Richardson Maturity Model & HTTP Semantics",
                "content": "Understand the 4 levels of REST maturity: URI resources, standard HTTP verbs, and HATEOAS hypermedia controls.",
                "resource_url": "https://martinfowler.com/articles/richardsonMaturityModel.html"
            },
            {
                "title": "Filtering, Sorting, and Pagination Strategies",
                "content": "Design query parameters for complex API filtering, sorting multi-attribute payloads, and handling pagination headers.",
                "resource_url": "https://restfulapi.net/"
            },
            {
                "title": "OpenAPI / Swagger Specification Specifications",
                "content": "Author machine-readable OpenAPI definitions to generate client SDKs, automated mock servers, and interactive docs.",
                "resource_url": "https://swagger.io/specification/"
            }
        ]
    },
    {
        "title": "Web Performance Optimization & Core Web Vitals",
        "category": "Web Development",
        "instructor": "Addy Osmani",
        "duration": "5 Weeks (25 Hours)",
        "description": "Optimize web page load speeds and user experience. Master Critical Rendering Path, asset compression, lazy loading, caching strategies, and Core Web Vitals.",
        "learning_objectives": "- Diagnose bottlenecks with Chrome DevTools and Lighthouse\n- Optimize Largest Contentful Paint (LCP) and Cumulative Layout Shift (CLS)\n- Configure Brotli/Gzip compression and HTTP/2 multiplexing\n- Implement resource hints: preload, prefetch, and preconnect",
        "is_published": True,
        "lessons": [
            {
                "title": "Understanding the Critical Rendering Path",
                "content": "Trace how browsers parse HTML into DOM, CSS into CSSOM, create render trees, and execute layout and paint stages.",
                "resource_url": "https://web.dev/critical-rendering-path/"
            },
            {
                "title": "Mastering Core Web Vitals (LCP, FID/INP, CLS)",
                "content": "Measure user-centric performance metrics and optimize assets to pass Google Core Web Vitals benchmarks.",
                "resource_url": "https://web.dev/vitals/"
            },
            {
                "title": "HTTP Caching and Service Worker Offline Strategies",
                "content": "Implement Cache-Control, ETag headers, and Progressive Web App service workers for instantaneous page loads.",
                "resource_url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching"
            }
        ]
    },
    {
        "title": "Interactive Data Visualization with Chart.js",
        "category": "Web Development",
        "instructor": "Evert Timberg",
        "duration": "4 Weeks (20 Hours)",
        "description": "Transform raw analytical data into interactive dashboards using HTML5 Canvas and Chart.js. Build responsive bar, line, radar, and doughnut charts.",
        "learning_objectives": "- Render performant canvas graphs from database queries\n- Customize chart animations, tooltips, and legends\n- Update chart datasets dynamically via AJAX/Fetch API\n- Design accessible chart alternatives for screen readers",
        "is_published": True,
        "lessons": [
            {
                "title": "Chart.js Architecture and Canvas Rendering",
                "content": "Learn how Chart.js uses HTML5 2D canvas context to render hardware-accelerated interactive visualizations.",
                "resource_url": "https://www.chartjs.org/docs/latest/"
            },
            {
                "title": "Multi-Dataset Charts and Dynamic Updates",
                "content": "Bind real-time JSON endpoint data to line and bar charts using modern asynchronous JavaScript fetch calls.",
                "resource_url": "https://www.chartjs.org/docs/latest/developers/updates.html"
            },
            {
                "title": "Creating Analytics Dashboards with Bootstrap Grid",
                "content": "Combine Chart.js canvas elements inside Bootstrap 5 cards to build executive-ready business dashboards.",
                "resource_url": "https://www.chartjs.org/docs/latest/samples/"
            }
        ]
    },

    # 3. Cybersecurity (Courses 17 - 24)
    {
        "title": "Enterprise Cloud Security & Access Governance",
        "category": "Cybersecurity",
        "instructor": "Marcus Vance, CISSP",
        "duration": "5 Weeks (25 Hours)",
        "description": "In-depth cybersecurity fundamentals covering Role-Based Access Control (RBAC), secure secret management, zero-trust network boundaries, and automated vulnerability scanning.",
        "learning_objectives": "- Implement strict Role-Based Access Control on web backends\n- Manage sensitive environment variables and secrets safely\n- Prevent OWASP Top 10 vulnerabilities like SQLi, CSRF, and XSS\n- Audit and monitor administrative user actions",
        "is_published": True,
        "lessons": [
            {
                "title": "Foundations of Role-Based Access Control (RBAC)",
                "content": "Explore server-side permission checking versus client-side visibility toggles. Always enforce authorization decorators on backend endpoints to prevent privilege escalation.",
                "resource_url": "https://csrc.nist.gov/projects/role-based-access-control"
            },
            {
                "title": "Defending Against OWASP Top 10 Web Vulnerabilities",
                "content": "Examine common web attack vectors: Cross-Site Request Forgery (CSRF), SQL Injection, Cross-Site Scripting (XSS), and Broken Object Level Authorization.",
                "resource_url": "https://owasp.org/Top10/"
            },
            {
                "title": "Secure Secrets Management in CI/CD Environments",
                "content": "Never commit plaintext passwords, API keys, or private SSH keys into Git repositories. Use environment variables, secret managers, and automated secret scanners.",
                "resource_url": "https://12factor.net/config"
            }
        ]
    },
    {
        "title": "Ethical Hacking & Web Application Penetration Testing",
        "category": "Cybersecurity",
        "instructor": "Georgia Weidman",
        "duration": "8 Weeks (40 Hours)",
        "description": "Hands-on penetration testing methodologies using Kali Linux, Burp Suite, Nmap, and Metasploit. Discover, exploit, and patch real-world software flaws.",
        "learning_objectives": "- Conduct passive and active network reconnaissance\n- Intercept and manipulate HTTP traffic with Burp Suite Proxy\n- Exploit SQL injection and command injection vulnerabilities\n- Write comprehensive remediation reports for executive teams",
        "is_published": True,
        "lessons": [
            {
                "title": "Penetration Testing Methodology and Legal Frameworks",
                "content": "Learn the phases of a penetration test: scoping, reconnaissance, vulnerability scanning, exploitation, and post-exploitation documentation.",
                "resource_url": "https://www.ptes-technical.org/"
            },
            {
                "title": "Burp Suite Essentials: Intercepting and Fuzzing Requests",
                "content": "Configure Burp Suite as an HTTP proxy to analyze backend requests, test parameters with Intruder, and re-issue requests with Repeater.",
                "resource_url": "https://portswigger.net/burp/documentation"
            },
            {
                "title": "SQL Injection Identification and Remediation",
                "content": "Test for in-band, blind, and time-based SQL injections, and understand why ORM parameterized queries are the primary defense.",
                "resource_url": "https://portswigger.net/web-security/sql-injection"
            }
        ]
    },
    {
        "title": "Network Security & Cryptography Principles",
        "category": "Cybersecurity",
        "instructor": "Dr. Bruce Schneier",
        "duration": "6 Weeks (30 Hours)",
        "description": "Master cryptographic algorithms: symmetric AES, asymmetric RSA/ECC, SHA-256 hashing, digital signatures, TLS 1.3 handshakes, and PKI infrastructure.",
        "learning_objectives": "- Differentiate between symmetric and asymmetric encryption\n- Understand digital certificate chains and Certificate Authorities\n- Inspect TLS 1.3 handshakes using Wireshark packet captures\n- Secure passwords using PBKDF2, bcrypt, and Argon2",
        "is_published": True,
        "lessons": [
            {
                "title": "Symmetric vs. Asymmetric Encryption",
                "content": "Explore AES block ciphers for fast bulk encryption alongside RSA and Elliptic Curve Cryptography for key exchange and digital identity verification.",
                "resource_url": "https://csrc.nist.gov/projects/cryptographic-standards-and-applications"
            },
            {
                "title": "Public Key Infrastructure (PKI) and TLS 1.3",
                "content": "Understand how Certificate Authorities validate identity and how ephemeral Diffie-Hellman exchanges ensure Perfect Forward Secrecy in modern TLS.",
                "resource_url": "https://www.cloudflare.com/learning/ssl/what-is-tls/"
            },
            {
                "title": "Cryptographic Hash Functions and Salted Password Hashing",
                "content": "Analyze why SHA-256 is inadequate for passwords and how memory-hard key derivation functions like bcrypt and Argon2 defend against GPU attacks.",
                "resource_url": "https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html"
            }
        ]
    },
    {
        "title": "DevSecOps: Automated Security in CI/CD Pipelines",
        "category": "Cybersecurity",
        "instructor": "Shannon Lietz",
        "duration": "5 Weeks (25 Hours)",
        "description": "Shift security left! Integrate SAST, DAST, SCA dependency scanning, and container vulnerability audits into Jenkins and GitHub Actions pipelines.",
        "learning_objectives": "- Implement Static Application Security Testing (SAST) with SonarQube\n- Scan third-party dependencies with OWASP Dependency-Check and Snyk\n- Audit Docker images for CVEs using Trivy\n- Automate compliance guardrails in deployment pipelines",
        "is_published": True,
        "lessons": [
            {
                "title": "The DevSecOps Manifesto and Shift-Left Security",
                "content": "Integrate automated security gates early in the development lifecycle rather than performing isolated security reviews at the end of the release cycle.",
                "resource_url": "https://www.devsecops.org/"
            },
            {
                "title": "Static vs. Dynamic Application Security Testing",
                "content": "Compare SAST source code scanners with DAST runtime vulnerability scanners like OWASP ZAP.",
                "resource_url": "https://owasp.org/www-project-zap/"
            },
            {
                "title": "Container Vulnerability Auditing with Trivy",
                "content": "Scan Docker layers and base operating system packages for known CVEs before publishing container images to registries.",
                "resource_url": "https://aquasecurity.github.io/trivy/"
            }
        ]
    },
    {
        "title": "Zero Trust Architecture & Identity Federation",
        "category": "Cybersecurity",
        "instructor": "John Kindervag",
        "duration": "5 Weeks (25 Hours)",
        "description": "Never trust, always verify. Implement Zero Trust network perimeters, OAuth 2.0, OpenID Connect, SAML, and Multi-Factor Authentication (MFA).",
        "learning_objectives": "- Transition from perimeter-based firewalls to Zero Trust architecture\n- Implement Single Sign-On (SSO) with OpenID Connect\n- Enforce context-aware access policies and Device Health verification\n- Configure Time-based One-Time Password (TOTP) MFA",
        "is_published": True,
        "lessons": [
            {
                "title": "Core Tenets of Zero Trust Architecture",
                "content": "Assume breach and treat all network traffic as untrusted regardless of whether it originates inside or outside enterprise perimeters.",
                "resource_url": "https://www.nist.gov/publications/zero-trust-architecture"
            },
            {
                "title": "OAuth 2.0 and OpenID Connect (OIDC) Protocols",
                "content": "Understand authorization grant flows: Authorization Code with PKCE, Access Tokens, ID Tokens, and Refresh Tokens.",
                "resource_url": "https://auth0.com/intro-to-iam/what-is-oauth-2"
            },
            {
                "title": "Multi-Factor Authentication (MFA) & FIDO2 WebAuthn",
                "content": "Implement modern phishing-resistant authentication using WebAuthn public key credentials and hardware security tokens.",
                "resource_url": "https://fidoalliance.org/fido2/"
            }
        ]
    },
    {
        "title": "Incident Response & Digital Forensics (DFIR)",
        "category": "Cybersecurity",
        "instructor": "David Cowen",
        "duration": "6 Weeks (30 Hours)",
        "description": "Prepare for and investigate corporate cybersecurity breaches. Learn memory analysis with Volatility, disk forensics with Autopsy, and SIEM log correlation.",
        "learning_objectives": "- Execute NIST and SANS Incident Response phases\n- Acquire and preserve evidence following strict Chain of Custody\n- Analyze memory dumps for rootkits and injected DLLs\n- Hunt for Indicators of Compromise (IoCs) across SIEM logs",
        "is_published": True,
        "lessons": [
            {
                "title": "The Incident Response Lifecycle",
                "content": "Master the 6 steps of incident response: Preparation, Identification, Containment, Eradication, Recovery, and Lessons Learned.",
                "resource_url": "https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final"
            },
            {
                "title": "Volatile Memory Forensics with Volatility",
                "content": "Extract running processes, network connections, command histories, and decrypted credentials from RAM memory images.",
                "resource_url": "https://volatilityfoundation.org/"
            },
            {
                "title": "SIEM Log Analysis and Threat Hunting",
                "content": "Correlate syslog, web server, and authentication logs in Splunk or Elastic Security to reconstruct attacker lateral movement.",
                "resource_url": "https://www.elastic.co/security"
            }
        ]
    },
    {
        "title": "Secure Coding in Python & Software Supply Chain",
        "category": "Cybersecurity",
        "instructor": "Tanya Janca",
        "duration": "4 Weeks (20 Hours)",
        "description": "Write resilient Python applications resistant to injection attacks, deserialization exploits (pickle), timing attacks, and dependency confusion vulnerabilities.",
        "learning_objectives": "- Avoid insecure deserialization flaws with Python pickle\n- Implement constant-time string comparison to prevent timing attacks\n- Secure pip dependencies using hashes and requirements locking\n- Sanitize file upload pathways against path traversal exploits",
        "is_published": True,
        "lessons": [
            {
                "title": "Insecure Deserialization and Code Execution",
                "content": "Examine why Python's pickle module is inherently unsafe for untrusted input and adopt safe JSON or Protocol Buffer alternatives.",
                "resource_url": "https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data"
            },
            {
                "title": "File Upload Security and Path Traversal",
                "content": "Protect against path traversal and malicious executable upload by sanitizing filenames using secure_filename and checking magic bytes.",
                "resource_url": "https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html"
            },
            {
                "title": "Software Supply Chain Security & Dependency Pinning",
                "content": "Prevent typosquatting and supply chain attacks by using pip hash verification and automated software bill of materials (SBOM) tools.",
                "resource_url": "https://pip.pypa.io/en/stable/topics/secure-installs/"
            }
        ]
    },
    {
        "title": "Linux Server Hardening & Bastion Host Administration",
        "category": "Cybersecurity",
        "instructor": "Michael Boelen",
        "duration": "5 Weeks (25 Hours)",
        "description": "Harden Ubuntu and RHEL enterprise servers. Configure SSH key-only access, UFW/iptables firewalls, Fail2ban intrusion prevention, and Lynis security audits.",
        "learning_objectives": "- Lock down SSH daemon configuration against brute-force attacks\n- Configure stateful host firewalls and network segmentation\n- Implement automated intrusion blocking with Fail2ban\n- Run automated CIS benchmark compliance audits using Lynis",
        "is_published": True,
        "lessons": [
            {
                "title": "SSH Server Hardening and Key-Based Authentication",
                "content": "Disable root login, enforce public key authentication, configure non-standard ports, and enforce strong cipher suites in sshd_config.",
                "resource_url": "https://www.ssh.com/academy/ssh/sshd_config"
            },
            {
                "title": "Firewalling with UFW and iptables",
                "content": "Establish default-deny inbound firewall policies and open only required service ports (HTTP, HTTPS, SSH).",
                "resource_url": "https://help.ubuntu.com/community/UFW"
            },
            {
                "title": "Automated Security Auditing with Lynis",
                "content": "Perform comprehensive vulnerability scans on Linux systems to verify compliance with CIS and ISO 27001 security baselines.",
                "resource_url": "https://cisofy.com/lynis/"
            }
        ]
    },

    # 4. Data Science & AI (Courses 25 - 32)
    {
        "title": "Practical Data Science & Machine Learning with Python",
        "category": "Data Science & AI",
        "instructor": "Dr. Priya Sharma",
        "duration": "10 Weeks (50 Hours)",
        "description": "Hands-on exploration of data science workflows: exploratory data analysis, data cleansing, statistical modeling, machine learning algorithms, and deployment of predictive models.",
        "learning_objectives": "- Clean and analyze datasets using Pandas and NumPy\n- Build predictive regression and classification models\n- Evaluate model precision, recall, and ROC-AUC\n- Deploy ML models as REST API endpoints",
        "is_published": True,
        "lessons": [
            {
                "title": "Exploratory Data Analysis with Pandas & NumPy",
                "content": "Data ingestion, handling missing values, data normalization, and summary statistics to discover underlying patterns.",
                "resource_url": "https://pandas.pydata.org/"
            },
            {
                "title": "Supervised Machine Learning Algorithms",
                "content": "Training decision trees, random forests, and support vector machines for classification problems.",
                "resource_url": "https://scikit-learn.org/"
            },
            {
                "title": "Model Evaluation Metrics and Overfitting Prevention",
                "content": "Interpret confusion matrices, precision-recall curves, and apply k-fold cross-validation to prevent model overfitting.",
                "resource_url": "https://scikit-learn.org/stable/modules/model_evaluation.html"
            }
        ]
    },
    {
        "title": "Deep Learning & Neural Networks with PyTorch",
        "category": "Data Science & AI",
        "instructor": "Soumith Chintala",
        "duration": "8 Weeks (40 Hours)",
        "description": "Build modern deep learning models using PyTorch. Understand tensors, backpropagation, Convolutional Neural Networks (CNNs), and Recurrent Neural Networks (RNNs).",
        "learning_objectives": "- Understand computational graphs and autograd in PyTorch\n- Build CNNs for image classification and computer vision\n- Train sequence models for time-series forecasting\n- Leverage GPU acceleration with CUDA",
        "is_published": True,
        "lessons": [
            {
                "title": "PyTorch Tensors and Autograd Engine",
                "content": "Learn how PyTorch dynamically builds computational graphs and calculates gradients automatically through backpropagation.",
                "resource_url": "https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html"
            },
            {
                "title": "Convolutional Neural Networks (CNNs) for Vision",
                "content": "Explore convolutional filters, pooling layers, and transfer learning with pre-trained ResNet architectures.",
                "resource_url": "https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html"
            },
            {
                "title": "Training Pipelines, Loss Functions, and Optimizers",
                "content": "Configure training loops, Cross-Entropy loss, AdamW optimizers, and learning rate schedulers for neural network convergence.",
                "resource_url": "https://pytorch.org/docs/stable/optim.html"
            }
        ]
    },
    {
        "title": "Natural Language Processing (NLP) & Transformers",
        "category": "Data Science & AI",
        "instructor": "Dr. Christopher Manning",
        "duration": "7 Weeks (35 Hours)",
        "description": "Master natural language processing from word embeddings (Word2Vec) to self-attention mechanisms, BERT, GPT architectures, and Hugging Face Transformers.",
        "learning_objectives": "- Tokenize text data using Byte-Pair Encoding (BPE)\n- Understand Multi-Head Self-Attention mechanisms\n- Fine-tune pre-trained Transformer models with Hugging Face\n- Build sentiment analysis and question-answering systems",
        "is_published": True,
        "lessons": [
            {
                "title": "Text Preprocessing and Word Vector Representations",
                "content": "Learn tokenization, TF-IDF, and semantic word embeddings that capture vector relationships between linguistic concepts.",
                "resource_url": "https://nlp.stanford.edu/"
            },
            {
                "title": "The Transformer Architecture: Attention is All You Need",
                "content": "Deconstruct query, key, value matrices and multi-head self-attention that power modern Large Language Models.",
                "resource_url": "https://arxiv.org/abs/1706.03762"
            },
            {
                "title": "Fine-Tuning Models with Hugging Face Transformers",
                "content": "Fine-tune open-source models for domain-specific classification tasks using PyTorch and Hugging Face datasets.",
                "resource_url": "https://huggingface.co/docs/transformers/index"
            }
        ]
    },
    {
        "title": "Data Engineering Pipelines with Apache Airflow",
        "category": "Data Science & AI",
        "instructor": "Maxime Beauchemin",
        "duration": "6 Weeks (30 Hours)",
        "description": "Author, schedule, and monitor programmatic workflows using Apache Airflow. Build robust ETL data pipelines connecting SQL databases, APIs, and data lakes.",
        "learning_objectives": "- Define Directed Acyclic Graphs (DAGs) in Python\n- Schedule reliable batch data processing jobs\n- Manage task dependencies, retries, and failure alerts\n- Execute containerized tasks with KubernetesPodOperator",
        "is_published": True,
        "lessons": [
            {
                "title": "Airflow Core Concepts: DAGs, Operators, and Tasks",
                "content": "Learn how Airflow models workflows as DAGs where nodes represent task operations and edges define upstream/downstream execution order.",
                "resource_url": "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html"
            },
            {
                "title": "Building Resilient ETL Extraction and Transformation Tasks",
                "content": "Extract data from relational sources, transform data using Pandas, and load clean partitions into analytical storage.",
                "resource_url": "https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html"
            },
            {
                "title": "Airflow Scheduling, Catchup, and Monitoring",
                "content": "Configure cron-based execution intervals, handle data backfilling, and configure alerting webhooks for pipeline failures.",
                "resource_url": "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html"
            }
        ]
    },
    {
        "title": "Big Data Analytics with Apache Spark & PySpark",
        "category": "Data Science & AI",
        "instructor": "Matei Zaharia",
        "duration": "7 Weeks (35 Hours)",
        "description": "Process terabyte-scale distributed datasets with Apache Spark and PySpark. Master resilient distributed datasets (RDDs), Spark DataFrames, and Spark SQL.",
        "learning_objectives": "- Execute distributed computations across cluster worker nodes\n- Optimize Spark DataFrame transformations and joins\n- Prevent data skew and unnecessary memory shuffles\n- Query big data using Spark SQL syntax",
        "is_published": True,
        "lessons": [
            {
                "title": "Spark Cluster Architecture and In-Memory Computation",
                "content": "Explore how the Spark Driver coordinates distributed tasks across executors, performing lazy evaluation to optimize execution plans.",
                "resource_url": "https://spark.apache.org/docs/latest/cluster-overview.html"
            },
            {
                "title": "PySpark DataFrames and Spark SQL",
                "content": "Transform structured datasets using PySpark APIs and execute SQL queries on distributed tables.",
                "resource_url": "https://spark.apache.org/docs/latest/api/python/index.html"
            },
            {
                "title": "Partitioning and Shuffle Optimization",
                "content": "Optimize distributed joins and aggregations by partitioning data efficiently and avoiding wide shuffle dependencies.",
                "resource_url": "https://spark.apache.org/docs/latest/sql-performance-tuning.html"
            }
        ]
    },
    {
        "title": "MLOps: Machine Learning Operations & Model Deployment",
        "category": "Data Science & AI",
        "instructor": "Andrew Ng",
        "duration": "6 Weeks (30 Hours)",
        "description": "Bridge the gap between ML models and production systems. Track experiments with MLflow, version datasets with DVC, and deploy low-latency inference APIs.",
        "learning_objectives": "- Track model parameters, metrics, and artifacts with MLflow\n- Version datasets alongside code using Data Version Control (DVC)\n- Serve predictions using FastAPI and Docker containers\n- Detect data drift and model degradation in production",
        "is_published": True,
        "lessons": [
            {
                "title": "MLOps Lifecycle and Experiment Tracking with MLflow",
                "content": "Log training parameters, hyperparameters, loss curves, and serialized model binaries in a centralized registry.",
                "resource_url": "https://mlflow.org/docs/latest/index.html"
            },
            {
                "title": "Data and Pipeline Versioning with DVC",
                "content": "Version large datasets in cloud storage using Git-compatible hash pointers to guarantee reproducible machine learning pipelines.",
                "resource_url": "https://dvc.org/doc"
            },
            {
                "title": "Containerized Model Serving and Drift Monitoring",
                "content": "Package trained Scikit-learn and PyTorch models into Docker containers and monitor live predictions for distribution drift.",
                "resource_url": "https://christophergs.com/machine%20learning/2020/05/13/deploying-machine-learning-applications-in-production/"
            }
        ]
    },
    {
        "title": "Computer Vision & Image Processing with OpenCV",
        "category": "Data Science & AI",
        "instructor": "Dr. Adrian Rosebrock",
        "duration": "6 Weeks (30 Hours)",
        "description": "Process and analyze digital imagery using OpenCV and Python. Master color spaces, edge detection, contour analysis, face detection, and feature matching.",
        "learning_objectives": "- Manipulate image arrays and color spaces (RGB, HSV, Grayscale)\n- Apply Gaussian blurs, thresholding, and Canny edge detection\n- Detect and track objects in real-time video streams\n- Implement Haar cascades and deep learning face detectors",
        "is_published": True,
        "lessons": [
            {
                "title": "Digital Image Representation and OpenCV Basics",
                "content": "Understand pixels as multi-channel NumPy arrays, learn coordinate systems, and perform cropping and rotation transformations.",
                "resource_url": "https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html"
            },
            {
                "title": "Filtering, Edge Detection, and Morphological Operations",
                "content": "Apply spatial kernels to reduce camera noise, detect high-gradient edges, and dilate/erode binary masks.",
                "resource_url": "https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html"
            },
            {
                "title": "Contour Detection and Shape Analysis",
                "content": "Extract object boundaries from thresholded images and calculate perimeter, area, and bounding boxes for object tracking.",
                "resource_url": "https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html"
            }
        ]
    },
    {
        "title": "Time-Series Forecasting & Anomaly Detection",
        "category": "Data Science & AI",
        "instructor": "Rob J. Hyndman",
        "duration": "5 Weeks (25 Hours)",
        "description": "Analyze temporal datasets for financial modeling and system monitoring. Master stationarity, ARIMA, SARIMA, Facebook Prophet, and Isolation Forests.",
        "learning_objectives": "- Decompose time-series into trend, seasonality, and residual noise\n- Test for stationarity using Augmented Dickey-Fuller (ADF) test\n- Forecast future values using ARIMA and Prophet models\n- Detect operational telemetry anomalies using Isolation Forests",
        "is_published": True,
        "lessons": [
            {
                "title": "Time-Series Decomposition and Stationarity",
                "content": "Analyze autocorrelation functions (ACF) and partial autocorrelation functions (PACF) to identify seasonality and trend dynamics.",
                "resource_url": "https://otexts.com/fpp3/"
            },
            {
                "title": "ARIMA and Seasonal SARIMA Modeling",
                "content": "Fit autoregressive integrated moving average models to stationary time series and evaluate forecast confidence intervals.",
                "resource_url": "https://www.statsmodels.org/stable/tsa.html"
            },
            {
                "title": "Unsupervised Anomaly Detection on Metrics",
                "content": "Use Isolation Forests and autoencoders to automatically flag abnormal CPU spikes and traffic dips in server operations.",
                "resource_url": "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html"
            }
        ]
    },

    # 5. Databases (Courses 33 - 38)
    {
        "title": "Relational Database Design & Advanced PostgreSQL",
        "category": "Databases",
        "instructor": "Michael Stonebraker",
        "duration": "6 Weeks (30 Hours)",
        "description": "Master relational database architecture: 3NF normalization, ACID transaction isolation levels, B-tree indexes, foreign keys, window functions, and CTEs.",
        "learning_objectives": "- Design normalized schemas eliminating redundancy\n- Understand ACID transactions and concurrency control\n- Write complex queries using Common Table Expressions and Window Functions\n- Optimize query plans with EXPLAIN ANALYZE",
        "is_published": True,
        "lessons": [
            {
                "title": "Database Normalization (1NF to BCNF) and Integrity",
                "content": "Design relational tables enforcing primary keys, foreign key constraints, and cascade behaviors without data duplication anomalies.",
                "resource_url": "https://www.postgresql.org/docs/current/ddl.html"
            },
            {
                "title": "ACID Properties and Transaction Isolation Levels",
                "content": "Examine dirty reads, non-repeatable reads, phantom reads, and compare Read Committed with Serializable isolation.",
                "resource_url": "https://www.postgresql.org/docs/current/transaction-iso.html"
            },
            {
                "title": "Advanced SQL: Window Functions and CTEs",
                "content": "Utilize ROW_NUMBER(), RANK(), LEAD(), and LAG() analytical window functions alongside recursive Common Table Expressions.",
                "resource_url": "https://www.postgresql.org/docs/current/tutorial-window.html"
            }
        ]
    },
    {
        "title": "High-Performance Redis Caching & In-Memory Data Stores",
        "category": "Databases",
        "instructor": "Salvatore Sanfilippo",
        "duration": "4 Weeks (20 Hours)",
        "description": "Accelerate web response times using Redis. Learn in-memory data structures: Strings, Hashes, Lists, Sets, Sorted Sets, Pub/Sub, and distributed locking.",
        "learning_objectives": "- Implement caching patterns: cache-aside, write-through, and cache-eviction\n- Leverage Redis data structures for rate limiting and leaderboards\n- Build real-time messaging using Redis Pub/Sub\n- Implement distributed locks using Redlock algorithm",
        "is_published": True,
        "lessons": [
            {
                "title": "Redis In-Memory Architecture and Core Data Structures",
                "content": "Redis provides sub-millisecond data access by serving data directly from RAM with optional disk persistence via RDB snapshots and AOF logs.",
                "resource_url": "https://redis.io/docs/data-types/"
            },
            {
                "title": "Caching Strategies and TTL Eviction Policies",
                "content": "Implement Cache-Aside patterns with time-to-live expiration to prevent stale cache entries and database connection exhaustion.",
                "resource_url": "https://redis.io/docs/manual/eviction/"
            },
            {
                "title": "Building Real-Time Rate Limiters and Leaderboards",
                "content": "Leverage Redis Sorted Sets (ZADD/ZRANGE) for high-speed gaming leaderboards and atomic sliding-window rate limiters.",
                "resource_url": "https://redis.io/docs/interact/programmability/"
            }
        ]
    },
    {
        "title": "NoSQL Architecture with MongoDB",
        "category": "Databases",
        "instructor": "Dwight Merriman",
        "duration": "5 Weeks (25 Hours)",
        "description": "Design document-oriented databases using MongoDB. Master JSON/BSON schema design, embedding vs. referencing, aggregation pipelines, and sharding.",
        "learning_objectives": "- Design flexible schema models for document stores\n- Build multi-stage aggregation pipelines for reporting\n- Create compound and geospatial indexes\n- Understand replica sets for high availability",
        "is_published": True,
        "lessons": [
            {
                "title": "Document Data Modeling: Embedding vs. Referencing",
                "content": "Decide when to embed sub-documents for fast atomic reads versus referencing related collections with ObjectId foreign keys.",
                "resource_url": "https://www.mongodb.com/docs/manual/core/data-modeling-introduction/"
            },
            {
                "title": "The MongoDB Aggregation Framework",
                "content": "Filter, group, project, and reshape documents through multi-stage pipelines using $match, $group, $sort, and $lookup.",
                "resource_url": "https://www.mongodb.com/docs/manual/aggregation/"
            },
            {
                "title": "Replica Sets and Sharded Cluster Architecture",
                "content": "Configure primary-secondary replica sets for automatic failover and partition massive datasets across shards using shard keys.",
                "resource_url": "https://www.mongodb.com/docs/manual/replication/"
            }
        ]
    },
    {
        "title": "SQL Indexing & Query Performance Tuning",
        "category": "Databases",
        "instructor": "Markus Winand",
        "duration": "5 Weeks (25 Hours)",
        "description": "Make SQL queries fly! Learn internal B-tree mechanics, clustered vs. secondary indexes, composite index column ordering, and index-only scans.",
        "learning_objectives": "- Read and interpret EXPLAIN query execution plans\n- Structure composite indexes matching query WHERE and ORDER BY clauses\n- Eliminate table sequential scans on large datasets\n- Avoid index-suppressing expressions and implicit conversions",
        "is_published": True,
        "lessons": [
            {
                "title": "Internal Mechanics of B-Tree Indexes",
                "content": "Understand how balanced tree structures enable logarithmic O(log N) lookup speeds by traversing root, branch, and leaf nodes.",
                "resource_url": "https://use-the-index-luke.com/"
            },
            {
                "title": "Composite Indexes and the Leftmost Prefix Rule",
                "content": "Learn why column order matters in composite indexes and how to design indexes that satisfy equality, range, and sorting operations.",
                "resource_url": "https://use-the-index-luke.com/sql/where-clause/searching-for-ranges/greater-less-between-tuning-sql-indexing"
            },
            {
                "title": "Analyzing Execution Plans with EXPLAIN ANALYZE",
                "content": "Identify costly table scans, nested loop joins, and sort operations, converting them into efficient index scans.",
                "resource_url": "https://www.postgresql.org/docs/current/using-explain.html"
            }
        ]
    },
    {
        "title": "Distributed Databases & Apache Cassandra",
        "category": "Databases",
        "instructor": "Avinash Lakshman",
        "duration": "6 Weeks (30 Hours)",
        "description": "Architect masterless distributed databases with Apache Cassandra. Learn peer-to-peer ring topology, tunable consistency, partition keys, and CQL queries.",
        "learning_objectives": "- Understand Dynamo and BigTable hybrid architecture\n- Design query-driven data models based on partition keys\n- Configure tunable consistency levels (ONE, QUORUM, ALL)\n- Manage tombstone collection and SSTable compaction",
        "is_published": True,
        "lessons": [
            {
                "title": "Cassandra Architecture: Masterless Ring Topology",
                "content": "Cassandra uses a decentralized, masterless architecture where every node is identical, eliminating single points of failure.",
                "resource_url": "https://cassandra.apache.org/_/architecture.html"
            },
            {
                "title": "Data Modeling by Query in CQL",
                "content": "In Cassandra, you design tables around your exact read queries rather than normalizing data across relational joins.",
                "resource_url": "https://cassandra.apache.org/doc/latest/cassandra/data_modeling/index.html"
            },
            {
                "title": "CAP Theorem and Tunable Consistency",
                "content": "Balance write and read latency against consistency guarantees by tuning replication factors and read/write consistency levels.",
                "resource_url": "https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html"
            }
        ]
    },
    {
        "title": "Database Reliability Engineering & Disaster Recovery",
        "category": "Databases",
        "instructor": "Laine Campbell",
        "duration": "5 Weeks (25 Hours)",
        "description": "Operate production databases with zero data loss. Master Point-in-Time Recovery (PITR), physical/logical backups, replication lag, and automated failover.",
        "learning_objectives": "- Formulate Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO)\n- Configure WAL (Write-Ahead Logging) archiving for Point-in-Time Recovery\n- Implement streaming replication and automated failover with Patroni\n- Test database backup restoration routinely",
        "is_published": True,
        "lessons": [
            {
                "title": "RPO, RTO, and High Availability Design",
                "content": "Quantify disaster recovery requirements and design database clustering topologies that tolerate hardware and data center outages.",
                "resource_url": "https://aws.amazon.com/blogs/database/architecting-disaster-recovery-for-databases-on-aws/"
            },
            {
                "title": "Write-Ahead Logging (WAL) and Point-in-Time Recovery",
                "content": "Archive transaction logs to cloud storage to restore a database to the exact millisecond before a catastrophic failure or corruption occurred.",
                "resource_url": "https://www.postgresql.org/docs/current/continuous-archiving.html"
            },
            {
                "title": "Automated Clustering and Failover with Patroni",
                "content": "Use Patroni with etcd distributed consensus to automate leader election and safe failover in PostgreSQL clusters.",
                "resource_url": "https://patroni.readthedocs.io/en/latest/"
            }
        ]
    },

    # 6. Software Engineering (Courses 39 - 42)
    {
        "title": "Clean Code & Refactoring Architecture",
        "category": "Software Engineering",
        "instructor": "Robert C. Martin",
        "duration": "5 Weeks (25 Hours)",
        "description": "Write readable, maintainable, and extensible code. Master SOLID principles, code smell detection, meaningful naming, and systematic refactoring patterns.",
        "learning_objectives": "- Apply SOLID object-oriented design principles\n- Identify and eliminate code smells (long methods, god classes, primitive obsession)\n- Refactor legacy code safely with automated regression tests\n- Write expressive, self-documenting functions",
        "is_published": True,
        "lessons": [
            {
                "title": "The SOLID Principles of Object-Oriented Design",
                "content": "Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion explained with practical refactoring examples.",
                "resource_url": "https://en.wikipedia.org/wiki/SOLID"
            },
            {
                "title": "Detecting and Eradicating Common Code Smells",
                "content": "Learn how to spot feature envy, duplicated logic, and shotgun surgery, applying Extract Method and Move Method refactorings.",
                "resource_url": "https://refactoring.guru/refactoring/smells"
            },
            {
                "title": "Safe Refactoring with Unit Test Safety Nets",
                "content": "Learn the golden rule of refactoring: never change software behavior without automated unit tests protecting every alteration.",
                "resource_url": "https://refactoring.guru/refactoring"
            }
        ]
    },
    {
        "title": "Test-Driven Development (TDD) & Pytest Mastery",
        "category": "Software Engineering",
        "instructor": "Kent Beck",
        "duration": "5 Weeks (25 Hours)",
        "description": "Adopt the Red-Green-Refactor rhythm. Master unit testing, integration testing, parameterized tests, test doubles (mocks/stubs), and coverage reports.",
        "learning_objectives": "- Practice Test-Driven Development (Red-Green-Refactor)\n- Write expressive test fixtures and parameterizations in Pytest\n- Isolate external dependencies using unittest.mock and monkeypatch\n- Measure and maintain high code test coverage",
        "is_published": True,
        "lessons": [
            {
                "title": "The Red-Green-Refactor Cycle",
                "content": "Write a failing test first (Red), implement the minimum code to make it pass (Green), and clean up design while keeping tests green (Refactor).",
                "resource_url": "https://martinfowler.com/bliki/TestDrivenDevelopment.html"
            },
            {
                "title": "Pytest Fixtures, Marks, and Parameterized Tests",
                "content": "Use Pytest fixtures for modular dependency injection and test clean-up, and @pytest.mark.parametrize to test edge-cases succinctly.",
                "resource_url": "https://docs.pytest.org/en/stable/explanation/fixtures.html"
            },
            {
                "title": "Mocking External APIs and Database Layers",
                "content": "Use test doubles to mock third-party network APIs and simulate transient failures without calling production services.",
                "resource_url": "https://docs.python.org/3/library/unittest.mock.html"
            }
        ]
    },
    {
        "title": "Software Design Patterns in Python",
        "category": "Software Engineering",
        "instructor": "Erich Gamma",
        "duration": "6 Weeks (30 Hours)",
        "description": "Master classic Gang of Four (GoF) design patterns implemented cleanly in idiomatic Python: Factory, Singleton, Observer, Strategy, Decorator, and Adapter.",
        "learning_objectives": "- Understand creational, structural, and behavioral pattern categories\n- Implement Strategy and Factory patterns for decoupling business rules\n- Apply Decorator pattern for cross-cutting concerns (logging, auth, caching)\n- Know when NOT to over-engineer with patterns",
        "is_published": True,
        "lessons": [
            {
                "title": "Creational Patterns: Factory Method and Builder",
                "content": "Abstract object instantiation logic to create decoupled hierarchies without hardcoding concrete implementation classes.",
                "resource_url": "https://refactoring.guru/design-patterns/creational-patterns"
            },
            {
                "title": "Structural Patterns: Decorator and Adapter",
                "content": "Attach additional responsibilities to objects dynamically using Python decorators and adapt incompatible interfaces seamlessly.",
                "resource_url": "https://refactoring.guru/design-patterns/structural-patterns"
            },
            {
                "title": "Behavioral Patterns: Strategy and Observer",
                "content": "Define families of interchangeable algorithms with the Strategy pattern and build event-driven subscription systems with the Observer pattern.",
                "resource_url": "https://refactoring.guru/design-patterns/behavioral-patterns"
            }
        ]
    },
    {
        "title": "Microservices Communication & Event-Driven Architecture",
        "category": "Software Engineering",
        "instructor": "Martin Fowler",
        "duration": "6 Weeks (30 Hours)",
        "description": "Architect distributed enterprise systems. Compare synchronous gRPC and REST against asynchronous event-driven messaging with Apache Kafka and RabbitMQ.",
        "learning_objectives": "- Decompose monolithic domains using Bounded Contexts\n- Implement synchronous RPC communication using Protocol Buffers and gRPC\n- Build event-driven publishers and consumers with Apache Kafka\n- Manage distributed transactions with the Saga Pattern",
        "is_published": True,
        "lessons": [
            {
                "title": "Monolith to Microservices: Domain-Driven Design (DDD)",
                "content": "Identify logical business boundaries and microservice contracts using Event Storming and Domain-Driven Design Bounded Contexts.",
                "resource_url": "https://martinfowler.com/articles/microservices.html"
            },
            {
                "title": "High-Performance Inter-Service gRPC and Protocol Buffers",
                "content": "Use binary HTTP/2 gRPC streaming for low-latency, strongly-typed communication between backend microservices.",
                "resource_url": "https://grpc.io/docs/what-is-grpc/introduction/"
            },
            {
                "title": "Event-Driven Messaging with Apache Kafka and Sagas",
                "content": "Publish immutable domain events to distributed Kafka topics and coordinate distributed compensating transactions using Sagas.",
                "resource_url": "https://microservices.io/patterns/data/saga.html"
            }
        ]
    }
]
