async function fetchLatest() {
  try {
    const res = await fetch('/api/readings/latest');
    if (!res.ok) {
      document.getElementById('reading').innerText = 'No data';
      return;
    }
    const data = await res.json();
    document.getElementById('reading').innerText =
      `Işık: ${data.light}, pH: ${data.ph}, EC: ${data.ec}, Zaman: ${data.timestamp}`;
  } catch (err) {
    document.getElementById('reading').innerText = 'Hata: ' + err;
  }
}

document.getElementById('refresh').addEventListener('click', fetchLatest);

fetchLatest();
