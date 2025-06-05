// server/utils/jwtMiddleware.js

/**
 * JWT Middleware for Socket.io and Express
 * ----------------------------------------
 * - verifySocketToken: checks `socket.handshake.auth.token`
 *   and attaches `socket.user = { id, username }` if valid.
 */

const jwt = require('jsonwebtoken');

function verifySocketToken(socket, next) {
  try {
    const token = socket.handshake.auth.token;
    if (!token) {
      return next(new Error('Authentication error: No token provided.'));
    }
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    socket.user = { id: decoded.id, username: decoded.username };
    next();
  } catch (err) {
    console.error('Socket auth error:', err.message);
    next(new Error('Authentication error.'));
  }
}

module.exports = { verifySocketToken };
