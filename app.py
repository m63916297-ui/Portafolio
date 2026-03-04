import streamlit as st

st.set_page_config(
    page_title="Robinson Moncada | Software Engineer AI/Blockchain",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif !important;
    box-sizing: border-box;
}

html, body, .stApp {
    background: #0a0a0f !important;
    color: #f8fafc;
}

.main {
    background: linear-gradient(135deg, #0a0a0f 0%, #0c0c14 50%, #0f0f1a 100%);
    min-height: 100vh;
    position: relative;
}

.main::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(99, 102, 241, 0.15), transparent),
        radial-gradient(ellipse 60% 40% at 100% 0%, rgba(139, 92, 246, 0.1), transparent),
        radial-gradient(ellipse 50% 30% at 0% 100%, rgba(16, 185, 129, 0.08), transparent);
    pointer-events: none;
    z-index: 0;
}

.stApp > div {
    position: relative;
    z-index: 1;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero-section {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.1) 50%, rgba(16, 185, 129, 0.08) 100%);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 24px;
    padding: 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.5s ease-out forwards;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #818cf8, #34d399, transparent);
    background-size: 200% 100%;
    animation: gradient-shift 3s ease infinite;
}

.hero-title {
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    background: linear-gradient(135deg, #fff 0%, #a5b4fc 50%, #34d399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}

.hero-subtitle {
    font-size: clamp(1rem, 2vw, 1.35rem);
    color: #94a3b8;
    margin-bottom: 1rem;
    font-weight: 400;
}

.hero-location {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: #34d399;
    font-size: 0.95rem;
    font-weight: 500;
    padding: 0.5rem 1rem;
    background: rgba(16, 185, 129, 0.1);
    border-radius: 9999px;
    border: 1px solid rgba(16, 185, 129, 0.2);
}

.section-title {
    font-size: clamp(1.5rem, 3vw, 2rem);
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 2px solid transparent;
    position: relative;
    display: inline-block;
}

.section-title::before {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, #818cf8, #34d399);
    border-radius: 9999px;
}

.service-card {
    background: rgba(30, 41, 59, 0.6);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.service-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #10b981);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.service-card:hover {
    transform: translateY(-4px);
    background: rgba(49, 46, 129, 0.3);
    border-color: rgba(139, 92, 246, 0.4);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3), 0 0 40px rgba(99, 102, 241, 0.3);
}

.service-card:hover::before {
    transform: scaleX(1);
}

.service-icon {
    font-size: 2.5rem;
    margin-bottom: 0.75rem;
    display: inline-block;
    transition: transform 0.3s ease;
}

.service-card:hover .service-icon {
    transform: scale(1.15) rotate(5deg);
}

.service-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #f8fafc;
    margin-bottom: 0.5rem;
}

.service-description {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.7;
}

.tech-tag {
    display: inline-flex;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.1));
    color: #a5b4fc;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 500;
    margin: 0.25rem;
    border: 1px solid rgba(99, 102, 241, 0.2);
    transition: all 0.15s ease;
}

.tech-tag:hover {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(139, 92, 246, 0.2));
    border-color: #818cf8;
    transform: translateY(-2px);
}

.experience-card {
    background: rgba(30, 41, 59, 0.6);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-left: 4px solid #6366f1;
    padding: 1.5rem;
    margin-bottom: 1rem;
    border-radius: 0 12px 12px 0;
    transition: all 0.3s ease;
}

.experience-card:hover {
    background: rgba(49, 46, 129, 0.3);
    border-left-color: #10b981;
    transform: translateX(8px);
}

.experience-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #f8fafc;
}

.experience-company {
    color: #818cf8;
    font-weight: 500;
}

.experience-period {
    color: #64748b;
    font-size: 0.85rem;
    margin-bottom: 0.75rem;
    font-family: monospace;
}

.experience-description {
    color: #94a3b8;
    line-height: 1.7;
}

.industry-badge {
    display: inline-flex;
    background: rgba(99, 102, 241, 0.1);
    color: #a5b4fc;
    padding: 0.25rem 0.75rem;
    border-radius: 8px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-right: 0.5rem;
    border: 1px solid rgba(99, 102, 241, 0.15);
}

