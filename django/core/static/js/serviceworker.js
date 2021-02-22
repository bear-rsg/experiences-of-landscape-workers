var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/',
    '/cookies/',
    '/offline/',
    '/journal/drafts/',
    
    'static/images/favicon.png',
    'static/images/pwa/icon-48.png',
    'static/images/pwa/icon-72.png',
    'static/images/pwa/icon-96.png',
    'static/images/pwa/icon-128.png',
    'static/images/pwa/icon-144.png',
    'static/images/pwa/icon-152.png',
    'static/images/pwa/icon-167.png',
    'static/images/pwa/icon-180.png',
    'static/images/pwa/icon-192.png',
    'static/images/pwa/icon-256.png',
    'static/images/pwa/icon-512.png',
    'static/images/pwa/icon-1024.png',
    
    '/static/js/bootstrap.min.js',
    '/static/js/bootstrap.min.js.map',
    '/static/js/jquery-3.5.1.min.js',
    '/static/js/dexie.min.js',
    '/static/js/main.js',
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
// self.addEventListener("fetch", event => {
//     event.respondWith(
//         caches.match(event.request)
//             .then(response => {
//                 return response || fetch(event.request);
//             })
//             .catch(() => {
//                 return caches.match('/offline/');
//             })
//     )
// });






// // Network falling back to the cache
// self.addEventListener('fetch', function(event) {
//     event.respondWith(

//       fetch(event.request).catch(function() {
//         return caches.match(event.request);
//       })

//     );
//   });



//   // Cache falling back to the network
//   self.addEventListener('fetch', function(event) {
//     event.respondWith(

//       caches.match(event.request).then(function(response) {
//         return response || fetch(event.request);
//       })

//     );
//   });
  



//   // Generic fallback
//   self.addEventListener('fetch', function(event) {
//     event.respondWith(

//       // Try the cache
//       caches.match(event.request).then(function(response) {
//         // Fall back to network
//         return response || fetch(event.request);
//       }).catch(function() {
//         // If both fail, show a generic fallback:
//         return caches.match('/offline.html');
//         // However, in reality you'd have many different
//         // fallbacks, depending on URL & headers.
//         // Eg, a fallback silhouette image for avatars.
//       })

//     );
//   });






  // My attempt: Network -> Cache -> Fallback
  self.addEventListener('fetch', function(event) {
    
    if (navigator.onLine) {
        event.respondWith(
            // Network falling back to the cache
            fetch(event.request).catch(function() {
                return caches.match(event.request);
            })
        )
    }
    else {
        event.respondWith(
            caches.match(event.request)
                .then(response => {
                    return response || fetch(event.request);
                })
                .catch(() => {
                    return caches.match('/offline/');
                })
        )
    }
    
  });


