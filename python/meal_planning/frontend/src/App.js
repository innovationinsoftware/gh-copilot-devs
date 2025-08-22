import React, { useState, useEffect } from 'react';
import MealList from './components/MealList';
import { getMeals } from './services/api';

function App() {
    const [meals, setMeals] = useState([]);

    useEffect(() => {
        getMeals().then(data => setMeals(data));
    }, []);

    return (
        <div>
            <h1>Meal Planning App</h1>
            <MealList meals={meals} />
        </div>
    );
}

export default App;
