import { ArrowRight, Check, Mail, Sparkles, Zap } from 'lucide-react';

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100 font-sans">
      <nav className="flex items-center justify-between max-w-7xl mx-auto px-6 py-5">
        <div className="flex items-center gap-2 font-bold text-xl text-slate-900">
          <Sparkles className="w-5 h-5 text-primary-600" /> Travel Booking Website
        </div>
        <div className="hidden md:flex items-center gap-8">
          <a href="#features" className="text-sm text-slate-500 hover:text-slate-900 transition-colors">Features</a>
          <a href="#contact" className="text-sm text-slate-500 hover:text-slate-900 transition-colors">Contact</a>
        </div>
      </nav>

      <section className="max-w-7xl mx-auto px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
        <div>
          <span className="text-xs font-bold uppercase tracking-widest text-primary-600">Premium and Modern design</span>
          <h1 className="mt-4 text-5xl md:text-6xl font-bold leading-tight text-slate-900">
            Your Travel Booking Website built with Premium and Modern style.
          </h1>
          <p className="mt-6 text-lg text-slate-500 leading-relaxed max-w-lg">
            Use a modern color palette and typography, ensuring consistency across all pages. Implement hover effects and transitions for interactive components.
          </p>
          <div className="mt-8 flex flex-wrap gap-4">
            <a href="#features" className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-primary-700 transition-colors">
              Explore features <ArrowRight className="w-4 h-4" />
            </a>
          </div>
        </div>
        <div className="bg-slate-900 text-white rounded-xl p-6 shadow-2xl">
          <p className="text-xs font-mono text-slate-400 mb-4">// sections</p>
            <div className="flex items-center gap-4 py-3 border-b border-white/10 last:border-0">
              <span className="font-mono text-yellow-400 text-sm w-8">01</span>
              <strong className="flex-1 text-sm capitalize">hero</strong>
              <Check className="w-4 h-4 text-green-400" />
            </div>
            <div className="flex items-center gap-4 py-3 border-b border-white/10 last:border-0">
              <span className="font-mono text-yellow-400 text-sm w-8">02</span>
              <strong className="flex-1 text-sm capitalize">features</strong>
              <Check className="w-4 h-4 text-green-400" />
            </div>
            <div className="flex items-center gap-4 py-3 border-b border-white/10 last:border-0">
              <span className="font-mono text-yellow-400 text-sm w-8">03</span>
              <strong className="flex-1 text-sm capitalize">contact</strong>
              <Check className="w-4 h-4 text-green-400" />
            </div>
        </div>
      </section>

      <section id="features" className="max-w-7xl mx-auto px-6 py-20">
        <div className="mb-8">
          <span className="text-xs font-bold uppercase tracking-widest text-primary-600">Features</span>
          <h2 className="mt-2 text-3xl font-bold text-slate-900">What makes this great.</h2>
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
            <article className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">Large Hero Section with High-Resolution Images</h3>
              <p className="text-sm text-slate-500">Built for reliable performance and great user experience.</p>
            </article>
            <article className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">Responsive Design for Mobile and Desktop</h3>
              <p className="text-sm text-slate-500">Built for reliable performance and great user experience.</p>
            </article>
            <article className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">Multiple Destination Cards with Detailed Information</h3>
              <p className="text-sm text-slate-500">Built for reliable performance and great user experience.</p>
            </article>
            <article className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">Advanced Search Filters for Filtering Destinations by Criteria</h3>
              <p className="text-sm text-slate-500">Built for reliable performance and great user experience.</p>
            </article>
            <article className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">Interactive Itinerary Section to Plan Trips</h3>
              <p className="text-sm text-slate-500">Built for reliable performance and great user experience.</p>
            </article>
            <article className="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
              <Zap className="w-6 h-6 text-primary-600 mb-3" />
              <h3 className="font-bold text-slate-900 mb-1">Hotel Recommendations Based on User Preferences</h3>
              <p className="text-sm text-slate-500">Built for reliable performance and great user experience.</p>
            </article>
        </div>
      </section>


      <section id="contact" className="max-w-7xl mx-auto px-6 py-20 text-center">
        <Mail className="w-8 h-8 text-primary-600 mx-auto mb-4" />
        <h2 className="text-3xl font-bold text-slate-900 mb-3">Ready to get started?</h2>
        <p className="text-slate-500 mb-6">Generate your Travel Booking Website today.</p>
        <a href="mailto:hello@example.com" className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-primary-700 transition-colors">Get in touch</a>
      </section>
    </div>
  );
}
