const inputText = document.getElementById('inputText');
const output = document.getElementById('output');
const translateBtn = document.getElementById('translateBtn');
const language = document.getElementById('language');

translateBtn.addEventListener('click', async () => {
    const text = inputText.value.trim();
    if (!text) return;

    output.innerHTML = '<p class="loading">Translating...</p>';
    translateBtn.disabled = true;

    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/translate-text', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, targetLanguage: language.value })
        });

        const data = await response.json();
        output.innerHTML = `<p class="result">${data.translatedText || data.error}</p>`;
    } catch (err) {
        output.innerHTML = '<p class="result">Network error. Is the server running?</p>';
    }

    translateBtn.disabled = false;
});