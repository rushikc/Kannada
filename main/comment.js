const fs = require('fs');
const server = require('http').createServer();

server.on('request', (req, res) => {
    const src = fs.createReadStream("../data/comment_log.csv");
    src.pipe(res);
});

server.listen(8084);