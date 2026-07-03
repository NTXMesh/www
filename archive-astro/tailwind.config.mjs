/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'mesh-green':     '#67EA94',
        'mesh-green-d':   '#4ac97a',
        'mesh-green-l':   '#9ef5b9',
        'mesh-bg':        '#0d1117',
        'mesh-surface':   '#161b22',
        'mesh-surface-2': '#21262d',
        'mesh-border':    '#30363d',
        'mesh-text':      '#e6edf3',
        'mesh-muted':     '#8b949e',
      },
      fontFamily: {
        mono: ['"Space Mono"', 'ui-monospace', 'monospace'],
        sans: ['"DM Sans"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      typography: {
        DEFAULT: {
          css: {
            color: '#e6edf3',
            a: { color: '#67EA94' },
            h1: { color: '#e6edf3', fontFamily: '"Space Mono", monospace' },
            h2: { color: '#e6edf3', fontFamily: '"Space Mono", monospace' },
            h3: { color: '#e6edf3', fontFamily: '"Space Mono", monospace' },
          },
        },
      },
    },
  },
  plugins: [],
};
