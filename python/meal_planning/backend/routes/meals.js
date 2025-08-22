const express = require('express');
const router = express.Router();

let meals = [
    { id: 1, name: 'Spaghetti', calories: 400 },
    { id: 2, name: 'Chicken Salad', calories: 300 },
];

// Get all meals
router.get('/', (req, res) => {
    res.json(meals);
});

// Add a new meal
router.post('/', (req, res) => {
    const newMeal = { id: Date.now(), ...req.body };
    meals.push(newMeal);
    res.status(201).json(newMeal);
});

module.exports = router;
