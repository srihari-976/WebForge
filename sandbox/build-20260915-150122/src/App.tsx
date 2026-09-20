
      import React, { useState } from 'react';
      import { Search, Calendar, MapPin } from 'lucide-react';
      import './styles.css';

      const destinations = [
        { id: 1, name: 'Paris', image: '/images/paris.jpg' },
        { id: 2, name: 'New York', image: '/images/newyork.jpg' },
        { id: 3, name: 'Tokyo', image: '/images/tokyo.jpg' }
      ];

      const products = [
        { id: 1, title: 'Luxury Hotel Suite', price: '$500/night' },
        { id: 2, title: 'Beachfront Villa', price: '$400/night' },
        { id: 3, title: 'Mountain Cabin', price: '$300/night' }
      ];

      const App = () => {
        const [searchTerm, setSearchTerm] = useState('');
        const [selectedDestination, setSelectedDestination] = useState(null);

        return (
          <div className="flex flex-col min-h-screen">
            {/* Navigation */}
            <nav className="bg-gray-900 text-white py-4 px-6">
              <h1 className="text-xl font-bold">Travel Booking</h1>
              <ul className="flex space-x-4">
                <li><a href="#hero" className="hover:text-blue-500">Home</a></li>
                <li><a href="#destinations" className="hover:text-blue-500">Destinations</a></li>
                <li><a href="#featured-trips" className="hover:text-blue-500">Featured Trips</a></li>
              </ul>
            </nav>

            {/* Hero */}
            <section id="hero" className="bg-gray-100 py-24">
              <div className="container mx-auto px-6 flex items-center justify-between">
                <div className="flex flex-col space-y-4">
                  <h2 className="text-3xl font-bold">Explore the world</h2>
                  <p className="text-lg text-gray-700">Find your dream destination and book a trip today.</p>
                  <form className="flex items-center space-x-4">
                    <input
                      type="search"
                      placeholder="Search destinations..."
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      className="bg-white border rounded-md p-2 w-full focus:outline-none focus:border-blue-500"
                    />
                    <button className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600">
                      Search
                    </button>
                  </form>
                </div>
                <img src="/images/hero.jpg" alt="Hero Image" className="w-96 h-auto object-cover" />
              </div>
            </section>

            {/* Destinations */}
            <section id="destinations" className="bg-white py-24">
              <h2 className="text-3xl font-bold text-center">Explore destinations</h2>
              <div className="container mx-auto px-6 grid grid-cols-3 gap-8">
                {destinations.map((destination) => (
                  <div key={destination.id} className="bg-gray-100 rounded-lg p-4 shadow-md hover:shadow-xl transition duration-300">
                    <img src={destination.image} alt={destination.name} className="w-full h-auto object-cover mb-4" />
                    <h3 className="text-xl font-bold">{destination.name}</h3>
                  </div>
                ))}
              </div>
            </section>

            {/* Featured Trips */}
            <section id="featured-trips" className="bg-gray-900 text-white py-24">
              <h2 className="text-3xl font-bold text-center">Featured trips</h2>
              <div className="container mx-auto px-6 grid grid-cols-3 gap-8">
                {products.map((product) => (
                  <div key={product.id} className="bg-white rounded-lg p-4 shadow-md hover:shadow-xl transition duration-300">
                    <img src="/images/product.jpg" alt={product.title} className="w-full h-auto object-cover mb-4" />
                    <h3 className="text-xl font-bold">{product.title}</h3>
                    <p className="text-lg text-gray-700">{product.price}</p>
                  </div>
                ))}
              </div>
            </section>

            {/* Footer */}
            <footer className="bg-gray-900 text-white py-8 px-6">
              <div className="container mx-auto flex items-center justify-between">
                <p>&copy; 2023 Travel Booking. All rights reserved.</p>
                <ul className="flex space-x-4">
                  <li><a href="#hero" className="hover:text-blue-500">Home</a></li>
                  <li><a href="#destinations" className="hover:text-blue-500">Destinations</a></li>
                  <li><a href="#featured-trips" className="hover:text-blue-500">Featured Trips</a></li>
                </ul>
              </div>
            </footer>
          </div>
        );
      };

      export default App;
    