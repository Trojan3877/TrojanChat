// server/models/User.js

/**
 * User Model
 * ----------
 * - Stores registered users with hashed passwords
 */

const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true,
    trim: true,
    minlength: 3
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true
  },
  passwordHash: {
    type: String,
    required: true
  }
}, { timestamps: true });

module.exports = mongoose.model('User', UserSchema);
