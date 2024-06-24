document.addEventListener('DOMContentLoaded', (event: Event) => {
    const container = document.getElementById('grid');

    if (container) {
        for (let i = 1; i <= 16; i++) {
            const gridItem = document.createElement('div');
            gridItem.className = 'grid-item';
            gridItem.textContent = i.toString();
            container.appendChild(gridItem);
        }
    } else {
        console.error('O container com o id "grid-container" não foi encontrado.');
    }
});
