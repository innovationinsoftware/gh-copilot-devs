import React from 'react';

function MealList({ meals }) {
    return (
        <ul>
            {meals.map(meal => (
                <li key={meal.id}>
                    {meal.name} - {meal.calories} calories
                </li>
            ))}
        </ul>
    );
}

export default MealList;
