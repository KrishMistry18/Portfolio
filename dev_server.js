const express = require('express');
const app = express();
const chatHandler = require('./api/chat.js');

app.use(express.json());
app.post('/api/chat', (req, res) => {
    chatHandler(req, res);
});

app.listen(3000, () => {
    console.log("Test server running on port 3000");
});
