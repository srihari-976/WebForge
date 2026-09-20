import { useState, useMemo } from 'react';
import { Search, ShoppingCart, Heart, Star, Filter, X, Plus, Minus, Menu, ChevronDown, Check, ArrowRight, Mail, Sparkles, Zap, Eye } from 'lucide-react';

type Product = {
  id: number;
  name: string;
  price: number;
  category: string;
  rating: number;
  reviews: number;
  image: string;
  colors: string[];
  sizes: string[];
  description: string;
  badge?: string;
};

type CartItem = Product & { quantity: number; selectedColor: string; selectedSize: string };

const categories = ['All', 'Running', 'Lifestyle', 'Basketball', 'Casual'];
const sortOptions = ['Featured', 'Price: Low to High', 'Price: High to Low', 'Newest', 'Best Rating'];

const products: Product[] = [
  { id: 1, name: 'Air Max Pulse', price: 159.99, category: 'Running', rating: 4.8, reviews: 234, image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=400&fit=crop', colors: ['#000', '#fff', '#e74c3c'], sizes: ['7', '8', '9', '10', '11', '12'], description: 'Ultra-lightweight running shoe with Max Air cushioning for a responsive ride.', badge: 'New' },
  { id: 2, name: 'Retro Boost 990', price: 189.99, category: 'Lifestyle', rating: 4.6, reviews: 189, image: 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400&h=400&fit=crop', colors: ['#333', '#8B4513', '#4a6fa5'], sizes: ['7', '8', '9', '10', '11'], description: 'Classic silhouette meets modern comfort with premium suede and mesh upper.' },
  { id: 3, name: 'Court Vision Low', price: 89.99, category: 'Basketball', rating: 4.4, reviews: 567, image: 'https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?w=400&h=400&fit=crop', colors: ['#000', '#fff', '#c0392b'], sizes: ['8', '9', '10', '11', '12', '13'], description: 'Court-inspired style with padded collar for comfort and durability.' },
  { id: 4, name: 'Urban Runner Pro', price: 134.99, category: 'Running', rating: 4.7, reviews: 312, image: 'https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=400&h=400&fit=crop', colors: ['#2c3e50', '#27ae60', '#e67e22'], sizes: ['7', '8', '9', '10', '11'], description: 'Responsive foam midsole with breathable mesh for all-day comfort.' },
  { id: 5, name: 'Heritage Classic', price: 119.99, category: 'Lifestyle', rating: 4.5, reviews: 445, image: 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=400&h=400&fit=crop', colors: ['#8B4513', '#000', '#f5f5dc'], sizes: ['8', '9', '10', '11', '12'], description: 'Timeless design with premium leather upper and rubber cupsole.' },
  { id: 6, name: 'Speed Elite', price: 219.99, category: 'Running', rating: 4.9, reviews: 156, image: 'https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?w=400&h=400&fit=crop', colors: ['#e74c3c', '#3498db', '#000'], sizes: ['7', '8', '9', '10', '11', '12'], description: 'Carbon plate technology for maximum energy return and speed.', badge: 'Popular' },
  { id: 7, name: 'Cloud Walker', price: 99.99, category: 'Casual', rating: 4.3, reviews: 678, image: 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400&h=400&fit=crop', colors: ['#ecf0f1', '#34495e', '#9b59b6'], sizes: ['7', '8', '9', '10', '11'], description: 'Ultra-soft Cloudfoam midsole for step-in comfort and all-day wear.' },
  { id: 8, name: 'Trail Blazer', price: 149.99, category: 'Running', rating: 4.6, reviews: 203, image: 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=400&h=400&fit=crop', colors: ['#27ae60', '#2c3e50', '#e67e22'], sizes: ['8', '9', '10', '11', '12'], description: 'Aggressive traction pattern for grip on any terrain.' },
];

const navLinks = ['Home', 'Shop', 'Featured', 'Contact'];

export default function App() {
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [searchQuery, setSearchQuery] = useState('');
  const [sortBy, setSortBy] = useState('Featured');
  const [cart, setCart] = useState<CartItem[]>([]);
  const [wishlist, setWishlist] = useState<number[]>([]);
  const [showCart, setShowCart] = useState(false);
  const [showFilters, setShowFilters] = useState(false);
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);
  const [mobileMenu, setMobileMenu] = useState(false);

  const filteredProducts = useMemo(() => {
    let result = products.filter(p =>
      (selectedCategory === 'All' || p.category === selectedCategory) &&
      (p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
       p.category.toLowerCase().includes(searchQuery.toLowerCase()))
    );
    switch (sortBy) {
      case 'Price: Low to High': return [...result].sort((a, b) => a.price - b.price);
      case 'Price: High to Low': return [...result].sort((a, b) => b.price - a.price);
      case 'Newest': return [...result].sort((a, b) => b.id - a.id);
      case 'Best Rating': return [...result].sort((a, b) => b.rating - a.rating);
      default: return result;
    }
  }, [selectedCategory, searchQuery, sortBy]);

  const cartTotal = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const cartCount = cart.reduce((sum, item) => sum + item.quantity, 0);

  const addToCart = (product: Product) => {
    setCart(prev => {
      const existing = prev.find(i => i.id === product.id);
      if (existing) return prev.map(i => i.id === product.id ? { ...i, quantity: i.quantity + 1 } : i);
      return [...prev, { ...product, quantity: 1, selectedColor: product.colors[0], selectedSize: product.sizes[2] }];
    });
  };

  const updateQuantity = (id: number, delta: number) => {
    setCart(prev => prev.map(item =>
      item.id === id ? { ...item, quantity: Math.max(0, item.quantity + delta) } : item
    ).filter(item => item.quantity > 0));
  };

  const toggleWishlist = (id: number) => {
    setWishlist(prev => prev.includes(id) ? prev.filter(i => i !== id) : [...prev, id]);
  };

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      <nav className="bg-white shadow-sm sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-2">
              <Sparkles className="w-6 h-6 text-primary-600" />
              <span className="text-xl font-bold text-gray-900">E-Commerce</span>
            </div>
            <div className="hidden md:flex items-center gap-8">
              {navLinks.map(link => (
                <a key={link} href={link === 'Shop' ? '#shop' : link === 'Contact' ? '#contact' : '#'}
                   className="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">
                  {link}
                </a>
              )))}
            </div>
            <div className="flex items-center gap-4">
              <button onClick={() => setShowCart(true)} className="relative p-2 text-gray-600 hover:text-gray-900">
                <ShoppingCart className="w-5 h-5" />
                {cartCount > 0 && (
                  <span className="absolute -top-1 -right-1 bg-primary-600 text-white text-xs w-5 h-5 rounded-full flex items-center justify-center font-bold">
                    {cartCount}
                  </span>
                )}
              </button>
              <button onClick={() => setMobileMenu(!mobileMenu)} className="md:hidden p-2 text-gray-600">
                <Menu className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
        {mobileMenu && (
          <div className="md:hidden border-t bg-white px-4 py-3 space-y-2">
            {navLinks.map(link => (
              <a key={link} href="#" className="block py-2 text-sm font-medium text-gray-600 hover:text-gray-900">{link}</a>
            ))}
          </div>
        )}
      </nav>

      <section className="bg-gradient-to-r from-gray-900 to-gray-800 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24">
          <div className="max-w-2xl">
            <span className="inline-block bg-primary-600 text-white text-xs font-bold px-3 py-1 rounded-full mb-4 uppercase tracking-wider">Premium Collection</span>
            <h1 className="text-4xl md:text-6xl font-extrabold leading-tight mb-6">
              Step Into Your<br />New Style
            </h1>
            <p className="text-lg text-gray-300 mb-8 max-w-lg">
              Discover our curated collection of premium sneakers designed for comfort, performance, and style.
            </p>
            <a href="#shop" className="inline-flex items-center gap-2 bg-primary-600 hover:bg-primary-700 text-white px-8 py-3 rounded-lg font-bold transition-colors">
              Shop Now <ArrowRight className="w-4 h-4" />
            </a>
          </div>
        </div>
      </section>

      <section id="shop" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="flex flex-col lg:flex-row gap-8">
          <aside className={showFilters ? 'block' : 'hidden lg:block'} className="lg:w-64 shrink-0">
            <div className="bg-white rounded-xl p-6 shadow-sm sticky top-20">
              <div className="flex items-center justify-between mb-4">
                <h3 className="font-bold text-gray-900">Filters</h3>
                <button onClick={() => setShowFilters(false)} className="lg:hidden text-gray-400 hover:text-gray-600">
                  <X className="w-5 h-5" />
                </button>
              </div>
              <div className="mb-6">
                <label className="text-sm font-medium text-gray-700 mb-3 block">Search</label>
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                  <input
                    type="text"
                    placeholder="Search sneakers..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full pl-10 pr-4 py-2 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
                  />
                </div>
              </div>
              <div className="mb-6">
                <label className="text-sm font-medium text-gray-700 mb-3 block">Category</label>
                <div className="space-y-1">
                  {categories.map(cat => (
                    <button
                      key={cat}
                      onClick={() => setSelectedCategory(cat)}
                      className={`w-full text-left px-3 py-2 rounded-lg text-sm transition-colors ${selectedCategory === cat ? 'bg-primary-50 text-primary-700 font-medium' : 'text-gray-600 hover:bg-gray-50'}`}
                    >
                      {cat}
                    </button>
                  ))}
                </div>
              </div>
              <div>
                <label className="text-sm font-medium text-gray-700 mb-3 block">Sort By</label>
                <select
                  value={sortBy}
                  onChange={(e) => setSortBy(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
                >
                  {sortOptions.map(opt => (
                    <option key={opt} value={opt}>{opt}</option>
                  ))}
                </select>
              </div>
            </div>
          </aside>

          <main className="flex-1">
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-3">
                <h2 className="text-2xl font-bold text-gray-900">
                  {selectedCategory === 'All' ? 'All Sneakers' : selectedCategory}
                </h2>
                <span className="text-sm text-gray-500">({filteredProducts.length} products)</span>
              </div>
              <button onClick={() => setShowFilters(!showFilters)} className="lg:hidden p-2 border rounded-lg text-gray-600 hover:bg-gray-50">
                <Filter className="w-5 h-5" />
              </button>
            </div>

            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredProducts.map(product => (
                <div key={product.id} className="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition-shadow group">
                  <div className="relative aspect-square bg-gray-100 overflow-hidden">
                    <img src={product.image} alt={product.name} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" />
                    {product.badge && (
                      <span className="absolute top-3 left-3 bg-primary-600 text-white text-xs font-bold px-2 py-1 rounded">
                        {product.badge}
                      </span>
                    )}
                    <button
                      onClick={() => toggleWishlist(product.id)}
                      className="absolute top-3 right-3 w-8 h-8 bg-white rounded-full flex items-center justify-center shadow-sm hover:scale-110 transition-transform"
                    >
                      <Heart className={`w-4 h-4 ${wishlist.includes(product.id) ? 'fill-red-500 text-red-500' : 'text-gray-400'}`} />
                    </button>
                    <button
                      onClick={() => setSelectedProduct(product)}
                      className="absolute bottom-3 right-3 w-8 h-8 bg-white rounded-full items-center justify-center shadow-sm hover:scale-110 transition-transform hidden group-hover:flex"
                    >
                      <Eye className="w-4 h-4 text-gray-600" />
                    </button>
                  </div>
                  <div className="p-4">
                    <p className="text-xs text-gray-500 mb-1">{product.category}</p>
                    <h3 className="font-bold text-gray-900 mb-1">{product.name}</h3>
                    <div className="flex items-center gap-1 mb-2">
                      {[1,2,3,4,5].map(s => (
                        <Star key={s} className={`w-3.5 h-3.5 ${s <= Math.round(product.rating) ? 'fill-yellow-400 text-yellow-400' : 'text-gray-200'}`} />
                      ))}
                      <span className="text-xs text-gray-500 ml-1">({product.reviews})</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-lg font-bold text-gray-900">${product.price.toFixed(2)}</span>
                      <button
                        onClick={() => addToCart(product)}
                        className="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-lg text-sm font-medium transition-colors"
                      >
                        Add to Cart
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
            {filteredProducts.length === 0 && (
              <div className="text-center py-16">
                <Search className="w-12 h-12 text-gray-300 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900 mb-1">No products found</h3>
                <p className="text-gray-500">Try adjusting your search or filter criteria</p>
              </div>
            )}
          </main>
        </div>
      </section>

      {selectedProduct && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4" onClick={() => setSelectedProduct(null)}>
          <div className="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto" onClick={e => e.stopPropagation()}>
            <div className="relative">
              <img src={selectedProduct.image} alt={selectedProduct.name} className="w-full aspect-video object-cover" />
              <button onClick={() => setSelectedProduct(null)} className="absolute top-4 right-4 w-8 h-8 bg-white rounded-full flex items-center justify-center shadow hover:scale-110">
                <X className="w-4 h-4" />
              </button>
            </div>
            <div className="p-6">
              <p className="text-sm text-gray-500 mb-1">{selectedProduct.category}</p>
              <h2 className="text-2xl font-bold text-gray-900 mb-2">{selectedProduct.name}</h2>
              <div className="flex items-center gap-2 mb-4">
                <div className="flex">
                  {[1,2,3,4,5].map(s => (
                    <Star key={s} className={`w-4 h-4 ${s <= Math.round(selectedProduct.rating) ? 'fill-yellow-400 text-yellow-400' : 'text-gray-200'}`} />
                  ))}
                </div>
                <span className="text-sm text-gray-500">{selectedProduct.rating} ({selectedProduct.reviews} reviews)</span>
              </div>
              <p className="text-gray-600 mb-6">{selectedProduct.description}</p>
              <div className="mb-4">
                <p className="text-sm font-medium text-gray-700 mb-2">Colors</p>
                <div className="flex gap-2">
                  {selectedProduct.colors.map(color => (
                    <button key={color} className="w-8 h-8 rounded-full border-2 border-gray-200 hover:border-gray-400" style={{ backgroundColor: color }} />
                  ))}
                </div>
              </div>
              <div className="mb-6">
                <p className="text-sm font-medium text-gray-700 mb-2">Sizes</p>
                <div className="flex flex-wrap gap-2">
                  {selectedProduct.sizes.map(size => (
                    <button key={size} className="px-4 py-2 border border-gray-200 rounded-lg text-sm hover:border-gray-400 hover:bg-gray-50">
                      {size}
                    </button>
                  ))}
                </div>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-3xl font-bold text-gray-900">${selectedProduct.price.toFixed(2)}</span>
                <button
                  onClick={() => { addToCart(selectedProduct); setSelectedProduct(null); } }
                  className="bg-primary-600 hover:bg-primary-700 text-white px-8 py-3 rounded-lg font-bold transition-colors"
                >
                  Add to Cart
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {showCart && (
        <div className="fixed inset-0 z-50 flex justify-end bg-black/50" onClick={() => setShowCart(false)}>
          <div className="bg-white w-full max-w-md h-full overflow-y-auto shadow-2xl" onClick={e => e.stopPropagation()}>
            <div className="p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-xl font-bold text-gray-900">Shopping Cart ({cartCount})</h2>
                <button onClick={() => setShowCart(false)} className="text-gray-400 hover:text-gray-600">
                  <X className="w-5 h-5" />
                </button>
              </div>
              {cart.length === 0 ? (
                <div className="text-center py-12">
                  <ShoppingCart className="w-12 h-12 text-gray-300 mx-auto mb-4" />
                  <p className="text-gray-500">Your cart is empty</p>
                </div>
              ) : (
                <>
                  <div className="space-y-4 mb-6">
                    {cart.map(item => (
                      <div key={item.id} className="flex gap-4 p-4 bg-gray-50 rounded-xl">
                        <img src={item.image} alt={item.name} className="w-20 h-20 object-cover rounded-lg" />
                        <div className="flex-1">
                          <h4 className="font-medium text-gray-900 text-sm">{item.name}</h4>
                          <p className="text-xs text-gray-500 mt-0.5">{item.selectedSize} / {item.selectedColor}</p>
                          <p className="font-bold text-gray-900 mt-1">${(item.price * item.quantity).toFixed(2)}</p>
                          <div className="flex items-center gap-2 mt-2">
                            <button onClick={() => updateQuantity(item.id, -1)} className="w-6 h-6 rounded bg-gray-200 flex items-center justify-center hover:bg-gray-300">
                              <Minus className="w-3 h-3" />
                            </button>
                            <span className="text-sm font-medium w-6 text-center">{item.quantity}</span>
                            <button onClick={() => updateQuantity(item.id, 1)} className="w-6 h-6 rounded bg-gray-200 flex items-center justify-center hover:bg-gray-300">
                              <Plus className="w-3 h-3" />
                            </button>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                  <div className="border-t pt-4">
                    <div className="flex justify-between mb-2">
                      <span className="text-gray-600">Subtotal</span>
                      <span className="font-bold text-gray-900">${cartTotal.toFixed(2)}</span>
                    </div>
                    <div className="flex justify-between mb-4">
                      <span className="text-gray-600">Shipping</span>
                      <span className="font-bold text-green-600">Free</span>
                    </div>
                    <div className="flex justify-between mb-6 text-lg">
                      <span className="font-bold text-gray-900">Total</span>
                      <span className="font-bold text-gray-900">${cartTotal.toFixed(2)}</span>
                    </div>
                    <button className="w-full bg-primary-600 hover:bg-primary-700 text-white py-3 rounded-lg font-bold transition-colors">
                      Checkout
                    </button>
                  </div>
                </>
              )}
            </div>
          </div>
        </div>
      )}

      <section id="contact" className="bg-gray-900 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <Mail className="w-8 h-8 text-primary-400 mx-auto mb-4" />
          <h2 className="text-3xl font-bold mb-3">Stay in the Loop</h2>
          <p className="text-gray-400 mb-6 max-w-md mx-auto">Get notified about new releases, exclusive deals, and style guides.</p>
          <form className="flex max-w-md mx-auto gap-2">
            <input type="email" placeholder="Enter your email" className="flex-1 px-4 py-3 rounded-lg bg-gray-800 border border-gray-700 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-primary-500" />
            <button type="submit" className="bg-primary-600 hover:bg-primary-700 text-white px-6 py-3 rounded-lg font-bold transition-colors">
              Subscribe
            </button>
          </form>
        </div>
      </section>

      <footer className="bg-gray-950 text-gray-400 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-primary-500" />
            <span className="text-sm font-bold text-white">E-Commerce</span>
          </div>
          <p className="text-sm">&copy; 2026 {brand_name}. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}
