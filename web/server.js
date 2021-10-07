// express 연동
const express = require('express');
const app = express();
const path = require('path');

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/web/views/intro/intro.html'))
});

// express에서 css 적용
app.use('/css', express.static(__dirname + '/web/css/'));

// express image 적용
app.use('/images', express.static(__dirname + '/images/'));




// 연결되는 포트
const port = 5000;
app.listen(port, () => console.log(`listening on ${port}!`));