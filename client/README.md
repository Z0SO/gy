# Frontend con Svelte

- Requisitos previos antes de ejecutar el proyecto:
  - Node.js
  - npm

- Para ejecutar el proyecto en local:
- Clonar el repositorio
- Ejecutar el comando `npm install`
- Ejecutar el comando `npm run dev`
- Abrir el navegador en la dirección `localhost:5173/`

---

## Estilos de CSS y Componentes

> **Nota:** Los estilos voy a usar componentes de flowbite-svelte con npm

#### Instalación

- Puedes seguir la documentación de [Flowbite-Svelte](https://flowbite-svelte.com/docs/pages/quickstart) para instalar los estilos y componentes.

- Asegurate de ejecutar un `npm i` antes de instalar los estilos de Flowbite-Svelte.

- Para instalar TailwindCSS

```bash
npx svelte-add@latest tailwindcss
npm i
```

- Para instalar Flowbite-Svelte

```bash
npm i -D flowbite-svelte flowbite
```

Lo siguiente es modificar el archivo tailwind.config.js

```js
import type { Config } from 'tailwindcss';
import flowbitePlugin from 'flowbite/plugin'

export default {
  content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],
  darkMode: 'selector',
  theme: {
    extend: {
      colors: {
        // flowbite-svelte
        primary: {
          50: '#FFF5F2',
          100: '#FFF1EE',
          200: '#FFE4DE',
          300: '#FFD5CC',
          400: '#FFBCAD',
          500: '#FE795D',
          600: '#EF562F',
          700: '#EB4F27',
          800: '#CC4522',
          900: '#A5371B'
        }
      }
    }
  },
  plugins: [flowbitePlugin]
} as Config;
```

Con esto ya puedes usar los estilos de Flowbite-Svelte en tu proyecto.

---
