# front

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
### Structure of src
- assets: static assets, such as logos or background images, go here

- components: pieces that may go on multiple pages, such as an event modal

- mixins: functions and other elements that should be available globally, such as rules.js where you may want to access
the same rule(s) in multiple views/components

- plugins: contains plugins to be used by vue

- router: contains index.js, which holds routes for various pages such as login and home. add views and their 
routes here to call `router.push('url')` and have it navigate to its corresponding view

- views: This is where pages are stored. These are rendered in the main section of the app, and have routes associated

- App.vue: This is the main vue template, and contains the router where all the additional pages are rendered.

- main.js: This is the script that ties everything together and sticks it onto an actual html file.

### Installed Dependencies
[Vue CLI](https://cli.vuejs.org/config/)

[Vue Router](https://router.vuejs.org/guide/)

[Vuetify](https://vuetifyjs.com/en/introduction/why-vuetify/#guide)

[VueSession](https://www.npmjs.com/package/vue-session)


