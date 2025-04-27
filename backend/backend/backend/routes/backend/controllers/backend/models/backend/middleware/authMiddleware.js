exports.protect = (req, res, next) => {
  // Dummy auth middleware
  const token = req.headers.authorization;

  if (token === 'secret-token') {
    next();
  } else {
    res.status(401).json({ message: 'Not authorized' });
  }
};