.prose-card {
    background: rgba(30, 41, 59, 0.6);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    border: 1px solid rgba(148, 163, 184, 0.1);
}

.prose-card h4 {
    color: #f8fafc;
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.1rem;
}

.prose-card p {
    color: #94a3b8;
    line-height: 1.8;
}

.prose-card strong {
    color: #a5b4fc;
}

.contact-card {
    background: rgba(30, 41, 59, 0.6);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(148, 163, 184, 0.1);
}

.contact-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #10b981, #f59e0b);
}

.contact-card:hover {
    transform: translateY(-4px);
    border-color: rgba(139, 92, 246, 0.4);
}

.contact-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.contact-label {
    color: #f8fafc;
    font-weight: 600;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}

.contact-value {
    color: #94a3b8;
    font-size: 0.95rem;
}

.footer {
    text-align: center;
    padding: 2rem 0;
    margin-top: 2rem;
    border-top: 1px solid rgba(148, 163, 184, 0.1);
}

.footer-text {
    color: #64748b;
    font-size: 0.9rem;
}

.footer-brand {
    color: #818cf8;
    font-weight: 600;
}

section[data-testid="stSidebar"] {
    background: rgba(10, 10, 15, 0.95) !important;
}

div[data-testid="stMetric"] {
    background: rgba(30, 41, 59, 0.6);
    border-radius: 12px;
    padding: 1rem;
    border: 1px solid rgba(148, 163, 184, 0.1);
}

.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 8px;
    padding: 0.5rem 1rem;
    color: #94a3b8;
}

.stTabs [aria-selected="true"] {
    background: rgba(99, 102, 241, 0.2);
    border-color: #6366f1;
    color: #a5b4fc;
}

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #12121a;
}

::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 4px;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_header():
    st.markdown(
        """
    <div class="hero-section">
        <h1 class="hero-title">Robinson Moncada</h1>
        <p class="hero-subtitle">⚡ Software Engineer AI/Blockchain | 15 Years of Excellence</p>
        <span class="hero-location">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
            </svg>
            Singapur
        </span>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_about():
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        **Senior Technology Expert con 15+ años de experiencia** transformando industrias a través de soluciones innovadoras 
        basadas en Inteligencia Artificial, Computación Cuántica y tecnologías emergentes.
        
        Especialista en desarrollar arquitecturas de próxima generación que impulsan la transformación digital 
        en sectores críticos como **Fintech**, **Salud** y **Movilidad**.
        
        Mi enfoque combina profundidad técnica con visión estratégica de negocio, deliverando soluciones 
        que generan impacto medible y sostenible.
        """)

    with col2:
        st.markdown("### Quick Stats")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Years", "15+")
            st.metric("Projects", "50+")
        with col_b:
            st.metric("Industries", "3")
            st.metric("Clients", "30+")


