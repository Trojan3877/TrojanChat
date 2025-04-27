const express = require('express');
const app = express();
const exampleRoutes = require('./routes/exampleRoutes');

// Middleware
app.use(express.json());

// Routes
app.use('/api/example', exampleRoutes);

module.exports = app;
