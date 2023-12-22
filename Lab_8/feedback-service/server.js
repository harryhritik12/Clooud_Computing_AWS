const express = require('express');
const cors = require('cors');  // Importing the CORS module
const app = express();

// Enable CORS for all routes

// This is middleware that helps to parse JSON in request body
app.use(express.json());

// Simple POST endpoint for feedback
app.post('/feedback', (req, res) => {
    // In a real-world scenario, you might save this feedback to a database
    console.log('Received feedback:', req.body);

    // Send a response to the client
    res.json({ status: 'Feedback received!' });
});

// Listen on port 3000
app.listen(3000, () => {
    console.log('Feedback service listening on port 3000!');
});
