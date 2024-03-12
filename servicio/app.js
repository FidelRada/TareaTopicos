const express = require('express');
const generateRoutes = require('./routes/gpt');

const app = express();

app.use(express.json());

app.use('/gpt', generateRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
