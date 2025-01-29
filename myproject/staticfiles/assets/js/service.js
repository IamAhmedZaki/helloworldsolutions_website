document.addEventListener('DOMContentLoaded', function() {
    // Safely get all elements
    const elements = {
        image: document.getElementById('service-image'),
        title: document.getElementById('service-title'),
        description: document.getElementById('service-description'),
        list: document.getElementById('service-list'),
        details: document.getElementById('service-details')
    };

    // Check if all elements exist
    if (Object.values(elements).some(el => !el)) {
        console.error('Missing elements:', elements);
        return;
    }

    // Add click handlers after a small delay to ensure AOS animations don't interfere
    setTimeout(() => {
        document.querySelectorAll('.services-list a').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const service = this.dataset.service;
                if (window.servicesData[service]) {
                    updateService(service);
                }
            });
        });
        
        // Initialize with default service
        updateService('web-design');
    }, 100);

    function updateService(serviceKey) {
        const service = window.servicesData[serviceKey];
        
        // Update elements
        elements.image.src = service.image;
        elements.title.textContent = service.title;
        elements.description.textContent = service.description;
        elements.details.textContent = service.details;
        
        // Update features list
        elements.list.innerHTML = service.features
            .map(feature => `
                <li>
                    <i class="bi bi-check-circle"></i>
                    <span>${feature}</span>
                </li>
            `).join('');
        
        // Refresh AOS animations
        if (typeof AOS !== 'undefined') {
            AOS.refresh();
        }
    }
});