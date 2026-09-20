
      import React, { useState } from 'react';
      import { IconSearch } from '@lucide-react/search';
      import { IconCalendar } from '@lucide-react/calendar';
      import { IconLocationMarker } from '@lucide-react/location-marker';
      import { IconHeart } from '@lucide-react/heart';
      import { IconStar } from '@lucide-react/star';
      import { IconArrowRight } from '@lucide-react/arrow-right';

      const destinations = [
        { id: 1, name: 'Paris', image: 'https://via.placeholder.com/300x200?text=Paris' },
        { id: 2, name: 'New York', image: 'https://via.placeholder.com/300x200?text=New+York' },
        // Add more destinations as needed
      ];

      const products = [
        { id: 1, title: 'Luxury Hotel in Paris', price: '$450/night', description: 'Experience the best of Paris with our luxurious hotel.' },
        { id: 2, title: 'Escape to Bali', price: '$350/day', description: 'Discover the beauty of Bali on a luxury vacation package.' },
        // Add more products as needed
      ];

      const App = () => {
        const [searchTerm, setSearchTerm] = useState('');
        const [selectedDestination, setSelectedDestination] = useState(null);

        return (
          <div className="bg-gray-100 min-h-screen">
            {/* Navigation */}
            <nav className="bg-white shadow-md py-4 px-6 flex justify-between items-center">
              <h1 className="text-xl font-bold">Travel Booking</h1>
              <form className="flex items-center">
                <IconSearch size={24} className="mr-2" />
                <input
                  type="text"
                  placeholder="Search destinations"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="bg-gray-100 p-2 rounded-md focus:outline-none focus:bg-white"
                />
              </form>
            </nav>

            {/* Hero */}
            <div className="bg-gray-50 py-16">
              <h2 className="text-3xl font-bold text-center mb-4">Explore the world</h2>
              <p className="text-lg text-center mb-8">Find your next adventure with us.</p>
              <form className="flex items-center justify-center">
                <input
                  type="date"
                  className="bg-gray-100 p-2 rounded-md focus:outline-none focus:bg-white mr-4"
                />
                <button className="bg-blue-500 text-white font-bold py-2 px-4 rounded-md hover:bg-blue-700">
                  Search
                </button>
              </form>
            </div>

            {/* Content */}
            <main className="container mx-auto p-6">
              {/* Featured Destinations */}
              <section className="mb-12">
                <h3 className="text-xl font-bold mb-4">Featured Destinations</h3>
                <div className="grid grid-cols-3 gap-8">
                  {destinations.map((destination) => (
                    <div key={destination.id} className="bg-white shadow-md p-6 rounded-lg">
                      <img src={destination.image} alt={destination.name} className="w-full h-40 object-cover mb-4" />
                      <h4 className="text-xl font-bold">{destination.name}</h4>
                      <p className="text-gray-500">Explore {destination.name} and discover its beauty.</p>
                      <button
                        onClick={() => setSelectedDestination(destination)}
                        className="bg-blue-500 text-white font-bold py-2 px-4 rounded-md hover:bg-blue-700"
                      >
                        View Details
                      </button>
                    </div>
                  ))}
                </div>
              </section>

              {/* Featured Products */}
              <section className="mb-12">
                <h3 className="text-xl font-bold mb-4">Featured Products</h3>
                <div className="grid grid-cols-3 gap-8">
                  {products.map((product) => (
                    <div key={product.id} className="bg-white shadow-md p-6 rounded-lg">
                      <img src="https://via.placeholder.com/200x150?text=Product" alt={product.title} className="w-full h-40 object-cover mb-4" />
                      <h4 className="text-xl font-bold">{product.title}</h4>
                      <p className="text-gray-500">${product.price}/night</p>
                      <p>{product.description}</p>
                      <button
                        onClick={() => setSelectedDestination(product)}
                        className="bg-blue-500 text-white font-bold py-2 px-4 rounded-md hover:bg-blue-700"
                      >
                        Book Now
                      </button>
                    </div>
                  ))}
                </div>
              </section>

              {/* Booking Form */}
              {selectedDestination && (
                <form className="bg-white shadow-md p-6 rounded-lg mb-12">
                  <h3 className="text-xl font-bold mb-4">Book Now</h3>
                  <div className="mb-4">
                    <label htmlFor="destination" className="block text-gray-700 font-bold mb-2">
                      Destination
                    </label>
                    <input
                      type="text"
                      id="destination"
                      value={selectedDestination.name}
                      readOnly
                      className="bg-gray-100 p-2 rounded-md focus:outline-none focus:bg-white"
                    />
                  </div>
                  {/* Add more form fields as needed */}
                  <button
                    type="submit"
                    className="bg-blue-500 text-white font-bold py-2 px-4 rounded-md hover:bg-blue-700"
                  >
                    Submit Booking
                  </button>
                </form>
              )}
            </main>

            {/* Footer */}
            <footer className="bg-gray-900 text-white p-6">
              <p>&copy; 2023 Travel Booking. All rights reserved.</p>
            </footer>
          </div>
        );
      };

      export default App;
    