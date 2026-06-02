require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const { MongoMemoryServer } = require('mongodb-memory-server');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Routes
app.use('/api/auth', require('./routes/authRoutes'));
app.use('/api/predictions', require('./routes/predictionRoutes'));
app.use('/api/contact', require('./routes/contactRoutes'));

// Connect to MongoDB
const connectDB = async () => {
  let mongoUri = process.env.MONGO_URI;
  
  try {
    if (mongoUri) {
      console.log(`Attempting to connect to MongoDB at ${mongoUri}...`);
      await mongoose.connect(mongoUri);
      console.log(`MongoDB Connected: ${mongoose.connection.host}`);
      return; // Success
    }
  } catch (error) {
    console.log(`Could not connect to ${mongoUri}. Error: ${error.message}`);
    console.log('Falling back to MongoDB Memory Server...');
  }

  // Fallback if no MONGO_URI provided or if connection failed
  try {
    const mongoServer = await MongoMemoryServer.create();
    const memoryUri = mongoServer.getUri();
    console.log(`MongoDB Memory Server started at ${memoryUri}`);
    
    await mongoose.connect(memoryUri);
    console.log(`MongoDB (Memory) Connected: ${mongoose.connection.host}`);
  } catch (error) {
    console.error(`Failed to start Memory Server: ${error.message}`);
    process.exit(1);
  }
};

connectDB().then(() => {
  const PORT = process.env.PORT || 5000;
  app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
});
