// require('dotenv').config();
// const express = require('express');
// const bodyParser = require('body-parser');
// const cookieSession = require('cookie-session');
// const { OAuth2Client } = require('google-auth-library');

// const app = express();
// const CLIENT_ID = process.env.CLIENT_ID;
// const CLIENT_SECRET = process.env.CLIENT_SECRET;
// const REDIRECT_URI = 'http://localhost:8000/oauth2callback';
// const oAuth2Client = new OAuth2Client(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI);

// app.use(bodyParser.json());
// app.use(cookieSession({
//   name: 'session',
//   keys: ['key1', 'key2'],
//   maxAge: 24 * 60 * 60 * 1000 // 24 hours
// }));

// // Serve static files from the 'public' folder
// app.use(express.static('public'));

// app.get('/', (req, res) => {
//   res.sendFile(__dirname + '/public/index.html');
// });

// app.get('/auth/google', (req, res) => {
//   const url = oAuth2Client.generateAuthUrl({
//     access_type: 'offline',
//     scope: ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
//   });
//   res.redirect(url);
// });

// app.get('/oauth2callback', async (req, res) => {
//   try {
//     const { tokens } = await oAuth2Client.getToken(req.query.code);
//     oAuth2Client.setCredentials(tokens);
    
//     // verify the token
//     const ticket = await oAuth2Client.verifyIdToken({
//       idToken: tokens.id_token,
//       audience: CLIENT_ID,
//     });
//     const payload = ticket.getPayload();

//     // check if the domain is iiitg.ac.in
//     if (payload['hd'] === 'iiitg.ac.in') {
//       req.session.token = tokens.id_token;
//       res.redirect('/feedback');
//     } else {
//       res.status(401).send('Unauthorized: Only IIITG domain is allowed');
//     }
//   } catch (error) {
//     console.error('Error during Google Auth callback', error);
//     res.status(500).send('Authentication failed');
//   }
// });

// app.get('/feedback', (req, res) => {
//   if (req.session.token) {
//     res.sendFile(__dirname + '/public/feedback.html');
//   } else {
//     res.redirect('/');
//   }
// });

// const PORT = process.env.PORT || 8000;
// app.listen(PORT, () => {
//     console.log(`Server is running on http://localhost:${PORT}`);
//   }).on('error', (e) => {
//     console.error('Error starting server: ', e);
//   });
  

// require('dotenv').config();
// const express = require('express');
// const bodyParser = require('body-parser');
// const cookieSession = require('cookie-session');
// const { OAuth2Client } = require('google-auth-library');
// const sqlite3 = require('sqlite3').verbose();

// const app = express();
// const CLIENT_ID = process.env.CLIENT_ID;
// const CLIENT_SECRET = process.env.CLIENT_SECRET;
// const REDIRECT_URI = 'http://localhost:8000/oauth2callback';
// const oAuth2Client = new OAuth2Client(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI);

// app.use(bodyParser.json());
// app.use(bodyParser.urlencoded({ extended: true }));
// app.use(cookieSession({
//   name: 'session',
//   keys: ['key1', 'key2'],
//   maxAge: 24 * 60 * 60 * 1000 // 24 hours
// }));

// // Serve static files from the 'public' folder
// app.use(express.static('public'));

// app.get('/', (req, res) => {
//   res.sendFile(__dirname + '/public/index.html');
// });

// app.get('/auth/google', (req, res) => {
//   const url = oAuth2Client.generateAuthUrl({
//     access_type: 'offline',
//     scope: ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
//   });
//   res.redirect(url);
// });

// app.get('/oauth2callback', async (req, res) => {
//   try {
//     const { tokens } = await oAuth2Client.getToken(req.query.code);
//     oAuth2Client.setCredentials(tokens);
    
//     // verify the token
//     const ticket = await oAuth2Client.verifyIdToken({
//       idToken: tokens.id_token,
//       audience: CLIENT_ID,
//     });
//     const payload = ticket.getPayload();

//     // check if the domain is iiitg.ac.in
//     if (payload['hd'] === 'iiitg.ac.in') {
//       req.session.token = tokens.id_token;
//       res.redirect('/feedback');
//     } else {
//       res.status(401).send('Unauthorized: Only IIITG domain is allowed');
//     }
//   } catch (error) {
//     console.error('Error during Google Auth callback', error);
//     res.status(500).send('Authentication failed');
//   }
// });

