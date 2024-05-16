import express from "express";
import cors from "cors";
import bodyParser from "body-parser";

const app = express();
const port = 3001;

app.use(cors());
app.use(bodyParser.json());

app.post("/message", (req, res) => {
    const message = req.body.message;
    // Process the message and generate a response using GPT-4 API or any other method
    const response = `You said: ${message}`
})