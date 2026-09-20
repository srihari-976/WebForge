import { Sparkles, Mail, ArrowRight, Zap, Check } from 'lucide-react';

const sections = ["hero", "features", "contact"];

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100 font-sans">
      <nav className="flex items-center justify-between max-w-7xl mx-auto px-6 py-5">
        <div className="flex items-center gap-2 font-bold text-xl text-slate-900">
          <Sparkles className="w-5 h-5 text-blue-600" /> E-Commerce/Travel Booking Website
        </div>
        <div className="hidden md:flex items-center gap-8">
          {sections.filter(s => s !== 'hero').map(sec => (
            <a key={sec} href={'#' + sec} className="text-sm text-slate-500 hover:text-slate-900 transition-colors">
              {sec.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}
            </a>
          ))}
        </div>
      </nav>

      <section className="max-w-7xl mx-auto px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
        <div>
          <span className="text-xs font-bold uppercase tracking-widest text-blue-600">Premium Design</span>
          <h1 className="mt-4 text-5xl md:text-6xl font-bold leading-tight text-slate-900">
            Your E-Commerce/Travel Booking Website built with modern style.
          </h1>
          <p className="mt-6 text-lg text-slate-500 leading-relaxed max-w-lg">
            Build a premium travel booking website with destination search, featured trips, and a booking form
          </p>
          <div className="mt-8 flex flex-wrap gap-4">
            <a href="#features" className="inline-flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors">
              Explore <ArrowRight className="w-4 h-4" />
            </a>
          </div>
        </div>
        <div className="bg-slate-900 text-white rounded-xl p-6 shadow-2xl">
          <p className="text-xs font-mono text-slate-400 mb-4">// sections</p>
          {sections.map((section, i) => (
            <div key={section} className="flex items-center gap-4 py-3 border-b border-white/10 last:border-0">
              <span className="font-mono text-yellow-400 text-sm w-8">{String(i + 1).padStart(2, '0')}</span>
              <strong className="flex-1 text-sm capitalize">{section.replace(/_/g, ' ')}</strong>
              <Check className="w-4 h-4 text-green-400" />
            </div>
          ))}
        </div>
      </section>

      <section id="features" className="max-w-7xl mx-auto px-6 py-20">
        <div className="mb-8">
          <span className="text-xs font-bold uppercase tracking-widest text-blue-600">Features</span>
          <h2 className="mt-2 text-3xl font-bold text-slate-900">What's included</h2>
        </div>
        <ul className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <li key="Real-time Search Functionality for Destinations" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Real-time Search Functionality for Destinations</li>
      <li key="User-Friendly Booking Form with Validation" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">User-Friendly Booking Form with Validation</li>
      <li key="Ability to Save and Reuse Searches" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Ability to Save and Reuse Searches</li>
      <li key="Trip Detail Page with Reviews and Ratings" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Trip Detail Page with Reviews and Ratings</li>
      <li key="Secure Payment Gateway Integration (Visa, Mastercard)" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Secure Payment Gateway Integration (Visa, Mastercard)</li>
      <li key="Personalized Recommendations Based on User History" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Personalized Recommendations Based on User History</li>
        </ul>
      </section>

      <section id="contact" className="max-w-7xl mx-auto px-6 py-20 text-center">
        <Mail className="w-8 h-8 text-blue-600 mx-auto mb-4" />
        <h2 className="text-3xl font-bold text-slate-900 mb-3">Ready to get started?</h2>
        <p className="text-slate-500 mb-6">Build something great with E-Commerce/Travel Booking Website.</p>
        <a href="mailto:hello@example.com" className="inline-flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors">
          Get in touch
        </a>
      </section>
    </div>
  );
}
