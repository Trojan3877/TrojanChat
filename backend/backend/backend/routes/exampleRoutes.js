const express = require('express');
const router = express.Router();
const { getExample } = require('../controllers/exampleController');

router.get('/', getExample);

module.exports = router;
