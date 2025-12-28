// Chart.js CDN loader and fallback
(function() {
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
    script.onload = function() {
        if (typeof Chart === 'undefined') {
            alert('Chart.js failed to load.');
        }
    };
    document.head.appendChild(script);
})();
