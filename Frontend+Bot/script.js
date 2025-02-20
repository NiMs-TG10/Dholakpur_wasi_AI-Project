document.getElementById('meetForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const meetId = document.getElementById('meetId').value;
    const name = document.getElementById('name').value;

    document.getElementById('status').textContent = 'Starting bot...';

    try {
        const response = await fetch('/start-bot', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ meetId, name })
        });

        // Debugging: Print response content
        const text = await response.text();
        console.log("Raw Response:", text);

        // Try parsing JSON
        const result = JSON.parse(text);
        document.getElementById('status').textContent = result.message;
    } catch (error) {
        document.getElementById('status').textContent = 'An error occurred! Check console.';
        console.error("Fetch error:", error);
    }
});
