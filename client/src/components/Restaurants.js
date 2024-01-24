
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './App.css';

export default function Restaurant() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch('https://pizza-restaurant-buse.onrender.com/restaurants')
      .then((r) => r.json())
      .then((data) => setRestaurants(data))
      .catch((error) => console.error('Error fetching restaurants:', error));
  }, []);

  return (
    <div>
      <h2>Restaurants</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <div className='list'>
              <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
