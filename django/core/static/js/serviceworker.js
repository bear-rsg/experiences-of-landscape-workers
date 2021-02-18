var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/',
    '/cookies/',
    '/offline/',
    '/journal/',
    '/journal/drafts/',
    '/accounts/profile/',
    
    'static/images/favicon.png',
    'static/images/pwa/icon-160.png',
    'static/images/pwa/icon-512.png',
    
    '/static/js/bootstrap.min.js',
    '/static/js/bootstrap.min.js.map',
    '/static/js/jquery-3.5.1.min.js',
    '/static/js/dexie.min.js',
    '/static/js/drafts.js',

    '/static/css/bootstrap.min.css',
    '/static/css/bootstrap.min.css.map',
    '/static/css/custom.css',
    '/static/css/custom_xs.css',
    '/static/css/custom_lg.css',

    'manifest.json'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});
