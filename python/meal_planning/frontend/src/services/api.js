const API_URL = 'http://localhost:5000/api/meals';

export async function getMeals() {
    const response = await fetch(API_URL);
    return response.json();
}
