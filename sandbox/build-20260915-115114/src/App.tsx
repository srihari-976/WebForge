import { ArrowRight, Check, Mail, Sparkles, Zap } from 'lucide-react';

const features = ["User authentication for secure checkout", "Wishlist functionality", "Social media sharing buttons", "Newsletter subscription form", "Responsive design for mobile and desktop"];
const featureDescriptions: Record<string, string> = {"responsive": "Adapts seamlessly to all screen sizes and devices.", "dark mode": "Toggle between light and dark themes effortlessly.", "authentication": "Secure user login, signup, and session management.", "dashboard": "Real-time analytics and data visualization at a glance.", "search": "Fast full-text search with filters and sorting.", "notifications": "Real-time push notifications and alerts.", "api": "RESTful API endpoints for third-party integrations.", "database": "Persistent data storage with automatic backups.", "payments": "Secure payment processing with Stripe integration.", "analytics": "Track user behavior and conversion metrics.", "seo": "Optimized for search engines with metadata and sitemaps.", "testing": "Automated test suite for reliable deployments.", "ci/cd": "Continuous integration and deployment pipeline.", "containerized": "Docker-ready for consistent deployments."};
const sections = ["hero", "features", "contact"];

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100 font-sans">
      <nav className="flex items-center justify-between max-w-7xl mx-auto px-6 py-5">
        <div className="flex items-center gap-2 font-bold text-xl text-slate-900">
          <Sparkles className="w-5 h-5 text-primary-600" /> E-Commerce
        </div>
        <div className="hidden md:flex items-center gap-8">
          <a href="#features" className="text-sm text-slate-500 hover:text-slate-900 transition-colors">Features</a>
          <a href="#contact" className="text-sm text-slate-500 hover:text-slate-900 transition-colors">Contact</a>
        </div>
      </nav>

      <section className="max-w-7xl mx-auto px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
        <div>
          <span className="text-xs font-bold uppercase tracking-widest text-primary-600">premium and modern design</span>
          <h1 className="mt-4 text-5xl md:text-6xl font-bold leading-tight text-slate-900">
            Your E-Commerce built with premium and modern style.
          </h1>
          <p className="mt-6 text-lg text-slate-500 leading-relaxed max-w-lg">
            Use a clean, modern color palette with high contrast text and images. Ensure all elements are visually appealing and easy to navigate.
          </p>
          <div className="mt-8 flex flex-wrap gap-4">
            <a href="#features" className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-primary-700 transition-colors">
              Explore features <ArrowRight className="w-4 h-4" />
            </a>
            <a href='#contact' className='inline-flex items-center gap-2 border border-slate-200 px-6 py-3 rounded-lg font-bold text-slate-700 hover:bg-slate-50 transition-colors'>Contact us</a>
          </div>
        </div>
        <div className="bg-slate-900 text-white rounded-xl p-6 shadow-2xl">
          <p className="text-xs font-mono text-slate-400 mb-4">// sections</p>
          {sections.map((section, index) => (
            <div key={section} className="flex items-center gap-4 py-3 border-b border-white/10 last:border-0">
              <span className="font-mono text-yellow-400 text-sm w-8">{String(index + 1).padStart(2, '0')}</span>
              <strong className="flex-1 text-sm capitalize">{section.replace(/_/g, ' ')}</strong>
              <Check className="w-4 h-4 text-green-400" />
            </div>
          ))}
        </div>
      </section>

      <section id="features" className="max-w-7xl mx-auto px-6 py-20">
        <div className="mb-8">
          <span className="text-xs font-bold uppercase tracking-widest text-primary-600">Features</span>
          <h2 className="mt-2 text-3xl font-bold text-slate-900">What makes this e-commerce great.</h2>
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
            <article key={features[0]} className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">{features[0]}</h3>
              <p className="text-sm text-slate-500">{featureDescriptions[features[0]] || 'Built for reliable performance and great user experience.'}</p>
            </article>
            <article key={features[1]} className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">{features[1]}</h3>
              <p className="text-sm text-slate-500">{featureDescriptions[features[1]] || 'Built for reliable performance and great user experience.'}</p>
            </article>
            <article key={features[2]} className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">{features[2]}</h3>
              <p className="text-sm text-slate-500">{featureDescriptions[features[2]] || 'Built for reliable performance and great user experience.'}</p>
            </article>
            <article key={features[3]} className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">{features[3]}</h3>
              <p className="text-sm text-slate-500">{featureDescriptions[features[3]] || 'Built for reliable performance and great user experience.'}</p>
            </article>
            <article key={features[4]} className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">{features[4]}</h3>
              <p className="text-sm text-slate-500">{featureDescriptions[features[4]] || 'Built for reliable performance and great user experience.'}</p>
            </article>
        </div>
      </section>


      <section id="contact" className="max-w-7xl mx-auto px-6 py-20 text-center">
        <Mail className="w-8 h-8 text-primary-600 mx-auto mb-4" />
        <h2 className="text-3xl font-bold text-slate-900 mb-3">Ready to get started?</h2>
        <p className="text-slate-500 mb-6">Generate your E-Commerce today and ship it to production.</p>
        <a href="mailto:hello@example.com" className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-primary-700 transition-colors">
          Get in touch
        </a>
      </section>
    </div>
  );
}
