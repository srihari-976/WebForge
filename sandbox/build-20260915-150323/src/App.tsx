
      import React, { useState } from 'react';
      import { Search, Calendar, MapPin } from 'lucide-react';

      const App: React.FC = () => {
        const [searchTerm, setSearchTerm] = useState('');

        const destinations = [
          { id: 1, name: 'New York', location: 'USA' },
          { id: 2, name: 'Paris', location: 'France' },
          { id: 3, name: 'Tokyo', location: 'Japan' }
        ];

        const products = [
          { id: 1, name: 'Air Jordan 1 Retro High OG', price: 150, imageUrl: 'https://example.com/jordan1.jpg' },
          { id: 2, name: 'Nike Air Max 97', price: 180, imageUrl: 'https://example.com/max97.jpg' },
          { id: 3, name: 'Adidas Yeezy Boost 500', price: 220, imageUrl: 'https://example.com/yeezy500.jpg' }
        ];

        return (
          <div className="flex flex-col min-h-screen">
            <header className="bg-gray-900 text-white py-4 px-6">
              <nav className="container mx-auto flex justify-between items-center">
                <a href="#" className="text-xl font-bold">Sneaker Store</a>
                <div className="flex space-x-4">
                  <button className="p-2 rounded-lg hover:bg-gray-800">
                    <Search size={16} />
                  </button>
                  <button className="p-2 rounded-lg hover:bg-gray-800">
                    <Calendar size={16} />
                  </button>
                  <button className="p-2 rounded-lg hover:bg-gray-800">
                    <MapPin size={16} />
                  </button>
                </div>
              </nav>
            </header>

            <main className="container mx-auto mt-10">
              <section className="grid grid-cols-3 gap-4">
                {products.map(product => (
                  <div key={product.id} className="bg-white rounded-lg shadow-md p-6">
                    <img src={product.imageUrl} alt={product.name} className="w-full h-[200px] object-cover mb-4" />
                    <h3 className="text-xl font-bold">{product.name}</h3>
                    <p className="text-gray-700">${product.price}</p>
                  </div>
                ))}
              </section>

              <div className="mt-10">
                <h2 className="text-2xl font-bold">Destinations</h2>
                <ul className="list-disc pl-4 mt-2">
                  {destinations.map(destination => (
                    <li key={destination.id}>{destination.name} - {destination.location}</li>
                  ))}
                </ul>
              </div>

              <form className="mt-10">
                <h2 className="text-2xl font-bold">Contact Us</h2>
                <input
                  type="email"
                  placeholder="Email"
                  className="w-full p-2 rounded-lg mb-4"
                />
                <textarea
                  placeholder="Message"
                  rows={3}
                  className="w-full p-2 rounded-lg mb-4"
                />
                <button type="submit" className="bg-blue-500 text-white p-2 rounded-lg hover:bg-blue-600">
                  Submit
                </button>
              </form>
            </main>

            <footer className="bg-gray-900 text-white py-4 px-6">
              <div className="container mx-auto flex justify-between items-center">
                <p>&copy; 2023 Sneaker Store</p>
                <nav className="flex space-x-4">
                  <a href="#" className="text-sm font-bold">About Us</a>
                  <a href="#" className="text-sm font-bold">Contact Us</a>
                  <a href="#" className="text-sm font-bold">Privacy Policy</a>
                </nav>
              </div>
            </footer>
          </div>
        );
      };

      export default App;
    