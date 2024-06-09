const express = require('express');
const compression = require('compression');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Enable gzip and Brotli compression
app.use(compression());

// Serve static files
app.use(express.static(path.join(__dirname, 'src')));

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
