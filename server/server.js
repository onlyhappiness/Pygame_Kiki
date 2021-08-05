const express = require('express');
const app = express();

app.get('/', (req, res) => res.sendFile(__dirname + '../web/intro.html'));



const port = 5000;
app.listen(port, () => console.log(`listening on ${port}!`));