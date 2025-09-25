async function fetchCoins() {
    let res = await fetch('/api/coins');
    let coins = await res.json();
    
    // Ensure Vanry is first if available
    coins.sort((a, b) => {
        if (a.symbol === "vanry") return -1;
        if (b.symbol === "vanry") return 1;
        return 0;
    });
    displayCoins(coins);
}

function displayCoins(coins) {
    let table = document.getElementById('coinTable');
    table.innerHTML = '';
    coins.forEach(coin => {
        let row = document.createElement('tr');
        row.classList.add('cursor-pointer', 'hover:bg-gray-200');
        row.innerHTML = `
            <td class="border px-4 py-2 flex items-center space-x-2">
                <img src="${coin.image}" alt="${coin.name}" class="w-6 h-6"> 
                <span>${coin.name}</span>
            </td>
            <td class="border px-4 py-2">${coin.current_price}</td>
            <td class="border px-4 py-2 ${coin.price_change_percentage_24h >= 0 ? 'text-green-600' : 'text-red-600'}">
                ${coin.price_change_percentage_24h.toFixed(2)}%
            </td>
        `;
        row.onclick = () => showCoinDetails(coin.id);
        table.appendChild(row);
    });
}

async function showCoinDetails(coinId) {
    let res = await fetch(`/api/coin/${coinId}/chart?days=7`);
    let data = await res.json();
    let labels = data.prices.map(p => new Date(p[0]).toLocaleDateString());
    let prices = data.prices.map(p => p[1]);

    let ctx = document.getElementById('coinChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: coinId.toUpperCase(),
                data: prices,
                borderColor: 'blue',
                fill: false
            }]
        }
    });
}

document.getElementById('searchInput').addEventListener('input', async (e) => {
    let query = e.target.value.toLowerCase();
    let res = await fetch('/api/coins');
    let coins = await res.json();
    coins = coins.filter(c => c.name.toLowerCase().includes(query) || c.symbol.toLowerCase().includes(query));
    displayCoins(coins);
});

document.getElementById('toggleTheme').addEventListener('click', () => {
    let html = document.documentElement;
    if (html.getAttribute('data-theme') === 'light') {
        html.setAttribute('data-theme', 'dark');
        document.body.classList.replace('bg-gray-100', 'bg-gray-900');
        document.body.classList.replace('text-gray-900', 'text-gray-100');
    } else {
        html.setAttribute('data-theme', 'light');
        document.body.classList.replace('bg-gray-900', 'bg-gray-100');
        document.body.classList.replace('text-gray-100', 'text-gray-900');
    }
});

fetchCoins();
