from __future__ import annotations

import json

from webbuilder.models import JsonDict


def render(requirements: JsonDict, plan: JsonDict) -> dict[str, str]:
    website_type = str(requirements.get("website_type", "Landing Page")).replace("_", " ").title()
    theme = str(requirements.get("theme", "modern"))
    components = requirements.get("components", ["Navbar", "Hero", "Features", "Contact", "Footer"])

    package_json = {
        "name": "generated-app",
        "version": "0.1.0",
        "private": True,
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview",
        },
        "dependencies": {
            "vue": "latest",
            "@vueuse/core": "latest",
        },
        "devDependencies": {
            "@vitejs/plugin-vue": "latest",
            "vite": "latest",
            "typescript": "latest",
            "tailwindcss": "latest",
            "postcss": "latest",
            "autoprefixer": "latest",
        },
    }

    vite_config = """import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
  },
})
"""

    tsconfig_json = {
        "compilerOptions": {
            "target": "ES2020",
            "useDefineForClassFields": True,
            "module": "ESNext",
            "lib": ["ES2020", "DOM", "DOM.Iterable"],
            "skipLibCheck": True,
            "moduleResolution": "bundler",
            "allowImportingTsExtensions": True,
            "resolveJsonModule": True,
            "isolatedModules": True,
            "noEmit": True,
            "jsx": "preserve",
            "strict": True,
            "noUnusedLocals": True,
            "noUnusedParameters": True,
            "noFallthroughCasesInSwitch": True,
        },
        "include": ["src/**/*.ts", "src/**/*.tsx", "src/**/*.vue"],
        "references": [{"path": "./tsconfig.node.json"}],
    }

    app_vue = f"""<script setup lang="ts">
import {{ ref }} from 'vue'

const sections = {json.dumps(components)}
const currentSection = ref('home')
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100 font-sans">
    <nav class="flex items-center justify-between max-w-7xl mx-auto px-6 py-5">
      <div class="flex items-center gap-2 font-bold text-xl text-slate-900">
        <span class="text-blue-600">&#10024;</span> {website_type}
      </div>
      <div class="hidden md:flex items-center gap-8">
        <a href="#features" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Features</a>
        <a href="#pricing" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Pricing</a>
        <a href="#contact" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Contact</a>
      </div>
    </nav>

    <section class="max-w-7xl mx-auto px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
      <div>
        <span class="text-xs font-bold uppercase tracking-widest text-blue-600">{theme} web engineering</span>
        <h1 class="mt-4 text-5xl md:text-6xl font-bold leading-tight text-slate-900">
          Ship polished web pages with local AI agents.
        </h1>
        <p class="mt-6 text-lg text-slate-500 leading-relaxed max-w-lg">
          A focused autonomous builder that plans, generates, validates, repairs,
          and previews production-ready Vue interfaces from a single prompt.
        </p>
        <div class="mt-8 flex flex-wrap gap-4">
          <a href="#contact" class="inline-flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors">
            Start building &#8594;
          </a>
          <a href="#features" class="inline-flex items-center gap-2 border border-slate-200 px-6 py-3 rounded-lg font-bold text-slate-700 hover:bg-slate-50 transition-colors">
            View system
          </a>
        </div>
      </div>
      <div class="bg-slate-900 text-white rounded-xl p-6 shadow-2xl">
        <p class="text-xs font-mono text-slate-400 mb-4">// builder pipeline</p>
        <div v-for="(section, index) in sections" :key="section" class="flex items-center gap-4 py-3 border-b border-white/10 last:border-0">
          <span class="font-mono text-yellow-400 text-sm w-8">{{ String(index + 1).padStart(2, '0') }}</span>
          <strong class="flex-1 text-sm">{{ section }}</strong>
          <span class="text-green-400">&#10003;</span>
        </div>
      </div>
    </section>

    <section id="features" class="max-w-7xl mx-auto px-6 py-20">
      <div class="mb-8">
        <span class="text-xs font-bold uppercase tracking-widest text-blue-600">Core capabilities</span>
        <h2 class="mt-2 text-3xl font-bold text-slate-900">Small team, strong workflow.</h2>
      </div>
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <article v-for="feature in ['Vue 3 Composition API', 'Vite-powered builds', 'TypeScript first', 'TailwindCSS styling']" :key="feature" class="p-6 border border-slate-200 rounded-xl bg-white hover:shadow-lg transition-shadow">
          <div class="w-6 h-6 text-blue-600 mb-3">&#9889;</div>
          <h3 class="font-bold text-slate-900 mb-1">{{ feature }}</h3>
          <p class="text-sm text-slate-500">Designed for reliable generation, quick iteration, and readable output.</p>
        </article>
      </div>
    </section>

    <section id="contact" class="max-w-7xl mx-auto px-6 py-20 text-center">
      <div class="w-8 h-8 text-blue-600 mx-auto mb-4">&#9993;</div>
      <h2 class="text-3xl font-bold text-slate-900 mb-3">Ready for the next prompt.</h2>
      <p class="text-slate-500 mb-6">Generate, validate, repair, and preview without leaving your local machine.</p>
      <a href="mailto:hello@example.com" class="inline-flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors">
        Contact team
      </a>
    </section>
  </div>
</template>
"""

    index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>""" + website_type + """</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>
"""

    main_ts = """import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

createApp(App).mount('#app')
"""

    style_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  margin: 0;
  font-family: system-ui, -apple-system, sans-serif;
}
"""

    env_d_ts = """/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}
"""

    return {
        "package.json": json.dumps(package_json, indent=2),
        "vite.config.ts": vite_config,
        "tsconfig.json": json.dumps(tsconfig_json, indent=2),
        "index.html": index_html,
        "src/main.ts": main_ts,
        "src/App.vue": app_vue,
        "src/style.css": style_css,
        "src/vite-env.d.ts": env_d_ts,
    }
