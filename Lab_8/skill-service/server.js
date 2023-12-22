const express = require('express');
const cors = require('cors');
const app = express();

// Enable CORS for all routes
app.use(cors());
// Middleware to parse JSON in request body
app.use(express.json());

// All predefined skills
const allSkills = ["js", "java", "cpp", "flutter"]
// Skills chosen by the user
const userSkills = [];

// GET endpoint to fetch all predefined skills
app.get('/all-skills', (req, res) => {
    res.json({ skills: allSkills });
});

// POST endpoint to add a user's skill
app.post('/add-user-skill', (req, res) => {
    const skill = req.body.skill;
    if (allSkills.includes(skill) && !userSkills.includes(skill)) {
        userSkills.push(skill);
        console.log('Added user skill:', skill);
        res.json({ status: 'Skill added!', skill: skill });
    } else {
        res.status(400).json({ status: "Skill either doesn't exist or has already been added!" });
    }
});

// GET endpoint to fetch all user's skills
app.get('/user-skills', (req, res) => {
    res.json({ skills: userSkills });
});

// Listen on port 5000 (to avoid conflicts with other services)
app.listen(5000, () => {
    console.log('Skills service listening on port 5000!');
});
