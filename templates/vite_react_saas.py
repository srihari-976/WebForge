from __future__ import annotations

import json

from webbuilder.models import JsonDict


def render(requirements: JsonDict, plan: JsonDict) -> dict[str, str]:
    website_type = str(requirements.get("website_type", "AI SaaS")).replace("_", " ").title()
    theme = str(requirements.get("theme", "modern"))
    components = requirements.get("components", ["Navbar", "Hero", "Features", "Pricing", "Contact", "Footer"])
    sections = plan.get("sections", ["hero", "features", "pricing", "contact"])
    primary = str(plan.get("primary_color", "blue"))

    package_json = {
        "scripts": {
            "dev": "vite --host 0.0.0.0",
            "build": "vite build",
            "preview": "vite preview",
        },
        "dependencies": {
            "@vitejs/plugin-react": "latest",
            "vite": "latest",
            "typescript": "latest",
            "react": "latest",
            "react-dom": "latest",
            "lucide-react": "latest",
        },
        "devDependencies": {},
    }

    app_tsx = f"""import {{ ArrowRight, Check, Mail, Sparkles, Zap }} from 'lucide-react';

const features = [
  'Autonomous repair loop',
  'Multi-agent collaboration',
  'Template-guided generation',
  'Live local preview',
];

const sections = {json.dumps(sections)};

export default function App() {{
  return (
    <main className="app-shell">
      <nav className="nav">
        <div className="brand"><Sparkles size={{20}} /> {website_type}</div>
        <div className="nav-links">
          <a href="#features">Features</a>
          <a href="#pricing">Pricing</a>
          <a href="#contact">Contact</a>
        </div>
      </nav>

      <section className="hero">
        <div className="hero-copy">
          <span className="eyebrow">{theme} web engineering</span>
          <h1>Ship polished web pages with local AI agents.</h1>
          <p>
            A focused autonomous builder that plans, generates, validates, repairs,
            and previews production-ready React interfaces from a single prompt.
          </p>
          <div className="actions">
            <a className="primary" href="#contact">Start building <ArrowRight size={{18}} /></a>
            <a className="secondary" href="#features">View system</a>
          </div>
        </div>
        <div className="console-panel" aria-label="Builder pipeline">
          {{sections.map((section, index) => (
            <div className="pipeline-row" key={{section}}>
              <span>{{String(index + 1).padStart(2, '0')}}</span>
              <strong>{{section}}</strong>
              <Check size={{18}} />
            </div>
          ))}}
        </div>
      </section>

      <section id="features" className="section">
        <div className="section-heading">
          <span className="eyebrow">Core agents</span>
          <h2>Small team, strong workflow.</h2>
        </div>
        <div className="feature-grid">
          {{features.map((feature) => (
            <article className="feature-card" key={{feature}}>
              <Zap size={{22}} />
              <h3>{{feature}}</h3>
              <p>Designed for reliable generation, quick iteration, and readable project output.</p>
            </article>
          ))}}
        </div>
      </section>

      <section id="pricing" className="pricing">
        <div>
          <span className="eyebrow">MVP stack</span>
          <h2>Built for local-first experimentation.</h2>
          <p>Ollama models, sandboxed tools, deterministic templates, and a repair loop around real terminal feedback.</p>
        </div>
        <ul>
          {''.join(f"<li>{component}</li>" for component in components)}
        </ul>
      </section>

      <section id="contact" className="contact">
        <Mail size={{24}} />
        <h2>Ready for the next prompt.</h2>
        <p>Generate, validate, repair, and preview without leaving your local machine.</p>
        <a className="primary" href="mailto:hello@example.com">Contact team</a>
      </section>
    </main>
  );
}}
"""

    css = f""":root {{
  color: #172033;
  background: #f7f4ec;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}

* {{ box-sizing: border-box; }}
body {{ margin: 0; }}
a {{ color: inherit; text-decoration: none; }}

.app-shell {{
  min-height: 100vh;
  background:
    linear-gradient(135deg, rgba(26, 95, 122, 0.16), transparent 34%),
    linear-gradient(315deg, rgba(198, 74, 52, 0.16), transparent 30%),
    #f7f4ec;
}}

.nav {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  max-width: 1120px;
  margin: 0 auto;
  padding: 24px;
}}

.brand, .nav-links, .actions {{
  display: flex;
  align-items: center;
  gap: 14px;
}}

.brand {{ font-weight: 800; }}
.nav-links a {{ color: #536173; font-size: 14px; }}

.hero {{
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(320px, 0.9fr);
  gap: 40px;
  align-items: center;
  max-width: 1120px;
  margin: 0 auto;
  padding: 72px 24px 64px;
}}

.eyebrow {{
  color: #a83e2f;
  font-size: 13px;
  font-weight: 800;
  text-transform: uppercase;
}}

h1, h2, h3, p {{ margin-top: 0; }}
h1 {{ max-width: 720px; font-size: 64px; line-height: 1; margin-bottom: 24px; }}
h2 {{ font-size: 34px; margin-bottom: 16px; }}
p {{ color: #536173; font-size: 17px; line-height: 1.7; }}

.actions {{ flex-wrap: wrap; margin-top: 32px; }}
.primary, .secondary {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 8px;
  font-weight: 800;
}}
.primary {{ background: #1a5f7a; color: white; }}
.secondary {{ border: 1px solid rgba(23, 32, 51, 0.2); }}

.console-panel {{
  background: #172033;
  color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 28px 80px rgba(23, 32, 51, 0.22);
}}

.pipeline-row {{
  display: grid;
  grid-template-columns: 44px 1fr 24px;
  align-items: center;
  gap: 16px;
  padding: 16px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}}
.pipeline-row:last-child {{ border-bottom: 0; }}
.pipeline-row span {{ color: #f1b24a; }}

.section, .pricing, .contact {{
  max-width: 1120px;
  margin: 0 auto;
  padding: 64px 24px;
}}

.section-heading {{
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 28px;
}}

.feature-grid {{
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
}}

.feature-card {{
  min-height: 210px;
  padding: 22px;
  border: 1px solid rgba(23, 32, 51, 0.12);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.68);
}}
.feature-card svg {{ color: #1a5f7a; }}

.pricing {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 36px;
  align-items: start;
}}
.pricing ul {{
  display: grid;
  gap: 12px;
  padding: 0;
  margin: 0;
  list-style: none;
}}
.pricing li {{
  padding: 16px;
  border-left: 4px solid #1a5f7a;
  background: white;
  border-radius: 8px;
  font-weight: 700;
}}

.contact {{
  text-align: center;
  padding-bottom: 96px;
}}
.contact .primary {{ margin-top: 12px; }}

@media (max-width: 820px) {{
  .nav {{ align-items: flex-start; flex-direction: column; }}
  .hero, .pricing {{ grid-template-columns: 1fr; padding-top: 36px; }}
  h1 {{ font-size: 44px; }}
  .feature-grid {{ grid-template-columns: 1fr; }}
  .section-heading {{ display: block; }}
}}
"""

    return {
        "package.json": json.dumps(package_json, indent=2),
        "index.html": '<div id="root"></div><script type="module" src="/src/main.tsx"></script>',
        "tsconfig.json": json.dumps(
            {
                "compilerOptions": {
                    "target": "ES2020",
                    "useDefineForClassFields": True,
                    "lib": ["DOM", "DOM.Iterable", "ES2020"],
                    "allowJs": False,
                    "skipLibCheck": True,
                    "esModuleInterop": True,
                    "allowSyntheticDefaultImports": True,
                    "strict": True,
                    "forceConsistentCasingInFileNames": True,
                    "module": "ESNext",
                    "moduleResolution": "Node",
                    "resolveJsonModule": True,
                    "isolatedModules": True,
                    "noEmit": True,
                    "jsx": "react-jsx",
                },
                "include": ["src"],
                "references": [],
            },
            indent=2,
        ),
        "src/main.tsx": "import React from 'react';\nimport ReactDOM from 'react-dom/client';\nimport App from './App';\nimport './styles.css';\n\nReactDOM.createRoot(document.getElementById('root')!).render(\n  <React.StrictMode>\n    <App />\n  </React.StrictMode>,\n);\n",
        "src/App.tsx": app_tsx,
        "src/styles.css": css,
    }