// app.get('/feedback', (req, res) => {
//   if (req.session.token) {
//     res.sendFile(__dirname + '/public/feedback.html');
//   } else {
//     res.redirect('/');
//   }
// });

// app.post('/submit-feedback', (req, res) => {
//   if (req.session.token) {
//     const db = new sqlite3.Database('./feedback.db', sqlite3.OPEN_READWRITE);
//     const { username, feedback } = req.body;

//     const query = `INSERT INTO feedback (username, feedback) VALUES (?, ?)`;
//     db.run(query, [username, feedback], function(err) {
//       if (err) {
//         res.status(500).send("Error submitting feedback");
//         console.error(err.message);
//       } else {
//         res.send("Feedback submitted successfully");
//         console.log(`A row has been inserted with rowid ${this.lastID}`);
//       }
//       // Close the database connection inside the callback
//       db.close();
//     });
//   } else {
//     res.status(403).send('Unauthorized: No active session');
//   }
// });

// const PORT = process.env.PORT || 8000;
// app.listen(PORT, () => {
//   console.log(`Server is running on http://localhost:${PORT}`);
// }).on('error', (e) => {
//   console.error('Error starting server: ', e);
// });


require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const cookieSession = require('cookie-session');
const { OAuth2Client } = require('google-auth-library');

const app = express();
const CLIENT_ID = process.env.CLIENT_ID;
const CLIENT_SECRET = process.env.CLIENT_SECRET;
const REDIRECT_URI = 'http://localhost:8000/oauth2callback';
const oAuth2Client = new OAuth2Client(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI);

// Array to store feedback in-memory
const feedbacks = [];
const recommendations = [];
const skills = [];


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieSession({
  name: 'session',
  keys: ['key1', 'key2'],
  maxAge: 24 * 60 * 60 * 1000 // 24 hours
}));

// Serve static files from the 'public' folder
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.get('/auth/google', (req, res) => {
  const url = oAuth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
  });
  res.redirect(url);
});

app.get('/oauth2callback', async (req, res) => {
  try {
    const { tokens } = await oAuth2Client.getToken(req.query.code);
    oAuth2Client.setCredentials(tokens);
    
    // verify the token
    const ticket = await oAuth2Client.verifyIdToken({
      idToken: tokens.id_token,
      audience: CLIENT_ID,
    });
    const payload = ticket.getPayload();

    // check if the domain is iiitg.ac.in
    if (payload['hd'] === 'iiitg.ac.in') {
      req.session.token = tokens.id_token;
      res.redirect('/feedback');
    } else {
      res.status(401).send('Unauthorized: Only IIITG domain is allowed');
    }
  } catch (error) {
    console.error('Error during Google Auth callback', error);
    res.status(500).send('Authentication failed');
  }
});

app.get('/feedback', (req, res) => {
  if (req.session.token) {
    res.sendFile(__dirname + '/public/feedback.html');
  } else {
    res.redirect('/');
  }
});

app.post('/submit-feedback', (req, res) => {
  if (req.session.token) {
    const { username, feedback } = req.body;

    // Add the feedback to the in-memory array
    feedbacks.push({
      id: feedbacks.length + 1,
      username,
      feedback,
      submitted_at: new Date().toISOString()
    });

    // Log feedback to the server's terminal
    console.log('New feedback received:', feedbacks[feedbacks.length - 1]);

    res.send("Feedback submitted successfully");
  } else {
    res.status(403).send('Unauthorized: No active session');
  }
});

// Endpoint for submitting a recommendation
app.post('/submit-recommendation', (req, res) => {
  const { skill } = req.body; // Assuming the form input has name='skill'
  recommendations.push({
    id: recommendations.length + 1,
    skill: skill,
    submitted_at: new Date().toISOString()
  });
  console.log('New recommendation received:', recommendations[recommendations.length - 1]);
  res.send("Recommendation submitted successfully");
});

// Endpoint for adding a new skill
app.post('/add-skill', (req, res) => {
  const { skill } = req.body; // Assuming the form input has name='skill'
  skills.push(skill);
  console.log('New skill added:', skill);
  res.send("Skill added successfully");
});


const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
}).on('error', (e) => {
  console.error('Error starting server: ', e);
});
