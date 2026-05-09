import { defineConfig } from 'vite';

export default defineConfig({
  // Serve the public/ directory at the root.
  // This means public/sections/navbar.html → /sections/navbar.html ✅
  publicDir: 'public',

  // Build output goes into dist/
  build: {
    outDir: 'dist',
    // Copy all HTML entry points so Vercel picks them up
    rollupOptions: {
      input: {
        main: 'index.html',
        mark: 'mark.html',
        contact: 'contact.html',
        book: 'book.html',
      },
    },
  },
});
