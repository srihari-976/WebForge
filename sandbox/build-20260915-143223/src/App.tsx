import { Sparkles, Mail, ArrowRight, Zap, Check } from 'lucide-react';

const sections = ["hero", "features", "contact"];

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100 font-sans">
      <nav className="flex items-center justify-between max-w-7xl mx-auto px-6 py-5">
        <div className="flex items-center gap-2 font-bold text-xl text-slate-900">
          <Sparkles className="w-5 h-5 text-blue-600" /> Travel Booking Website
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
            Your Travel Booking Website built with modern style.
          </h1>
          <p className="mt-6 text-lg text-slate-500 leading-relaxed max-w-lg">
            Build a premium travel booking website for European destinations with a large hero section, destination cards, search filters, itinerary section, hotel recommendations, and responsive design
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
      <li key="Large Hero Section for Promoting Destinations" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Large Hero Section for Promoting Destinations</li>
      <li key="Filterable Search Functionality to Find Specific Destinations and Accommodations" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Filterable Search Functionality to Find Specific Destinations and Accommodations</li>
      <li key="Detailed Itinerary View for Booking Management" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Detailed Itinerary View for Booking Management</li>
      <li key="Responsive Design for Mobile and Desktop Devices" className="p-4 bg-white rounded-lg shadow-sm border border-gray-100">Responsive Design for Mobile and Desktop Devices</li>
        </ul>
      </section>

      <section id="contact" className="max-w-7xl mx-auto px-6 py-20 text-center">
        <Mail className="w-8 h-8 text-blue-600 mx-auto mb-4" />
        <h2 className="text-3xl font-bold text-slate-900 mb-3">Ready to get started?</h2>
        <p className="text-slate-500 mb-6">Build something great with Travel Booking Website.</p>
        <a href="mailto:hello@example.com" className="inline-flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors">
          Get in touch
        </a>
      </section>
    </div>
  );
}
