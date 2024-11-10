import http from "http";
import express from "express";

const server = http.createServer((request, response) =>{
    response.statusCode = 200;
    response.setHeader("Content-type", "text/plain");
    response.end("Hello, World!\n");
});

server.listen(3000, () => {
    console.log("Server running at localhost:3000");
});

