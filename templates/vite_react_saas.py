from __future__ import annotations

import json
import re
from typing import Any

from webbuilder.models import JsonDict

SCENE: dict[str, dict[str, Any]] = {
    "ecommerce": {
        "keywords": ["e-commerce", "ecommerce", "shop", "store", "product", "cart", "sneaker", "fashion", "clothing", "shoe", "watch", "jewelry"],
        "sample_data": [
            {"id": 1, "name": "Air Max Pulse", "price": 159.99, "category": "Running", "rating": 4.8, "reviews": 234, "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=400&fit=crop", "badge": "New"},
            {"id": 2, "name": "Classic Leather", "price": 189.99, "category": "Lifestyle", "rating": 4.6, "reviews": 189, "image": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400&h=400&fit=crop", "badge": ""},
            {"id": 3, "name": "Court Vision", "price": 89.99, "category": "Basketball", "rating": 4.4, "reviews": 567, "image": "https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?w=400&h=400&fit=crop", "badge": "Sale"},
            {"id": 4, "name": "Urban Runner", "price": 134.99, "category": "Running", "rating": 4.7, "reviews": 312, "image": "https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=400&h=400&fit=crop", "badge": ""},
            {"id": 5, "name": "Heritage Boot", "price": 219.99, "category": "Lifestyle", "rating": 4.9, "reviews": 156, "image": "https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?w=400&h=400&fit=crop", "badge": "Popular"},
            {"id": 6, "name": "Trail Runner", "price": 149.99, "category": "Running", "rating": 4.5, "reviews": 203, "image": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=400&h=400&fit=crop", "badge": ""},
        ],
    },
    "travel": {
        "keywords": ["travel", "booking", "hotel", "destination", "flight", "vacation", "resort", "trip", "itinerary", "airbnb", "airline", "cruise", "europe"],
        "sample_data": [
            {"id": 1, "name": "Paris, France", "price": 899, "rating": 4.9, "reviews": 1243, "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&h=400&fit=crop", "tag": "Romantic", "duration": "5 days"},
            {"id": 2, "name": "Rome, Italy", "price": 799, "rating": 4.8, "reviews": 987, "image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=600&h=400&fit=crop", "tag": "Historic", "duration": "4 days"},
            {"id": 3, "name": "Barcelona, Spain", "price": 699, "rating": 4.7, "reviews": 856, "image": "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=600&h=400&fit=crop", "tag": "Beach", "duration": "6 days"},
            {"id": 4, "name": "Amsterdam, Netherlands", "price": 749, "rating": 4.6, "reviews": 654, "image": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=600&h=400&fit=crop", "tag": "Culture", "duration": "3 days"},
            {"id": 5, "name": "Santorini, Greece", "price": 1099, "rating": 4.9, "reviews": 432, "image": "https://images.unsplash.com/photo-1613395877344-13d4a8e0d49e?w=600&h=400&fit=crop", "tag": "Luxury", "duration": "7 days"},
            {"id": 6, "name": "Prague, Czech Republic", "price": 599, "rating": 4.5, "reviews": 789, "image": "https://images.unsplash.com/photo-1541849546-216549ae216d?w=600&h=400&fit=crop", "tag": "Budget", "duration": "4 days"},
        ],
    },
    "portfolio": {
        "keywords": ["portfolio", "photographer", "gallery", "creative", "designer", "artist", "studio", "agency"],
        "sample_data": [
            {"id": 1, "title": "Brand Identity", "category": "Branding", "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=600&h=400&fit=crop"},
            {"id": 2, "title": "App Design", "category": "UI/UX", "image": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&h=400&fit=crop"},
            {"id": 3, "title": "E-Commerce Site", "category": "Web", "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&h=400&fit=crop"},
            {"id": 4, "title": "Landscape Series", "category": "Photography", "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop"},
            {"id": 5, "title": "Packaging Line", "category": "Branding", "image": "https://images.unsplash.com/photo-1586717799252-bd134755fbaf?w=600&h=400&fit=crop"},
            {"id": 6, "title": "Dashboard UI", "category": "UI/UX", "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=400&fit=crop"},
        ],
    },
    "blog": {
        "keywords": ["blog", "news", "article", "magazine", "publication", "editorial", "post"],
        "sample_data": [
            {"id": 1, "title": "Getting Started with React 19", "excerpt": "A deep dive into the new features in React 19.", "date": "Sep 10, 2026", "readTime": "8 min", "tag": "React", "image": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=600&h=300&fit=crop"},
            {"id": 2, "title": "Modern CSS Techniques", "excerpt": "Explore container queries, cascade layers, and more.", "date": "Sep 8, 2026", "readTime": "6 min", "tag": "CSS", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&h=300&fit=crop"},
            {"id": 3, "title": "Building Design Systems", "excerpt": "Step-by-step guide to scalable design systems.", "date": "Sep 5, 2026", "readTime": "12 min", "tag": "Design", "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=600&h=300&fit=crop"},
            {"id": 4, "title": "TypeScript Best Practices", "excerpt": "Level up with advanced TypeScript patterns.", "date": "Sep 3, 2026", "readTime": "10 min", "tag": "TypeScript", "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=300&fit=crop"},
            {"id": 5, "title": "Web Performance Guide", "excerpt": "Optimize your web apps for speed.", "date": "Sep 1, 2026", "readTime": "7 min", "tag": "Performance", "image": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=600&h=300&fit=crop"},
            {"id": 6, "title": "Figma to Code", "excerpt": "Streamline your design-to-dev pipeline.", "date": "Aug 28, 2026", "readTime": "9 min", "tag": "Workflow", "image": "https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=600&h=300&fit=crop"},
        ],
    },
    "restaurant": {
        "keywords": ["restaurant", "cafe", "food", "menu", "dining", "bakery", "pizza", "sushi", "coffee"],
        "sample_data": [
            {"id": 1, "name": "Truffle Risotto", "price": 28, "category": "Mains", "image": "https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400&h=300&fit=crop"},
            {"id": 2, "name": "Grilled Salmon", "price": 32, "category": "Mains", "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop"},
            {"id": 3, "name": "Caesar Salad", "price": 14, "category": "Starters", "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop"},
            {"id": 4, "name": "Tiramisu", "price": 12, "category": "Desserts", "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400&h=300&fit=crop"},
            {"id": 5, "name": "Espresso", "price": 5, "category": "Drinks", "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=400&h=300&fit=crop"},
            {"id": 6, "name": "Margherita Pizza", "price": 18, "category": "Mains", "image": "https://images.unsplash.com/photo-1604382355076-af4b0eb60143?w=400&h=300&fit=crop"},
        ],
    },
}

SCENE_ORDER = ["ecommerce", "travel", "portfolio", "blog", "restaurant"]


def detect_scene(user_prompt: str) -> str:
    lower = user_prompt.lower()
    for scene_key in SCENE_ORDER:
        for kw in SCENE[scene_key]["keywords"]:
            if kw in lower:
                return scene_key
    return "saas"


def render(requirements: JsonDict, plan: JsonDict) -> dict[str, str]:
    user_prompt = str(requirements.get("user_prompt", ""))
    website_type = str(requirements.get("website_type", "website")).replace("_", " ").title()
    features = requirements.get("features", [])
    sections = plan.get("sections", ["hero", "features", "contact"])
    primary = str(plan.get("primary_color", "blue"))
    theme = requirements.get("theme", "modern")
    style_notes = requirements.get("style_notes", "")

    scene = detect_scene(user_prompt)
    data = SCENE[scene]["sample_data"]

    color_map = {
        "blue": ("#2563eb", "#1d4ed8", "#eff6ff", "#dbeafe"),
        "purple": ("#9333ea", "#7e22ce", "#faf5ff", "#f3e8ff"),
        "green": ("#16a34a", "#15803d", "#f0fdf4", "#dcfce7"),
        "red": ("#dc2626", "#b91c1c", "#fef2f2", "#fee2e2"),
        "orange": ("#ea580c", "#c2410c", "#fff7ed", "#ffedd5"),
        "teal": ("#0d9488", "#0f766e", "#f0fdfa", "#ccfbf1"),
    }
    c = color_map.get(primary, color_map["blue"])

    if scene == "ecommerce":
        app_tsx = _ecommerce(website_type, features, sections, data, c, style_notes or user_prompt)
    elif scene == "travel":
        app_tsx = _travel(website_type, features, sections, data, c, style_notes or user_prompt)
    elif scene == "portfolio":
        app_tsx = _portfolio(website_type, features, sections, data, c, style_notes or user_prompt)
    elif scene == "blog":
        app_tsx = _blog(website_type, features, sections, data, c, style_notes or user_prompt)
    elif scene == "restaurant":
        app_tsx = _restaurant(website_type, features, sections, data, c, style_notes or user_prompt)
    else:
        app_tsx = _saas(website_type, features, sections, data, c, style_notes or user_prompt)

    return {
        "package.json": json.dumps({
            "name": "generated-app", "private": True, "type": "module",
            "scripts": {"dev": "vite --host 0.0.0.0", "build": "vite build", "preview": "vite preview"},
            "dependencies": {"@vitejs/plugin-react": "latest", "vite": "latest", "typescript": "latest",
                             "react": "latest", "react-dom": "latest", "lucide-react": "latest"},
            "devDependencies": {"tailwindcss": "latest", "@tailwindcss/postcss": "latest",
                                "postcss": "latest", "autoprefixer": "latest"},
        }, indent=2),
        "index.html": f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/><title>{website_type}</title></head><body><div id="root"></div><script type="module" src="/src/main.tsx"></script></body></html>',
        "tsconfig.json": json.dumps({"compilerOptions": {"target": "ES2020", "useDefineForClassFields": True, "lib": ["DOM", "DOM.Iterable", "ES2020"], "skipLibCheck": True, "esModuleInterop": True, "allowSyntheticDefaultImports": True, "strict": True, "module": "ESNext", "moduleResolution": "Node", "resolveJsonModule": True, "isolatedModules": True, "noEmit": True, "jsx": "react-jsx"}, "include": ["src"]}, indent=2),
        "vite.config.ts": "import { defineConfig } from 'vite'\nimport react from '@vitejs/plugin-react'\nexport default defineConfig({ plugins: [react()] })\n",
        "tailwind.config.js": "/** @type {import('tailwindcss').Config} */\nexport default {\n  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],\n  theme: { extend: {} },\n  plugins: [],\n}\n",
        "postcss.config.js": "export default {\n  plugins: {\n    '@tailwindcss/postcss': {},\n  },\n}\n",
        "src/main.tsx": "import React from 'react'\nimport ReactDOM from 'react-dom/client'\nimport App from './App'\nimport './styles.css'\nReactDOM.createRoot(document.getElementById('root')!).render(<React.StrictMode><App /></React.StrictMode>)\n",
        "src/styles.css": '@import "tailwindcss";\nbody { margin: 0; }\n',
        "src/App.tsx": app_tsx,
    }


# ---------------------------------------------------------------------------
# Scene renderers
# ---------------------------------------------------------------------------

def _ecommerce(name, features, sections, data, c, desc):
    items = ",\n    ".join(
        json.dumps({"id": d["id"], "name": d["name"], "price": d["price"], "cat": d["category"],
                     "rating": d["rating"], "reviews": d["reviews"], "img": d["image"], "badge": d.get("badge", "")})
        for d in data
    )
    cats = sorted(set(d["category"] for d in data))
    return f'''import {{ useState, useMemo }} from "react";
import {{ Search, ShoppingCart, Heart, Star, Filter, X, Plus, Minus, Menu, ArrowRight, Mail, Sparkles, Eye }} from "lucide-react";

type P = {{ id:number; name:string; price:number; cat:string; rating:number; reviews:number; img:string; badge:string }};
type Cart = P & {{ qty:number }};

const CATS = ["All",{",".join(f'"{c}"' for c in cats)}];
const products: P[] = [{items}];

export default function App() {{
  const [cat,setCat]=useState("All");
  const [q,setQ]=useState("");
  const [sort,setSort]=useState("Featured");
  const [cart,setCart]=useState<Cart[]>([]);
  const [wish,setWish]=useState<number[]>([]);
  const [showCart,setShowCart]=useState(false);
  const [sel,setSel]=useState<P|null>(null);
  const [menu,setMenu]=useState(false);

  const filtered=useMemo(()=>{{
    let r=products.filter(p=>(cat==="All"||p.cat===cat)&&(p.name.toLowerCase().includes(q.toLowerCase())));
    if(sort==="Price: Low") r=[...r].sort((a,b)=>a.price-b.price);
    if(sort==="Price: High") r=[...r].sort((a,b)=>b.price-a.price);
    if(sort==="Rating") r=[...r].sort((a,b)=>b.rating-a.rating);
    return r;
  }},[cat,q,sort]);

  const total=cart.reduce((s,i)=>s+i.price*i.qty,0);
  const count=cart.reduce((s,i)=>s+i.qty,0);
  const add=(p:P)=>setCart(c=>{{ const x=c.find(i=>i.id===p.id); if(x) return c.map(i=>i.id===p.id?{{...i,qty:i.qty+1}}:i); return [...c,{{...p,qty:1}}]; }});
  const upd=(id:number,d:number)=>setCart(c=>c.map(i=>i.id===id?{{...i,qty:Math.max(0,i.qty+d)}}:i).filter(i=>i.qty>0));
  const togW=(id:number)=>setWish(w=>w.includes(id)?w.filter(i=>i!==id):[...w,id]);

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-sm sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2 font-bold text-xl"><Sparkles className="w-6 h-6" style={{{{"color":"{c[0]}"}}}} />{name}</div>
          <div className="hidden md:flex items-center gap-8">
            <a href="#shop" className="text-sm font-medium text-gray-600 hover:text-gray-900">Shop</a>
            <a href="#contact" className="text-sm font-medium text-gray-600 hover:text-gray-900">Contact</a>
          </div>
          <div className="flex items-center gap-3">
            <button onClick={{()=>setShowCart(true)}} className="relative p-2"><ShoppingCart className="w-5 h-5" />{{count>0&&<span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs w-5 h-5 rounded-full flex items-center justify-center">{{count}}</span>}}</button>
            <button onClick={{()=>setMenu(!menu)}} className="md:hidden p-2"><Menu className="w-5 h-5" /></button>
          </div>
        </div>
      </nav>

      <section className="bg-gradient-to-r from-gray-900 to-gray-800 text-white py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <span className="inline-block bg-white/10 text-xs font-bold px-3 py-1 rounded-full mb-4 uppercase tracking-wider">Premium Collection</span>
          <h1 className="text-4xl md:text-6xl font-extrabold leading-tight mb-6">Step Into Your<br/>New Style</h1>
          <p className="text-lg text-gray-300 mb-8 max-w-lg">{desc[:150] if desc else "Discover our curated collection of premium products."}</p>
          <a href="#shop" className="inline-flex items-center gap-2 bg-white text-gray-900 px-8 py-3 rounded-lg font-bold hover:bg-gray-100 transition">Shop Now <ArrowRight className="w-4 h-4" /></a>
        </div>
      </section>

      <section id="shop" className="max-w-7xl mx-auto px-4 py-12">
        <div className="flex flex-col lg:flex-row gap-8">
          <aside className="lg:w-64 shrink-0">
            <div className="bg-white rounded-xl p-6 shadow-sm sticky top-20 space-y-6">
              <div>
                <label className="text-sm font-medium text-gray-700 mb-2 block">Search</label>
                <div className="relative"><Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" /><input placeholder="Search..." value={{q}} onChange={{e=>setQ(e.target.value)}} className="w-full pl-10 pr-4 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none" /></div>
              </div>
              <div>
                <label className="text-sm font-medium text-gray-700 mb-2 block">Category</label>
                {{CATS.map(c=><button key={{c}} onClick={{()=>setCat(c)}} className={{`w-full text-left px-3 py-2 rounded-lg text-sm ${{cat===c?"bg-blue-50 text-blue-700 font-medium":"text-gray-600 hover:bg-gray-50"}}`}}>{{c}}</button>)}}
              </div>
              <div>
                <label className="text-sm font-medium text-gray-700 mb-2 block">Sort</label>
                <select value={{sort}} onChange={{e=>setSort(e.target.value)}} className="w-full px-3 py-2 border rounded-lg text-sm">
                  {{["Featured","Price: Low","Price: High","Rating"].map(s=><option key={{s}}>{{s}}</option>)}}
                </select>
              </div>
            </div>
          </aside>
          <main className="flex-1">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold">{{cat==="All"?"All Products":cat}} <span className="text-sm text-gray-500 font-normal">({{filtered.length}})</span></h2>
            </div>
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {{filtered.map(p=>(
                <div key={{p.id}} className="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition group">
                  <div className="relative aspect-square bg-gray-100">
                    <img src={{p.img}} alt={{p.name}} className="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
                    {{p.badge&&<span className="absolute top-3 left-3 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">{{p.badge}}</span>}}
                    <button onClick={{()=>togW(p.id)}} className="absolute top-3 right-3 w-8 h-8 bg-white rounded-full flex items-center justify-center shadow-sm"><Heart className={{`w-4 h-4 ${{wish.includes(p.id)?"fill-red-500 text-red-500":"text-gray-400"}}`}} /></button>
                  </div>
                  <div className="p-4">
                    <p className="text-xs text-gray-500">{{p.cat}}</p>
                    <h3 className="font-bold">{{p.name}}</h3>
                    <div className="flex items-center gap-1 mb-2">{{[1,2,3,4,5].map(s=><Star key={{s}} className={{`w-3.5 h-3.5 ${{s<=Math.round(p.rating)?"fill-yellow-400 text-yellow-400":"text-gray-200"}}`}} />)}}<span className="text-xs text-gray-500 ml-1">({{p.reviews}})</span></div>
                    <div className="flex items-center justify-between">
                      <span className="text-lg font-bold">${{p.price.toFixed(2)}}</span>
                      <button onClick={{()=>add(p)}} className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-medium transition">Add to Cart</button>
                    </div>
                  </div>
                </div>
              ))}}
            </div>
          </main>
        </div>
      </section>

      {{sel&&<div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4" onClick={{()=>setSel(null)}}><div className="bg-white rounded-2xl max-w-lg w-full p-6" onClick={{e=>e.stopPropagation()}}><h2 className="text-xl font-bold mb-2">{{sel.name}}</h2><p className="text-gray-600 mb-4">${{sel.price.toFixed(2)}}</p><button onClick={{()=>{{add(sel);setSel(null);}}}} className="bg-blue-600 text-white px-6 py-2 rounded-lg">Add to Cart</button></div></div>}}

      {{showCart&&<div className="fixed inset-0 z-50 flex justify-end bg-black/50" onClick={{()=>setShowCart(false)}}><div className="bg-white w-full max-w-md h-full overflow-y-auto shadow-2xl" onClick={{e=>e.stopPropagation()}}><div className="p-6"><div className="flex items-center justify-between mb-6"><h2 className="text-xl font-bold">Cart ({{count}})</h2><button onClick={{()=>setShowCart(false)}}><X className="w-5 h-5" /></button></div>{{cart.length===0?<p className="text-gray-500 text-center py-12">Empty cart</p>:<>
              {{cart.map(i=>(<div key={{i.id}} className="flex gap-4 p-4 bg-gray-50 rounded-xl mb-3"><img src={{i.img}} className="w-16 h-16 rounded object-cover" /><div className="flex-1"><h4 className="font-medium text-sm">{{i.name}}</h4><p className="text-sm font-bold">${{(i.price*i.qty).toFixed(2)}}</p><div className="flex items-center gap-2 mt-1"><button onClick={{()=>upd(i.id,-1)}} className="w-6 h-6 bg-gray-200 rounded flex items-center justify-center"><Minus className="w-3 h-3" /></button><span className="text-sm w-6 text-center">{{i.qty}}</span><button onClick={{()=>upd(i.id,1)}} className="w-6 h-6 bg-gray-200 rounded flex items-center justify-center"><Plus className="w-3 h-3" /></button></div></div></div>))}}
              <div className="border-t pt-4 mt-4"><div className="flex justify-between text-lg font-bold"><span>Total</span><span>${{total.toFixed(2)}}</span></div><button className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg font-bold mt-4 transition">Checkout</button></div>
            </>}}</div></div></div>}}

      <section id="contact" className="bg-gray-900 text-white py-16 px-4"><div className="max-w-3xl mx-auto text-center"><Mail className="w-8 h-8 mx-auto mb-4" /><h2 className="text-3xl font-bold mb-3">Stay in the Loop</h2><p className="text-gray-400 mb-6">Get notified about new releases and deals.</p><form className="flex max-w-md mx-auto gap-2"><input type="email" placeholder="Email" className="flex-1 px-4 py-3 rounded-lg bg-gray-800 border border-gray-700 text-white placeholder-gray-500 focus:ring-2 focus:ring-blue-500 focus:outline-none" /><button className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-bold transition">Subscribe</button></form></div></section>

      <footer className="bg-gray-950 text-gray-400 py-8 px-4"><div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4 text-sm"><div className="flex items-center gap-2"><Sparkles className="w-4 h-4" /><span className="font-bold text-white">{name}</span></div><p>&copy; 2026 {name}. All rights reserved.</p></div></footer>
    </div>
  );
}}'''


def _travel(name, features, sections, data, c, desc):
    items = ",\n    ".join(
        json.dumps({"id": d["id"], "name": d["name"], "price": d["price"], "rating": d["rating"],
                     "reviews": d["reviews"], "img": d["image"], "tag": d.get("tag", ""), "dur": d.get("duration", "")})
        for d in data
    )
    tags = sorted(set(d.get("tag", "") for d in data if d.get("tag")))
    return f'''import {{ useState, useMemo }} from "react";
import {{ Search, MapPin, Star, Calendar, Clock, Filter, X, Heart, ArrowRight, Mail, Sparkles, Plane, Menu }} from "lucide-react";

type Trip = {{ id:number; name:string; price:number; rating:number; reviews:number; img:string; tag:string; dur:string }};

const TAGS = ["All",{",".join(f'"{t}"' for t in tags)}];
const trips: Trip[] = [{items}];

export default function App() {{
  const [tag,setTag]=useState("All");
  const [q,setQ]=useState("");
  const [sort,setSort]=useState("Featured");
  const [wish,setWish]=useState<number[]>([]);
  const [sel,setSel]=useState<Trip|null>(null);
  const [menu,setMenu]=useState(false);

  const filtered=useMemo(()=>{{
    let r=trips.filter(t=>(tag==="All"||t.tag===tag)&&(t.name.toLowerCase().includes(q.toLowerCase())));
    if(sort==="Price: Low") r=[...r].sort((a,b)=>a.price-b.price);
    if(sort==="Price: High") r=[...r].sort((a,b)=>b.price-a.price);
    if(sort==="Rating") r=[...r].sort((a,b)=>b.rating-a.rating);
    return r;
  }},[tag,q,sort]);

  const togW=(id:number)=>setWish(w=>w.includes(id)?w.filter(i=>i!==id):[...w,id]);

  return (
    <div className="min-h-screen bg-white">
      <nav className="bg-white shadow-sm sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2 font-bold text-xl"><Plane className="w-6 h-6" style={{{{"color":"{c[0]}"}}}} />{name}</div>
          <div className="hidden md:flex items-center gap-8">
            <a href="#destinations" className="text-sm font-medium text-gray-600 hover:text-gray-900">Destinations</a>
            <a href="#itinerary" className="text-sm font-medium text-gray-600 hover:text-gray-900">Itinerary</a>
            <a href="#hotels" className="text-sm font-medium text-gray-600 hover:text-gray-900">Hotels</a>
            <a href="#contact" className="text-sm font-medium text-gray-600 hover:text-gray-900">Contact</a>
          </div>
          <button onClick={{()=>setMenu(!menu)}} className="md:hidden p-2"><Menu className="w-5 h-5" /></button>
        </div>
      </nav>

      <section className="relative h-[60vh] min-h-[400px] bg-cover bg-center flex items-end" style={{{{"backgroundImage":"url('https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1600&h=900&fit=crop')"}}}}>
        <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent" />
        <div className="relative max-w-7xl mx-auto px-4 py-16 w-full text-white">
          <span className="inline-block bg-white/20 text-xs font-bold px-3 py-1 rounded-full mb-4 uppercase tracking-wider backdrop-blur-sm">Explore the World</span>
          <h1 className="text-4xl md:text-6xl font-extrabold leading-tight mb-4">Discover Your Next<br/>Adventure</h1>
          <p className="text-lg text-gray-200 mb-8 max-w-lg">{desc[:200] if desc else "Find amazing travel destinations across Europe and beyond."}</p>
          <a href="#destinations" className="inline-flex items-center gap-2 bg-white text-gray-900 px-8 py-3 rounded-lg font-bold hover:bg-gray-100 transition">Explore Now <ArrowRight className="w-4 h-4" /></a>
        </div>
      </section>

      <section id="destinations" className="max-w-7xl mx-auto px-4 py-16">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 mb-8">
          <div><h2 className="text-3xl font-bold">Popular Destinations</h2><p className="text-gray-500 mt-1">{{filtered.length}} amazing places to visit</p></div>
          <div className="flex items-center gap-3 flex-wrap">
            <div className="relative"><Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" /><input placeholder="Search destinations..." value={{q}} onChange={{e=>setQ(e.target.value)}} className="pl-10 pr-4 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none w-64" /></div>
            <select value={{sort}} onChange={{e=>setSort(e.target.value)}} className="px-3 py-2 border rounded-lg text-sm"><option>Featured</option><option>Price: Low</option><option>Price: High</option><option>Rating</option></select>
          </div>
        </div>
        <div className="flex gap-2 flex-wrap mb-8">{{TAGS.map(t=><button key={{t}} onClick={{()=>setTag(t)}} className={{`px-4 py-2 rounded-full text-sm font-medium transition ${{tag===t?"bg-blue-600 text-white":"bg-gray-100 text-gray-600 hover:bg-gray-200"}}`}}>{{t}}</button>)}}</div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {{filtered.map(t=>(
            <div key={{t.id}} className="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition group cursor-pointer" onClick={{()=>setSel(t)}}>
              <div className="relative aspect-[4/3] overflow-hidden">
                <img src={{t.img}} alt={{t.name}} className="w-full h-full object-cover group-hover:scale-105 transition duration-500" />
                <span className="absolute top-3 left-3 bg-white/90 backdrop-blur-sm text-xs font-bold px-2 py-1 rounded-full">{{t.tag}}</span>
                <button onClick={{e=>{{e.stopPropagation();togW(t.id);}}}} className="absolute top-3 right-3 w-8 h-8 bg-white/90 rounded-full flex items-center justify-center"><Heart className={{`w-4 h-4 ${{wish.includes(t.id)?"fill-red-500 text-red-500":"text-gray-400"}}`}} /></button>
              </div>
              <div className="p-5">
                <div className="flex items-center gap-1 mb-1"><MapPin className="w-4 h-4 text-blue-600" /><span className="text-sm text-gray-500">{{t.name}}</span></div>
                <div className="flex items-center gap-2 mb-3">
                  <div className="flex">{{[1,2,3,4,5].map(s=><Star key={{s}} className={{`w-4 h-4 ${{s<=Math.round(t.rating)?"fill-yellow-400 text-yellow-400":"text-gray-200"}}`}} />)}}</div>
                  <span className="text-sm text-gray-500">{{t.rating}} ({{t.reviews}})</span>
                </div>
                <div className="flex items-center gap-4 text-sm text-gray-500 mb-3"><span className="flex items-center gap-1"><Clock className="w-4 h-4" />{{t.dur}}</span></div>
                <div className="flex items-center justify-between"><span className="text-2xl font-bold">${{t.price}}</span><span className="text-sm text-gray-500">/person</span></div>
              </div>
            </div>
          ))}}
        </div>
      </section>

      {{sel&&<div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4" onClick={{()=>setSel(null)}}><div className="bg-white rounded-2xl max-w-lg w-full overflow-hidden" onClick={{e=>e.stopPropagation()}}>
        <img src={{sel.img}} className="w-full h-48 object-cover" />
        <div className="p-6"><div className="flex items-center gap-2 mb-2"><MapPin className="w-5 h-5 text-blue-600" /><h2 className="text-2xl font-bold">{{sel.name}}</h2></div>
          <div className="flex items-center gap-4 mb-4 text-sm text-gray-500"><span className="flex items-center gap-1"><Clock className="w-4 h-4" />{{sel.dur}}</span><span className="flex items-center gap-1"><Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />{{sel.rating}}</span><span>{{sel.reviews}} reviews</span></div>
          <p className="text-gray-600 mb-6">An amazing {{sel.tag.toLowerCase()}} destination perfect for your next vacation. Experience the best of {{sel.name}} with our curated travel packages.</p>
          <div className="flex items-center justify-between"><span className="text-3xl font-bold">${{sel.price}}<span className="text-sm font-normal text-gray-500">/person</span></span>
            <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-bold transition">Book Now</button></div></div></div></div>}}

      <section id="itinerary" className="bg-gray-50 py-16 px-4">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">Sample Itinerary</h2>
          <div className="space-y-8">
            {{["Day 1: Arrival & City Tour - Explore the historic center, local cafes, and iconic landmarks",
               "Day 2: Cultural Immersion - Visit museums, galleries, and experience local traditions",
               "Day 3: Adventure Day - Outdoor activities, nature walks, and scenic viewpoints",
               "Day 4: Free Day - Shopping, relaxation, or optional excursions",
               "Day 5: Departure - Final morning exploration and departure"].map((item,i)=>(
              <div key={{i}} className="flex gap-4 items-start">
                <div className="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold shrink-0">{{i+1}}</div>
                <div className="bg-white rounded-xl p-5 shadow-sm flex-1"><p className="text-gray-700">{{item}}</p></div>
              </div>
            ))}}
          </div>
        </div>
      </section>

      <section id="hotels" className="py-16 px-4">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-4">Recommended Hotels</h2>
          <p className="text-gray-500 text-center mb-12">Hand-picked accommodations for every budget</p>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {{[
              {{name:"Grand Palace Hotel",stars:5,price:"$280/night",area:"City Center",img:"https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400&h=300&fit=crop"}},
              {{name:"Boutique Stay",stars:4,price:"$150/night",area:"Old Town",img:"https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=400&h=300&fit=crop"}},
              {{name:"Cozy Hostel",stars:3,price:"$45/night",area:"Near Station",img:"https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=400&h=300&fit=crop"}},
            ].map((h,i)=>(
              <div key={{i}} className="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition">
                <img src={{h.img}} alt={{h.name}} className="w-full h-48 object-cover" />
                <div className="p-5">
                  <div className="flex items-center gap-1 mb-1">{{[1,2,3,4,5].map(s=><Star key={{s}} className={{`w-4 h-4 ${{s<=h.stars?"fill-yellow-400 text-yellow-400":"text-gray-200"}}`}} />)}}</div>
                  <h3 className="font-bold text-lg">{{h.name}}</h3>
                  <p className="text-sm text-gray-500 mb-3">{{h.area}}</p>
                  <div className="flex items-center justify-between"><span className="text-xl font-bold">{{h.price}}</span><button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-medium transition">Book</button></div>
                </div>
              </div>
            ))}}
          </div>
        </div>
      </section>

      <section id="contact" className="bg-gray-900 text-white py-16 px-4"><div className="max-w-3xl mx-auto text-center"><Mail className="w-8 h-8 mx-auto mb-4" /><h2 className="text-3xl font-bold mb-3">Plan Your Trip</h2><p className="text-gray-400 mb-6">Get personalized travel recommendations.</p><form className="flex max-w-md mx-auto gap-2"><input type="email" placeholder="Your email" className="flex-1 px-4 py-3 rounded-lg bg-gray-800 border border-gray-700 text-white placeholder-gray-500 focus:ring-2 focus:ring-blue-500 focus:outline-none" /><button className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-bold transition">Send</button></form></div></section>
      <footer className="bg-gray-950 text-gray-400 py-8 px-4 text-center text-sm">&copy; 2026 {name}. All rights reserved.</footer>
    </div>
  );
}}'''


def _portfolio(name, features, sections, data, c, desc):
    items_json = json.dumps(data)
    cats = sorted(set(d.get("category", "") for d in data))
    return f'''import {{ useState }} from "react";
import {{ Menu, X, Mail, ArrowRight, Sparkles }} from "lucide-react";

const projects = {items_json};
const cats = ["All",{",".join(f'"{cat}"' for cat in cats)}];
const services = [{{icon:"🎨",title:"Brand Identity",desc:"Logos and visual systems"}},{{icon:"💻",title:"Web Design",desc:"Responsive websites"}},{{icon:"📱",title:"UI/UX Design",desc:"Mobile apps and products"}},{{icon:"📸",title:"Photography",desc:"Product and lifestyle shoots"}}];

export default function App() {{
  const [filter,setFilter]=useState("All");
  const [menu,setMenu]=useState(false);
  const filtered=filter==="All"?projects:projects.filter(p=>p.category===filter);

  return (
    <div className="min-h-screen bg-white">
      <nav className="fixed top-0 w-full bg-white/80 backdrop-blur-md z-40 border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <a href="#" className="flex items-center gap-2 font-bold text-lg"><Sparkles className="w-5 h-5" style={{{{"color":"{c[0]}"}}}} />{name}</a>
          <div className="hidden md:flex items-center gap-8">{{["Work","Services","About","Contact"].map(l=><a key={{l}} href={{`#${{l.toLowerCase()}}`}} className="text-sm text-gray-600 hover:text-gray-900">{{l}}</a>)}}</div>
          <button onClick={{()=>setMenu(!menu)}} className="md:hidden">{{menu?<X className="w-5 h-5"/>:<Menu className="w-5 h-5"/>}}</button>
        </div>
        {{menu&&<div className="md:hidden border-t bg-white px-6 py-4 space-y-3">{{["Work","Services","About","Contact"].map(l=><a key={{l}} href="#" className="block text-sm text-gray-600">{{l}}</a>)}}</div>}}
      </nav>

      <section className="pt-32 pb-20 px-6"><div className="max-w-7xl mx-auto">
        <span className="text-xs font-bold uppercase tracking-widest" style={{{{"color":"{c[0]}"}}}}>Creative Portfolio</span>
        <h1 className="mt-4 text-5xl md:text-7xl font-extrabold leading-tight max-w-4xl">Designing digital experiences that matter.</h1>
        <p className="mt-6 text-lg text-gray-500 max-w-xl">{desc[:200] if desc else "We craft brands, build products, and create visual stories."}</p>
        <a href="#work" className="mt-8 inline-flex items-center gap-2 bg-gray-900 text-white px-6 py-3 rounded-lg font-bold hover:bg-gray-800 transition">View Work <ArrowRight className="w-4 h-4" /></a>
      </div></section>

      <section id="work" className="py-20 px-6 bg-gray-50"><div className="max-w-7xl mx-auto">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-10">
          <div><h2 className="text-3xl font-bold">Selected Work</h2><p className="text-gray-500">A curated collection of recent projects.</p></div>
          <div className="flex gap-2 flex-wrap">{{cats.map(ct=><button key={{ct}} onClick={{()=>setFilter(ct)}} className={{`px-4 py-2 rounded-full text-sm font-medium transition ${{filter===ct?"bg-gray-900 text-white":"bg-white text-gray-600 hover:bg-gray-100 border border-gray-200"}}`}}>{{ct}}</button>)}}</div>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">{{filtered.map(p=>(
          <div key={{p.id}} className="group bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition">
            <div className="aspect-[4/3] overflow-hidden"><img src={{p.image}} alt={{p.title}} className="w-full h-full object-cover group-hover:scale-105 transition duration-500" /></div>
            <div className="p-5"><p className="text-xs font-medium mb-1" style={{{{"color":"{c[0]}"}}}}>{{p.category}}</p><h3 className="font-bold">{{p.title}}</h3></div>
          </div>
        ))}}</div>
      </div></section>

      <section id="services" className="py-20 px-6"><div className="max-w-7xl mx-auto">
        <h2 className="text-3xl font-bold mb-10">Services</h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">{{services.map(s=><div key={{s.title}} className="p-6 border border-gray-200 rounded-xl hover:shadow-lg transition"><span className="text-3xl mb-4 block">{{s.icon}}</span><h3 className="font-bold mb-1">{{s.title}}</h3><p className="text-sm text-gray-500">{{s.desc}}</p></div>)}}</div>
      </div></section>

      <section id="contact" className="py-20 px-6 bg-gray-900 text-white"><div className="max-w-3xl mx-auto text-center">
        <Mail className="w-8 h-8 mx-auto mb-4" /><h2 className="text-3xl font-bold mb-3">Let's Work Together</h2><p className="text-gray-400 mb-8">Have a project in mind?</p>
        <a href="mailto:hello@example.com" className="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-bold transition">Get in Touch <ArrowRight className="w-4 h-4" /></a>
      </div></section>
      <footer className="py-6 px-6 border-t text-center text-sm text-gray-500">&copy; 2026 {name}. All rights reserved.</footer>
    </div>
  );
}}'''


def _blog(name, features, sections, data, c, desc):
    items_json = json.dumps(data)
    tags = sorted(set(d.get("tag", "") for d in data))
    return f'''import {{ useState }} from "react";
import {{ Clock, Search, ArrowRight, Mail, Sparkles, Menu, X }} from "lucide-react";

const posts = {items_json};
const tags = ["All",{",".join(f'"{t}"' for t in tags)}];

export default function App() {{
  const [tag,setTag]=useState("All");
  const [search,setSearch]=useState("");
  const [menu,setMenu]=useState(false);
  const filtered=posts.filter(p=>(tag==="All"||p.tag===tag)&&p.title.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="min-h-screen bg-white">
      <nav className="border-b bg-white sticky top-0 z-40">
        <div className="max-w-5xl mx-auto px-6 h-16 flex items-center justify-between">
          <a href="#" className="flex items-center gap-2 font-bold text-lg"><Sparkles className="w-5 h-5" style={{{{"color":"{c[0]}"}}}} />{name}</a>
          <div className="hidden md:flex items-center gap-6">{{["Articles","Topics","About","Newsletter"].map(l=><a key={{l}} href="#" className="text-sm text-gray-600 hover:text-gray-900">{{l}}</a>)}}</div>
          <button onClick={{()=>setMenu(!menu)}} className="md:hidden">{{menu?<X className="w-5 h-5"/>:<Menu className="w-5 h-5"/>}}</button>
        </div>
      </nav>

      <header className="py-16 px-6 bg-gray-50"><div className="max-w-5xl mx-auto">
        <h1 className="text-4xl md:text-5xl font-extrabold mb-4">Latest Articles</h1>
        <p className="text-gray-500 text-lg max-w-xl mb-8">{desc[:150] if desc else "Insights on web development, design, and technology."}</p>
        <div className="relative max-w-md"><Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" /><input placeholder="Search articles..." value={{search}} onChange={{e=>setSearch(e.target.value)}} className="w-full pl-11 pr-4 py-3 bg-white border rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none" /></div>
      </div></header>

      <main className="max-w-5xl mx-auto px-6 py-12">
        <div className="flex gap-2 flex-wrap mb-8">{{tags.map(t=><button key={{t}} onClick={{()=>setTag(t)}} className={{`px-4 py-2 rounded-full text-sm font-medium transition ${{tag===t?"bg-gray-900 text-white":"bg-gray-100 text-gray-600 hover:bg-gray-200"}}`}}>{{t}}</button>)}}</div>
        <div className="space-y-6">{{filtered.map((p,i)=>(
          <article key={{p.id}} className="flex flex-col md:flex-row gap-6 p-6 bg-gray-50 rounded-xl hover:shadow-md transition">
            <img src={{p.image}} alt={{p.title}} className={{`w-full md:w-64 object-cover rounded-lg ${{i===0?"md:w-96":"h-48"}}`}} />
            <div className="flex-1">
              <div className="flex items-center gap-3 mb-2"><span className="text-xs font-medium px-2 py-1 rounded" style={{{{"color":"{c[0]}","backgroundColor":"{c[2]}"}}}}>{{p.tag}}</span><span className="text-xs text-gray-400 flex items-center gap-1"><Clock className="w-3 h-3" />{{p.readTime}}</span></div>
              <h2 className={{`font-bold mb-2 hover:text-blue-600 cursor-pointer ${{i===0?"text-2xl":"text-lg"}}`}}>{{p.title}}</h2>
              <p className="text-sm text-gray-500 mb-3">{{p.excerpt}}</p>
              <div className="flex items-center justify-between"><span className="text-xs text-gray-400">{{p.date}}</span><a href="#" className="text-sm font-medium text-blue-600 flex items-center gap-1">Read More <ArrowRight className="w-3 h-3" /></a></div>
            </div>
          </article>
        ))}}</div>
      </main>

      <section className="bg-gray-900 text-white py-16 px-6"><div className="max-w-3xl mx-auto text-center">
        <Mail className="w-8 h-8 mx-auto mb-4" /><h2 className="text-3xl font-bold mb-3">Subscribe</h2><p className="text-gray-400 mb-6">Get articles delivered weekly.</p>
        <form className="flex max-w-md mx-auto gap-2"><input type="email" placeholder="your@email.com" className="flex-1 px-4 py-3 rounded-lg bg-gray-800 border border-gray-700 text-white placeholder-gray-500 focus:ring-2 focus:ring-blue-500 focus:outline-none" /><button className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-bold transition">Subscribe</button></form>
      </div></section>
      <footer className="py-6 px-6 border-t text-center text-sm text-gray-500">&copy; 2026 {name}. All rights reserved.</footer>
    </div>
  );
}}'''


def _restaurant(name, features, sections, data, c, desc):
    items_json = json.dumps(data)
    cats = sorted(set(d.get("category", "") for d in data))
    return f'''import {{ useState, useMemo }} from "react";
import {{ Search, Star, Clock, ArrowRight, Mail, Sparkles, Menu, X, ShoppingCart, Phone, MapPin }} from "lucide-react";

type Item = {{ id:number; name:string; price:number; category:string; image:string }};

const CATS = ["All",{",".join(f'"{ct}"' for ct in cats)}];
const menuItems: Item[] = {items_json};

export default function App() {{
  const [cat,setCat]=useState("All");
  const [q,setQ]=useState("");
  const [cart,setCart]=useState<(Item&{{qty:number}})[]>([]);
  const [menu,setMenu]=useState(false);

  const filtered=useMemo(()=>menuItems.filter(i=>(cat==="All"||i.category===cat)&&(i.name.toLowerCase().includes(q.toLowerCase()))),[cat,q]);
  const total=cart.reduce((s,i)=>s+i.price*i.qty,0);
  const count=cart.reduce((s,i)=>s+i.qty,0);
  const add=(item:Item)=>setCart(c=>{{ const x=c.find(i=>i.id===item.id); if(x) return c.map(i=>i.id===item.id?{{...i,qty:i.qty+1}}:i); return [...c,{{...item,qty:1}}]; }});

  return (
    <div className="min-h-screen bg-white">
      <nav className="bg-white shadow-sm sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2 font-bold text-xl"><Sparkles className="w-6 h-6" style={{{{"color":"{c[0]}"}}}} />{name}</div>
          <div className="hidden md:flex items-center gap-8">
            <a href="#menu" className="text-sm font-medium text-gray-600 hover:text-gray-900">Menu</a>
            <a href="#about" className="text-sm font-medium text-gray-600 hover:text-gray-900">About</a>
            <a href="#contact" className="text-sm font-medium text-gray-600 hover:text-gray-900">Contact</a>
          </div>
          <div className="flex items-center gap-3">
            <button className="relative p-2"><ShoppingCart className="w-5 h-5" />{{count>0&&<span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs w-5 h-5 rounded-full flex items-center justify-center">{{count}}</span>}}</button>
            <button onClick={{()=>setMenu(!menu)}} className="md:hidden p-2"><Menu className="w-5 h-5" /></button>
          </div>
        </div>
      </nav>

      <section className="relative h-[50vh] min-h-[350px] bg-cover bg-center flex items-center" style={{{{"backgroundImage":"url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600&h=900&fit=crop')"}}}}>
        <div className="absolute inset-0 bg-black/50" />
        <div className="relative max-w-7xl mx-auto px-4 text-white">
          <span className="inline-block text-sm font-bold tracking-widest uppercase mb-4">Welcome to</span>
          <h1 className="text-5xl md:text-7xl font-extrabold mb-4">{name}</h1>
          <p className="text-lg text-gray-200 mb-8 max-w-lg">{desc[:150] if desc else "Experience exquisite cuisine crafted with passion and the finest ingredients."}</p>
          <div className="flex gap-4">
            <a href="#menu" className="inline-flex items-center gap-2 bg-white text-gray-900 px-6 py-3 rounded-lg font-bold hover:bg-gray-100 transition">View Menu <ArrowRight className="w-4 h-4" /></a>
            <a href="#contact" className="inline-flex items-center gap-2 border border-white/50 text-white px-6 py-3 rounded-lg font-bold hover:bg-white/10 transition">Reserve Table</a>
          </div>
        </div>
      </section>

      <section id="menu" className="max-w-7xl mx-auto px-4 py-16">
        <h2 className="text-3xl font-bold text-center mb-4">Our Menu</h2>
        <p className="text-gray-500 text-center mb-8">Crafted with love and the finest ingredients</p>
        <div className="flex justify-center gap-2 flex-wrap mb-8">{{CATS.map(c=><button key={{c}} onClick={{()=>setCat(c)}} className={{`px-4 py-2 rounded-full text-sm font-medium transition ${{cat===c?"text-white":"bg-gray-100 text-gray-600 hover:bg-gray-200"}}`}} style={{{{"backgroundColor": cat===c?"{c[0]}":"", "color": cat===c?"white":""}}}}>{{c}}</button>)}}</div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {{filtered.map(item=>(
            <div key={{item.id}} className="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition group">
              <div className="aspect-[4/3] overflow-hidden"><img src={{item.image}} alt={{item.name}} className="w-full h-full object-cover group-hover:scale-105 transition duration-300" /></div>
              <div className="p-5">
                <p className="text-xs text-gray-500 mb-1">{{item.category}}</p>
                <h3 className="font-bold text-lg mb-1">{{item.name}}</h3>
                <div className="flex items-center justify-between"><span className="text-2xl font-bold">${{item.price}}</span><button onClick={{()=>add(item)}} className="bg-gray-900 hover:bg-gray-800 text-white px-4 py-2 rounded-lg text-sm font-medium transition">Add to Order</button></div>
              </div>
            </div>
          ))}}
        </div>
      </section>

      <section id="about" className="bg-gray-50 py-16 px-4">
        <div className="max-w-5xl mx-auto grid md:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="text-3xl font-bold mb-4">Our Story</h2>
            <p className="text-gray-600 mb-4">Founded with a passion for exceptional dining, we source the finest local ingredients to create memorable culinary experiences.</p>
            <p className="text-gray-600 mb-6">Every dish tells a story, every visit creates a memory. Our chefs combine traditional techniques with modern innovation.</p>
            <div className="flex gap-8">
              <div><p className="text-3xl font-bold" style={{{{"color":"{c[0]}"}}}}>15+</p><p className="text-sm text-gray-500">Years Experience</p></div>
              <div><p className="text-3xl font-bold" style={{{{"color":"{c[0]}"}}}}>50+</p><p className="text-sm text-gray-500">Menu Items</p></div>
              <div><p className="text-3xl font-bold" style={{{{"color":"{c[0]}"}}}}>10k+</p><p className="text-sm text-gray-500">Happy Guests</p></div>
            </div>
          </div>
          <div className="rounded-xl overflow-hidden shadow-lg"><img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop" className="w-full h-80 object-cover" /></div>
        </div>
      </section>

      <section id="contact" className="py-16 px-4">
        <div className="max-w-5xl mx-auto grid md:grid-cols-2 gap-12">
          <div><h2 className="text-3xl font-bold mb-4">Visit Us</h2>
            <div className="space-y-4 text-gray-600">
              <p className="flex items-center gap-3"><MapPin className="w-5 h-5" />123 Gourmet Street, Foodville</p>
              <p className="flex items-center gap-3"><Phone className="w-5 h-5" />+1 (555) 123-4567</p>
              <p className="flex items-center gap-3"><Clock className="w-5 h-5" />Mon-Sun: 11am - 11pm</p>
            </div>
          </div>
          <div><h2 className="text-3xl font-bold mb-4">Reserve a Table</h2>
            <form className="space-y-4"><input placeholder="Your name" className="w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none" /><input type="email" placeholder="Email" className="w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none" /><input type="date" className="w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none" /><button type="button" className="w-full text-white py-3 rounded-lg font-bold transition hover:opacity-90" style={{{{"backgroundColor":"{c[0]}"}}}}>Reserve Now</button></form>
          </div>
        </div>
      </section>

      <footer className="bg-gray-900 text-gray-400 py-8 px-4 text-center text-sm">&copy; 2026 {name}. All rights reserved.</footer>
    </div>
  );
}}'''


def _saas(name, features, sections, data, c, desc):
    feature_cards = "\n".join(
        f'<div key={{{i}}} className="p-6 border border-gray-200 rounded-xl hover:shadow-lg transition"><h3 className="font-bold text-lg mb-2">{f}</h3><p className="text-gray-500 text-sm">Built for reliable performance and great user experience.</p></div>'
        for i, f in enumerate(features[:6])
    )
    return f'''import {{ ArrowRight, Check, Mail, Sparkles, Zap }} from "lucide-react";

const sections = {json.dumps(sections)};

export default function App() {{
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100">
      <nav className="flex items-center justify-between max-w-7xl mx-auto px-6 py-5">
        <div className="flex items-center gap-2 font-bold text-xl"><Sparkles className="w-5 h-5" style={{{{"color":"{c[0]}"}}}} />{name}</div>
        <div className="hidden md:flex items-center gap-8">{{sections.filter(s=>s!=="hero").map(s=><a key={{s}} href={{`#${{s}}`}} className="text-sm text-gray-500 hover:text-gray-900">{{s.replace(/_/g," ").replace(/\\b\\w/g,c=>c.toUpperCase())}}</a>)}}</div>
      </nav>

      <section className="max-w-7xl mx-auto px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
        <div>
          <span className="text-xs font-bold uppercase tracking-widest" style={{{{"color":"{c[0]}"}}}}>Premium Design</span>
          <h1 className="mt-4 text-5xl md:text-6xl font-bold leading-tight">Your {name} built with modern style.</h1>
          <p className="mt-6 text-lg text-gray-500">{desc[:200] if desc else f"A modern {name.lower()} crafted with care."}</p>
          <div className="mt-8 flex flex-wrap gap-4"><a href="#features" className="inline-flex items-center gap-2 text-white px-6 py-3 rounded-lg font-bold transition hover:opacity-90" style={{{{"backgroundColor":"{c[0]}"}}}}>Explore <ArrowRight className="w-4 h-4" /></a></div>
        </div>
        <div className="bg-gray-900 text-white rounded-xl p-6 shadow-2xl">
          <p className="text-xs font-mono text-gray-400 mb-4">// sections</p>
          {{sections.map((s,i)=>(<div key={{s}} className="flex items-center gap-4 py-3 border-b border-white/10 last:border-0"><span className="font-mono text-yellow-400 text-sm w-8">{{String(i+1).padStart(2,"0")}}</span><strong className="flex-1 text-sm capitalize">{{s.replace(/_/g," ")}}</strong><Check className="w-4 h-4 text-green-400" /></div>))}}
        </div>
      </section>

      <section id="features" className="max-w-7xl mx-auto px-6 py-20">
        <div className="mb-8"><span className="text-xs font-bold uppercase tracking-widest" style={{{{"color":"{c[0]}"}}}}>Features</span><h2 className="mt-2 text-3xl font-bold">What's included</h2></div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{feature_cards}</div>
      </section>

      <section id="contact" className="max-w-7xl mx-auto px-6 py-20 text-center">
        <Mail className="w-8 h-8 mx-auto mb-4" style={{{{"color":"{c[0]}"}}}} />
        <h2 className="text-3xl font-bold mb-3">Ready to get started?</h2>
        <p className="text-gray-500 mb-6">Build something great with {name}.</p>
        <a href="mailto:hello@example.com" className="inline-flex items-center gap-2 text-white px-6 py-3 rounded-lg font-bold transition hover:opacity-90" style={{{{"backgroundColor":"{c[0]}"}}}}>Get in touch</a>
      </section>
    </div>
  );
}}'''
