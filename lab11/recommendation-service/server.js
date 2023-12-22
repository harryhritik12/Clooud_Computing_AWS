// const express = require('express');
// const cors = require('cors');
// const app = express();


// // Middleware to parse JSON in request body
// app.use(express.json());

// // POST endpoint for recommendations
// app.post('/recommend', (req, res) => {
//     // In a real-world scenario, you might save this recommendation to a database
//     console.log('Received recommendation for:', req.body.skill);

//     // Send a response to the client
// });

// // Listen on port 4000 (to avoid conflict with feedback service)
// app.listen(4000, () => {
//     console.log('Recommendation service listening on port 4000!');
// });

const express = require('express');
const cors = require('cors');
const app = express();

// Middleware to parse JSON in request body
app.use(express.json());

// Middleware to enable CORS (Cross-Origin Resource Sharing)
app.use(cors());

// POST endpoint for recommendations
app.post('/recommend', (req, res) => {
    // In a real-world scenario, you might save this recommendation to a database
    const skill = req.body.skill;
    console.log('Received recommendation for:', skill);

    // Send a response to the client
    res.json({ status: 'Recommendation received successfully', skill });
});

// Listen on port 4000 (to avoid conflict with other services)
app.listen(4000, () => {
    console.log('Recommendation service listening on port 4000!');
});

