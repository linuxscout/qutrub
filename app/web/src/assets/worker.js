let CACHE_NAME = 'qutrub';
let urlsToCache = [
  '.',
  'index.html',
  'image/doc/idea.png',
  'image/doc/levels.png',
  'image/doc/methods.png',
  'image/doc/tenses.png',
  'image/projects/adawat.png',
  'image/projects/ayaspell.png',
  'image/projects/pyarabic.png',
  'image/projects/qutrub.jpg',
  'image/projects/radif.png',
  'image/projects/tashaphyne.png',
  'image/arabeyes_logo.png',
  'image/dreamdevdz.png',
  'image/kuwaitnet.jpg',
  'image/logo.jpg',
  'css/style.css',
];

// Install a service worker
self.addEventListener('install', event => {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        return cache.addAll(urlsToCache);
      }).catch((err)=>{
        console.log(err)
      }),
  );
});


// Update a service worker
self.addEventListener('activate', event => {
  // we will work on this later.
});