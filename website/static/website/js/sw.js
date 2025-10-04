// Change the version number (v1) whenever you update the files in urlsToCache
const CACHE_NAME = "django-crm-pwa-v2";

// List of files to be immediately cached (make sure these paths are correct)
const urlsToCache = [
  "/", // The main landing page
  // Add your local static assets:
  "/static/website/css/styles.css",
  "/static/icons/apple-touch-icon.png",
  "/static/manifest.json",
  // You would add other critical HTML/CSS/JS files here too
];

// 1. Install Event: Caches the static assets
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log("Opened cache and pre-cached assets");
      return cache.addAll(urlsToCache);
    })
  );
});

// 2. Fetch Event: Intercepts requests
self.addEventListener("fetch", (event) => {
  // Strategy: Cache-first, then Network-fallback
  event.respondWith(
    caches.match(event.request).then((response) => {
      // Cache hit - return the response from the cache
      if (response) {
        return response;
      }
      // No match in cache - fetch from the network
      return fetch(event.request);
    })
  );
});

// 3. Activate Event: Cleans up old caches (crucial for updates)
self.addEventListener("activate", (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            console.log("Deleting old cache:", cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
