const express = require('express');
const cors = require('cors');
const mealRoutes = require('./routes/meals');

const app = express();
app.use(cors());
app.use(express.json());

app.use('/api/meals', mealRoutes);

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
