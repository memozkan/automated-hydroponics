async function fetchLatest() {
  const status = document.getElementById('status');
  status.innerText = 'Yükleniyor...';
  try {
    const res = await fetch('/api/readings/latest');
    if (!res.ok) {
      throw new Error('Veri yok');
    }
    const data = await res.json();
    document.getElementById('light').innerText = data.light ?? '-';
    document.getElementById('ph').innerText = data.ph ?? '-';
    document.getElementById('ec').innerText = data.ec ?? '-';
    if (data.timestamp) {
      document.getElementById('timestamp').innerText = new Date(data.timestamp).toLocaleString('tr-TR');
    } else {
      document.getElementById('timestamp').innerText = '-';
    }
    status.innerText = '';
  } catch (err) {
    document.getElementById('light').innerText = '-';
    document.getElementById('ph').innerText = '-';
    document.getElementById('ec').innerText = '-';
    document.getElementById('timestamp').innerText = '-';
    status.innerText = 'Hata: ' + err.message;
  }
}

document.getElementById('refresh').addEventListener('click', fetchLatest);

const autoBox = document.getElementById('auto-refresh');
let autoTimer = null;

autoBox.addEventListener('change', () => {
  if (autoBox.checked) {
    fetchLatest();
    autoTimer = setInterval(fetchLatest, 5000);
  } else {
    clearInterval(autoTimer);
    autoTimer = null;
  }
});