def render_services():
    st.markdown('<h2 class="section-title">Services</h2>', unsafe_allow_html=True)

    services = [
        {
            "icon": "🧠",
            "title": "Machine Learning",
            "description": "Modelos predictivos, clasificación, clustering y análisis de datos. Implementación de pipelines ML en producción con MLOps.",
            "tech": [
                "Python",
                "TensorFlow",
                "PyTorch",
                "Scikit-learn",
                "MLflow",
                "Kubeflow",
            ],
        },
        {
            "icon": "🧬",
            "title": "Deep Learning",
            "description": "Redes neuronales profundas, CNNs, RNNs, Transformers y arquitecturas avanzadas para visión por computador y NLP.",
            "tech": ["PyTorch", "TensorFlow", "Keras", "NVIDIA CUDA", "Apache MXNet"],
        },
        {
            "icon": "✨",
            "title": "AI Generativa",
            "description": "LLMs, generación de texto, imágenes y audio. Fine-tuning de modelos foundation y prompt engineering avanzado.",
            "tech": [
                "GPT-4",
                "Claude",
                "LangChain",
                "LlamaIndex",
                "Stable Diffusion",
                "RAG",
            ],
        },
        {
            "icon": "🔗",
            "title": "MCP Servers",
            "description": "Model Context Protocol servers para integración de LLMs con sistemas externos, APIs y bases de datos.",
            "tech": ["MCP Protocol", "FastAPI", "gRPC", "GraphQL", "Redis"],
        },
        {
            "icon": "🤖",
            "title": "Agentic Engineering",
            "description": "Diseño y desarrollo de AI Agents autonomous, multi-agent systems, reasoning engines y automation workflows.",
            "tech": ["AutoGen", "CrewAI", "LangChain Agents", "ReAct", "Tool Use"],
        },
        {
            "icon": "⚛️",
            "title": "Computación Cuántica",
            "description": "Algoritmos cuánticos, quantum machine learning, optimización cuántica y simulaciones cuánticas.",
            "tech": ["Qiskit", "Cirq", "PennyLane", "Quantum Gates", "VQE"],
        },
        {
            "icon": "🔄",
            "title": "DevOps & MLOps",
            "description": "CI/CD para ML, infraestructura como código, containerización y orquestación de modelos en producción.",
            "tech": [
                "Kubernetes",
                "Docker",
                "Terraform",
                "GitHub Actions",
                "MLflow",
                "Seldon",
            ],
        },
        {
            "icon": "🔐",
            "title": "Blockchain & Web3",
            "description": "Smart contracts, DeFi, NFTs y soluciones blockchain enterprise. Integración con oráculos y Layer 2.",
            "tech": ["Solidity", "Ethereum", "Polygon", "Web3.js", "Chainlink", "IPFS"],
        },
    ]

    cols = st.columns(2)
    for idx, service in enumerate(services):
        with cols[idx % 2]:
            tech_tags = "".join(
                [f'<span class="tech-tag">{tech}</span>' for tech in service["tech"]]
            )
            st.markdown(
                f"""
            <div class="service-card">
                <div class="service-icon">{service["icon"]}</div>
                <div class="service-title">{service["title"]}</div>
                <div class="service-description">{service["description"]}</div>
                <div style="margin-top: 1rem;">
                    {tech_tags}
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )


def render_experience():
    st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)

    experiences = [
        {
            "title": "Chief AI Architect",
            "company": "QuantumMind Labs",
            "period": "2022 - Present",
            "description": "Liderazgo técnico en arquitectura de sistemas AI/ML de escala enterprise. Implementación de Agentic AI para automatización de procesos financieros.",
            "industries": ["Fintech", "Quantum Computing"],
        },
        {
            "title": "Senior ML Engineer",
            "company": "MedTech Innovations",
            "period": "2019 - 2022",
            "description": "Desarrollo de sistemas de diagnóstico asistido por AI. Modelos de deep learning para análisis de imágenes médicas y predicción de resultados clínicos.",
            "industries": ["Healthcare"],
        },
        {
            "title": "AI Solutions Lead",
            "company": "Smart Mobility Corp",
            "period": "2016 - 2019",
            "description": "Implementación de sistemas de tráfico inteligente y vehículos autónomos. Modelos predictivos para optimización de rutas y gestión de flotas.",
            "industries": ["Mobility", "Transport"],
        },
        {
            "title": "Data Science Manager",
            "company": "FinServe Global",
            "period": "2011 - 2016",
            "description": "Equipo de 15 data scientists desarrollando modelos de riesgo crediticio, detección de fraude y trading algorítmico.",
            "industries": ["Fintech"],
        },
    ]

    for exp in experiences:
        industries_html = "".join(
            [f'<span class="industry-badge">{ind}</span>' for ind in exp["industries"]]
        )
        st.markdown(
            f"""
        <div class="experience-card">
            <div class="experience-title">{exp["title"]}</div>
            <div class="experience-company">{exp["company"]}</div>
            <div class="experience-period">{exp["period"]}</div>
            <div style="margin-bottom: 0.75rem;">{industries_html}</div>
            <div class="experience-description">{exp["description"]}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )


