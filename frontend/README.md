# Todo WebApp
## monorepo, CI/CD using Github actions
---
## Todo WebApp Frontend

---


<br><br>


> <br>
> 
> ## Setup for local development
> 
> Make sure to clone the repository first.
> ### **Windows**
> ```powershell
>   $ cd frontend # change to frontend project directory
>   $ npm i # install all the node dependencies
>   $ npm run dev # to run the local dev server
> ```
> 
> <br>
> 
> ## Setup from scratch
> 
> ```powershell
>     $ npm create vite@latest
>     # select react and then react-ts
>     $ npm i # to install the dependencies
>     $ npm run dev # to start the dev server
>     $ ^C # to stop the dev server
>     $ npm i -D tailwindcss postcss autoprefixer
>     $ npx tailwindcss init -p
> ```
> 
> now configure `tailwind.convfig.js` to the following content
> ```javascript
>     module.exports = {
>         content: ["./src/**/*.{html,js,jsx,ts,tsx}"],
>         theme: {
>             extend: {},
>         },
>         plugins: [],
>     }
> ```
> now the project is initialized with react, typescript, tailwindcss with vite as tooling.
> 
> <br>