import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Miguel Torres | AI & Quantum Computing Expert",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

DESIGN_TOKENS = """
:root {
    /* Primary Palette - Deep Blue & Violet */
    --color-primary-50: #eef2ff;
    --color-primary-100: #e0e7ff;
    --color-primary-200: #c7d2fe;
    --color-primary-300: #a5b4fc;
    --color-primary-400: #818cf8;
    --color-primary-500: #6366f1;
    --color-primary-600: #4f46e5;
    --color-primary-700: #4338ca;
    --color-primary-800: #3730a3;
    --color-primary-900: #312e81;
    
    /* Secondary - Emerald */
    --color-secondary-400: #34d399;
    --color-secondary-500: #10b981;
    --color-secondary-600: #059669;
    
    /* Accent - Amber */
    --color-accent-400: #fbbf24;
    --color-accent-500: #f59e0b;
    
    /* Neutral - Slate */
    --color-gray-50: #f8fafc;
    --color-gray-100: #f1f5f9;
    --color-gray-200: #e2e8f0;
    --color-gray-300: #cbd5e1;
    --color-gray-400: #94a3b8;
    --color-gray-500: #64748b;
    --color-gray-600: #475569;
    --color-gray-700: #334155;
    --color-gray-800: #1e293b;
    --color-gray-900: #0f172a;
    --color-gray-950: #020617;
    
    /* Semantic */
    --color-success: #10b981;
    --color-warning: #f59e0b;
    --color-error: #ef4444;
    --color-info: #3b82f6;
    
    /* Background */
    --bg-primary: #0a0a0f;
    --bg-secondary: #12121a;
    --bg-card: rgba(30, 41, 59, 0.6);
    --bg-card-hover: rgba(49, 46, 129, 0.3);
    
    /* Border */
    --border-color: rgba(148, 163, 184, 0.1);
    --border-color-hover: rgba(139, 92, 246, 0.4);
    
    /* Text */
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-tertiary: #64748b;
    
    /* Typography */
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    
    /* Spacing */
    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-3: 0.75rem;
    --space-4: 1rem;
    --space-5: 1.25rem;
    --space-6: 1.5rem;
    --space-8: 2rem;
    --space-10: 2.5rem;
    --space-12: 3rem;
    --space-16: 4rem;
    
    /* Radius */
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;
    --radius-2xl: 1.5rem;
    --radius-full: 9999px;
    
    /* Shadows */
    --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
    --shadow-glow: 0 0 40px rgba(99, 102, 241, 0.3);
    --shadow-glow-accent: 0 0 60px rgba(139, 92, 246, 0.4);
    
    /* Animation */
    --duration-fast: 150ms;
    --duration-normal: 300ms;
    --duration-slow: 500ms;
    --ease-out: cubic-bezier(0, 0, 0.2, 1);
    --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
    --ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
"""

