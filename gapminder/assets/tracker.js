const { makeTracker } = require ("@objectiv/tracker-browser");

makeTracker({
    applicationId: 'dash-demo',
    endpoint: 'http://localhost:8081'  // local collector
});

export {};