def render_tech_stack():
    st.markdown('<h2 class="section-title">Tech Stack</h2>', unsafe_allow_html=True)

    tabs = st.tabs(["AI/ML", "Quantum", "DevOps", "Blockchain"])

    with tabs[0]:
        st.markdown(
            """
        <div class="prose-card">
            <h4>Machine Learning & Deep Learning</h4>
            <p>
            <strong>ML:</strong> TensorFlow, PyTorch, Scikit-learn, XGBoost, LightGBM, Keras<br>
            <strong>NLP:</strong> Hugging Face, spaCy, NLTK, Transformers, BERT, GPT<br>
            <strong>Computer Vision:</strong> OpenCV, YOLO, Detectron, MediaPipe<br>
            <strong>MLOps:</strong> MLflow, Kubeflow, Seldon, TensorFlow Serving, Triton
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[1]:
        st.markdown(
            """
        <div class="prose-card">
            <h4>Quantum Computing</h4>
            <p>
            <strong>SDKs:</strong> Qiskit, Cirq, PennyLane, Forest (Rigetti)<br>
            <strong>Algorithms:</strong> VQE, QAOA, Grover, Shor, Quantum Annealing<br>
            <strong>Quantum ML:</strong> Quantum Neural Networks, Variational Quantum Eigensolver<br>
            <strong>Simulators:</strong> Qiskit Aer, IBM Quantum Experience
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[2]:
        st.markdown(
            """
        <div class="prose-card">
            <h4>DevOps & Cloud</h4>
            <p>
            <strong>Cloud:</strong> AWS, GCP, Azure, Oracle Cloud<br>
            <strong>Containers:</strong> Docker, Kubernetes, Helm, Istio<br>
            <strong>CI/CD:</strong> GitHub Actions, GitLab CI, Jenkins, ArgoCD<br>
            <strong>IaC:</strong> Terraform, CloudFormation, Pulumi
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[3]:
        st.markdown(
            """
        <div class="prose-card">
            <h4>Blockchain & Web3</h4>
            <p>
            <strong>Smart Contracts:</strong> Solidity, Vyper, Rust<br>
            <strong>Networks:</strong> Ethereum, Polygon, Avalanche, Solana<br>
            <strong>Tools:</strong> Hardhat, Truffle, Web3.js, Ethers.js<br>
            <strong>Oracles:</strong> Chainlink, Band Protocol, IPFS
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )


def render_contact():
    st.markdown('<h2 class="section-title">Contact</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="contact-card">
            <span class="contact-icon">📧</span>
            <div class="contact-label">Email</div>
            <div class="contact-value">mikets2026@gmail.com</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="contact-card">
            <span class="contact-icon">💬</span>
            <div class="contact-label">WhatsApp</div>
            <div class="contact-value">+57 301 867 60 51</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="contact-card">
            <span class="contact-icon">📍</span>
            <div class="contact-label">Location</div>
            <div class="contact-value">Singapur</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown(
        """
    <div class="footer">
        <p class="footer-text">
            © 2026 <span class="footer-brand">Robinson Moncada</span>. All rights reserved.<br>
            Building the future with AI & Blockchain
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )


def main():
    with st.sidebar:
        st.markdown("## Navigation")

        menu = st.radio(
            "Go to:",
            ["Home", "Services", "Experience", "Tech Stack", "Contact"],
            label_visibility="collapsed",
        )

        st.markdown("---")
        st.markdown("### Quick Stats")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Years", "15+")
            st.metric("Projects", "50+")
        with col_b:
            st.metric("Industries", "3")
            st.metric("Clients", "30+")

        st.markdown("---")
        st.markdown("### Industries")
        st.markdown("- Fintech")
        st.markdown("- Healthcare")
        st.markdown("- Mobility")

    if menu == "Home":
        render_header()
        render_about()
    elif menu == "Services":
        render_services()
    elif menu == "Experience":
        render_experience()
    elif menu == "Tech Stack":
        render_tech_stack()
    elif menu == "Contact":
        render_contact()


if __name__ == "__main__":
    main()
