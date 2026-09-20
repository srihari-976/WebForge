
      import React, { useState } from 'react';
      import { IconSearch } from '@lucide-react/search';
      import { twMerge } from 'tailwind-merge';

      const destinations = [
        { id: 1, name: 'Paris', image: '/paris.jpg' },
        { id: 2, name: 'London', image: '/london.jpg' },
        { id: 3, name: 'Berlin', image: '/berlin.jpg' },
        // Add more destinations as needed
      ];

      const products = [
        { id: 1, name: 'Paris Hotel', price: '$200/night', image: '/paris-hotel.jpg' },
        { id: 2, name: 'London Apartment', price: '$350/night', image: '/london-apartment.jpg' },
        // Add more products as needed
      ];

      const App = () => {
        const [searchTerm, setSearchTerm] = useState('');

        const filteredDestinations = destinations.filter((dest) =>
          dest.name.toLowerCase().includes(searchTerm.toLowerCase())
        );

        return (
          <div className="flex flex-col min-h-screen">
            <header className="bg-blue-500 text-white p-4">
              <h1 className="text-3xl font-bold">Travel Booking</h1>
              <input
                type="search"
                placeholder="Search destinations..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="bg-gray-200 p-2 rounded-l-full w-full focus:outline-none focus:bg-white"
              />
              <button className="bg-blue-700 text-white p-2 rounded-r-full">
                <IconSearch size={16} />
              </button>
            </header>

            <main className="flex-grow p-4">
              <div className="max-w-3xl mx-auto">
                <h2 className="text-2xl font-bold mb-4">Explore Europe</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {filteredDestinations.map((dest) => (
                    <div
                      key={dest.id}
                      className="bg-white rounded-lg shadow-md p-4"
                    >
                      <img src={dest.image} alt={dest.name} className="w-full h-60 object-cover mb-2" />
                      <h3 className="text-xl font-bold">{dest.name}</h3>
                      {/* Add more details as needed */}
                    </div>
                  ))}
                </div>

                <section className="mt-8">
                  <h2 className="text-2xl font-bold mb-4">Itinerary</h2>
                  {/* Add itinerary section content here */}
                </section>

                <section className="mt-8">
                  <h2 className="text-2xl font-bold mb-4">Hotel Recommendations</h2>
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {products.map((product) => (
                      <div
                        key={product.id}
                        className="bg-white rounded-lg shadow-md p-4"
                      >
                        <img src={product.image} alt={product.name} className="w-full h-60 object-cover mb-2" />
                        <h3 className="text-xl font-bold">{product.name}</h3>
                        <p className="text-gray-700">Price: ${product.price}</p>
                      </div>
                    ))}
                  </div>
                </section>
              </div>
            </main>

            <footer className="bg-blue-500 text-white p-4">
              <p>&copy; 2023 Travel Booking</p>
            </footer>
          </div>
        );
      };

      export default App;
    