'use strict';

const restify = require('restify');


const server = restify.createServer();
server.get('/hello/:name', (req, res, next) => {
    let {
        name
    } = req.params;

    let message = 'hello '+name;
    res.send({
        status: 'OK',
        message
    });
    next();
});

server.listen(3100, function() {
    console.log('%s listening at %s', server.name, server.url);
});

console.log('restify cms started at: ');