const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = 8080;  // Port for the API Gateway

app.use(cors());
app.use(express.json());

app.use((req, res, next) => {
    console.log(`Received ${req.method} request on ${req.path}`);
    next();
});

// Feedback Service Route
app.use('/feedback', async (req, res) => {
    try {
        console.log("Routing to Feedback Service");
        const response = await axios.post('http://localhost:3000/feedback', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Error contacting feedback service' });
    }
});

// Recommendation Service Route
app.use('/recommend', async (req, res) => {
    try {
        console.log("Routing to Recommendation Service");
        const response = await axios.post('http://localhost:4000/recommend', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Error contacting recommendation service' });
    }
});

// Skill Service Routes
app.get('/all-skills', async (req, res) => {
    try {
        console.log("Routing to Skills Service - Fetching All Skills");
        const response = await axios.get('http://localhost:5000/all-skills');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Error contacting skills service' });
    }
});

app.post('/add-user-skill', async (req, res) => {
    try {
        console.log("Routing to Skills Service - Adding User Skill");
        const response = await axios.post('http://localhost:5000/add-user-skill', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Error contacting skills service' });
    }
});

// Start the API Gateway
app.listen(PORT, () => {
    console.log(`API Gateway is running on port ${PORT}`);
});
