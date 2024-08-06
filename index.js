const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.use(bodyParser.json());

app.post('/webhook', (req, res) => {
    const chatId = req.body.message.chat.id;
    const text = req.body.message.text;

    axios.post(`https://api.telegram.org/bot6683299629:AAHt20PuoQV8lgbrWYGGf9lzfEhleNbZHQ8/sendMessage`, {
        chat_id: chatId,
        text: `Balasan dari bot: ${text}`
    });

    res.send('ok');
});

app.listen(process.env.PORT || 3000, () => {
    console.log('Server berjalan di port 3000');
});