CUSTOM_CSS = f"""
{DESIGN_TOKENS}

<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    * {{
        font-family: var(--font-sans);
        box-sizing: border-box;
    }}
    
    html, body {{
        background: var(--bg-primary);
        color: var(--text-primary);
    }}
    
    .main {{
        background: linear-gradient(135deg, var(--bg-primary) 0%, #0c0c14 50%, #0f0f1a 100%);
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
    }}
    
    .main::before {{
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
    }}
    
    .stApp {{
        background: transparent;
        position: relative;
        z-index: 1;
    }}
    
    /* ===== ANIMATIONS ===== */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    
    @keyframes pulse-glow {{
        0%, 100% {{ box-shadow: 0 0 20px rgba(99, 102, 241, 0.3); }}
        50% {{ box-shadow: 0 0 40px rgba(139, 92, 246, 0.5); }}
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    @keyframes shimmer {{
        0% {{ background-position: -200% 0; }}
        100% {{ background-position: 200% 0; }}
    }}
    
    @keyframes gradient-shift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    @keyframes border-glow {{
        0%, 100% {{ border-color: rgba(99, 102, 241, 0.3); }}
        50% {{ border-color: rgba(139, 92, 246, 0.6); }}
    }}
    
    .animate-fade-in {{
        animation: fadeIn var(--duration-slow) var(--ease-out) forwards;
    }}
    
    .animate-fade-in-up {{
        animation: fadeInUp var(--duration-slow) var(--ease-out) forwards;
    }}
    
    /* ===== HERO SECTION ===== */
    .hero-section {{
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(139, 92, 246, 0.15) 50%, rgba(16, 185, 129, 0.1) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-2xl);
        padding: var(--space-12);
        margin-bottom: var(--space-8);
        position: relative;
        overflow: hidden;
        animation: fadeInUp var(--duration-slow) var(--ease-out) forwards;
    }}
    
    .hero-section::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--color-primary-400), var(--color-secondary-400), transparent);
        background-size: 200% 100%;
        animation: gradient-shift 3s ease infinite;
    }}
    
    .hero-section::after {{
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
        pointer-events: none;
    }}
    
    .hero-title {{
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        background: linear-gradient(135deg, #fff 0%, var(--color-primary-300) 50%, var(--color-secondary-400) 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: var(--space-2);
        animation: gradient-shift 4s ease infinite;
        letter-spacing: -0.02em;
    }}
    
    .hero-subtitle {{
        font-size: clamp(1rem, 2vw, 1.35rem);
        color: var(--text-secondary);
        margin-bottom: var(--space-4);
        font-weight: 400;
        letter-spacing: 0.01em;
    }}
    
    .hero-location {{
        display: inline-flex;
        align-items: center;
        gap: var(--space-2);
        color: var(--color-secondary-400);
        font-size: 0.95rem;
        font-weight: 500;
        padding: var(--space-2) var(--space-4);
        background: rgba(16, 185, 129, 0.1);
        border-radius: var(--radius-full);
        border: 1px solid rgba(16, 185, 129, 0.2);
    }}
    
    /* ===== SECTION TITLES ===== */
    .section-title {{
        font-size: clamp(1.5rem, 3vw, 2rem);
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: var(--space-6);
        padding-bottom: var(--space-3);
        border-bottom: 2px solid transparent;
        border-image: linear-gradient(90deg, var(--color-primary-500), var(--color-secondary-500)) 1;
        display: inline-block;
        position: relative;
    }}
    
    .section-title::before {{
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 60px;
        height: 2px;
        background: linear-gradient(90deg, var(--color-primary-400), var(--color-secondary-400));
        border-radius: var(--radius-full);
    }}
    
    /* ===== SERVICE CARDS ===== */
    .service-card {{
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-xl);
        padding: var(--space-6);
        margin-bottom: var(--space-4);
        transition: all var(--duration-normal) var(--ease-out);
        position: relative;
        overflow: hidden;
    }}
    
    .service-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--color-primary-500), var(--color-secondary-500));
        transform: scaleX(0);
        transition: transform var(--duration-normal) var(--ease-out);
    }}
    
    .service-card:hover {{
        transform: translateY(-4px) scale(1.01);
        background: var(--bg-card-hover);
        border-color: var(--border-color-hover);
        box-shadow: var(--shadow-xl), var(--shadow-glow);
    }}
    
    .service-card:hover::before {{
        transform: scaleX(1);
    }}
    
    .service-icon {{
        font-size: 2.5rem;
        margin-bottom: var(--space-3);
        display: inline-block;
        transition: transform var(--duration-normal) var(--ease-out);
    }}
    
    .service-card:hover .service-icon {{
        transform: scale(1.15) rotate(5deg);
    }}
    
    .service-title {{
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: var(--space-2);
    }}
    
    .service-description {{
        color: var(--text-secondary);
        font-size: 0.95rem;
        line-height: 1.7;
    }}
    
    /* ===== TECH TAGS ===== */
    .tech-tag {{
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.1));
        color: var(--color-primary-300);
        padding: var(--space-1) var(--space-3);
        border-radius: var(--radius-full);
        font-size: 0.75rem;
        font-weight: 500;
        margin: var(--space-1);
        border: 1px solid rgba(99, 102, 241, 0.2);
        transition: all var(--duration-fast) var(--ease-out);
    }}
    
    .tech-tag:hover {{
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(139, 92, 246, 0.2));
        border-color: var(--color-primary-400);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }}
    
    /* ===== STAT CARDS ===== */
    .stat-card {{
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-xl);
        padding: var(--space-6);
        text-align: center;
        transition: all var(--duration-normal) var(--ease-out);
        position: relative;
        overflow: hidden;
    }}
    
    .stat-card::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--color-primary-500), var(--color-secondary-500));
        transition: width var(--duration-normal) var(--ease-out);
    }}
    
    .stat-card:hover {{
        transform: translateY(-4px);
        border-color: var(--border-color-hover);
        box-shadow: var(--shadow-lg);
    }}
    
    .stat-card:hover::after {{
        width: 100%;
    }}
    
    .stat-number {{
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--color-primary-400), var(--color-secondary-400));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    .stat-label {{
        color: var(--text-secondary);
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    
    /* ===== EXPERIENCE CARDS ===== */
    .experience-card {{
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border-color);
        border-left: 4px solid var(--color-primary-500);
        padding: var(--space-6);
        margin-bottom: var(--space-4);
        border-radius: 0 var(--radius-lg) var(--radius-lg) 0;
        transition: all var(--duration-normal) var(--ease-out);
        position: relative;
    }}
    
    .experience-card:hover {{
        background: var(--bg-card-hover);
        border-left-color: var(--color-secondary-500);
        transform: translateX(8px);
        box-shadow: var(--shadow-lg);
    }}
    
    .experience-title {{
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--text-primary);
    }}
    
    .experience-company {{
        color: var(--color-primary-400);
        font-weight: 500;
        margin-bottom: var(--space-1);
    }}
    
    .experience-period {{
        color: var(--text-tertiary);
        font-size: 0.85rem;
        margin-bottom: var(--space-3);
        font-family: var(--font-mono);
    }}
    
    .experience-description {{
        color: var(--text-secondary);
        line-height: 1.7;
    }}
    
    /* ===== INDUSTRY BADGES ===== */
    .industry-badge {{
        display: inline-flex;
        align-items: center;
        background: rgba(99, 102, 241, 0.1);
        color: var(--color-primary-300);
        padding: var(--space-1) var(--space-3);
        border-radius: var(--radius-md);
        font-size: 0.8rem;
        font-weight: 500;
        margin-right: var(--space-2);
        border: 1px solid rgba(99, 102, 241, 0.15);
        transition: all var(--duration-fast) var(--ease-out);
    }}
    
    .industry-badge:hover {{
        background: rgba(99, 102, 241, 0.2);
        transform: scale(1.05);
    }}
    
    /* ===== PROSE CARDS ===== */
    .prose-card {{
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-xl);
        padding: var(--space-6);
        margin-bottom: var(--space-4);
        transition: all var(--duration-normal) var(--ease-out);
    }}
    
    .prose-card:hover {{
        border-color: var(--border-color-hover);
        box-shadow: var(--shadow-lg);
    }}
    
    .prose-card h4 {{
        color: var(--text-primary);
        font-weight: 600;
        margin-bottom: var(--space-4);
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        gap: var(--space-2);
    }}
    
    .prose-card h4::before {{
        content: '';
        width: 4px;
        height: 20px;
        background: linear-gradient(180deg, var(--color-primary-500), var(--color-secondary-500));
        border-radius: var(--radius-full);
    }}
    
    .prose-card p {{
        color: var(--text-secondary);
        line-height: 1.8;
    }}
    
    .prose-card strong {{
        color: var(--color-primary-300);
        font-weight: 600;
    }}
    
    /* ===== SIDEBAR ===== */
    .stSidebar {{
        background: rgba(10, 10, 15, 0.95) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid var(--border-color);
    }}
    
    .sidebar-title {{
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--text-tertiary);
        font-weight: 600;
        margin-bottom: var(--space-3);
    }}
    
    .sidebar-nav-item {{
        display: flex;
        align-items: center;
        gap: var(--space-3);
        padding: var(--space-3) var(--space-4);
        border-radius: var(--radius-md);
        color: var(--text-secondary);
        cursor: pointer;
        transition: all var(--duration-fast) var(--ease-out);
        margin-bottom: var(--space-1);
    }}
    
    .sidebar-nav-item:hover {{
        background: rgba(99, 102, 241, 0.1);
        color: var(--text-primary);
    }}
    
    .sidebar-nav-item.active {{
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.1));
        color: var(--color-primary-300);
        border: 1px solid rgba(99, 102, 241, 0.2);
    }}
    
    /* ===== STREAMLIT OVERRIDES ===== */
    div[data-testid="stMetric"] {{
        background: var(--bg-card);
        border-radius: var(--radius-lg);
        padding: var(--space-4);
        border: 1px solid var(--border-color);
        transition: all var(--duration-fast) var(--ease-out);
    }}
    
    div[data-testid="stMetric"]:hover {{
        border-color: var(--border-color-hover);
        transform: translateY(-2px);
    }}
    
    div[data-testid="stMetricLabel"] {{
        color: var(--text-secondary) !important;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    
    div[data-testid="stMetricValue"] {{
        color: var(--text-primary) !important;
        font-weight: 600;
    }}
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: var(--space-2);
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: var(--space-2) var(--space-4);
        color: var(--text-secondary);
        font-weight: 500;
        transition: all var(--duration-fast) var(--ease-out);
    }}
    
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.1));
        border-color: var(--color-primary-500);
        color: var(--color-primary-300);
    }}
    
    /* ===== CONTACT SECTION ===== */
    .contact-card {{
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-xl);
        padding: var(--space-8);
        text-align: center;
        transition: all var(--duration-normal) var(--ease-out);
        position: relative;
        overflow: hidden;
    }}
    
    .contact-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--color-primary-500), var(--color-secondary-500), var(--color-accent-500));
    }}
    
    .contact-card:hover {{
        transform: translateY(-4px);
        border-color: var(--border-color-hover);
        box-shadow: var(--shadow-xl);
    }}
    
    .contact-icon {{
        font-size: 3rem;
        margin-bottom: var(--space-4);
        display: block;
    }}
    
    .contact-label {{
        color: var(--text-primary);
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: var(--space-2);
    }}
    
    .contact-value {{
        color: var(--text-secondary);
        font-size: 0.95rem;
        word-break: break-all;
    }}
    
    .contact-value:hover {{
        color: var(--color-primary-300);
    }}
    
    /* ===== FOOTER ===== */
    .footer {{
        text-align: center;
        padding: var(--space-8) 0;
        margin-top: var(--space-8);
        border-top: 1px solid var(--border-color);
    }}
    
    .footer-text {{
        color: var(--text-tertiary);
        font-size: 0.9rem;
    }}
    
    .footer-brand {{
        color: var(--color-primary-400);
        font-weight: 600;
    }}
    
    /* ===== DIVIDER ===== */
    hr {{
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border-color), transparent);
        margin: var(--space-8) 0;
    }}
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: var(--bg-secondary);
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: var(--color-gray-700);
        border-radius: var(--radius-full);
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: var(--color-primary-600);
    }}
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {{
        .hero-section {{
            padding: var(--space-6);
        }}
        
        .service-card, .experience-card, .stat-card {{
            margin-bottom: var(--space-3);
        }}
    }}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_header():
    st.markdown(
        """
    <div class="hero-section">
        <h1 class="hero-title">Miguel Torres</h1>
        <p class="hero-subtitle">🤖 AI & Quantum Computing Expert | 15 Years of Excellence</p>
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
        
        Mi enfoque combina profundidad técnica con visión estratégica de negocio, delivers soluciones 
        que generan impacto medible y sostenible.
        """)

    with col2:
        st.markdown("### 📊 Quick Stats")
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
            © 2026 <span class="footer-brand">Miguel Torres</span>. All rights reserved.<br>
            Building the future with AI & Quantum Computing
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )


def main():
    with st.sidebar:
        st.markdown("## 🧭 Navigation")

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
        st.markdown("- 🏦 Fintech")
        st.markdown("- 🏥 Healthcare")
        st.markdown("- 🚗 Mobility")

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
