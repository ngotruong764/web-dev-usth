console.log("Hello world");
const EventListener = require("events");
const emitter = new EventListener();

// register a listener
emitter.on("event" ,() =>{
    console.log("An even occurred!");
});

// emit the even
emitter.emit("event");

//
const events = require("events");