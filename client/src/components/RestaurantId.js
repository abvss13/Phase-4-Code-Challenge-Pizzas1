import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import './App.css';

export default function RestaurantId() {
  const [restaurant, setRestaurant] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    fetch(`https://pizza-restaurant-buse.onrender.com/restaurants/${id}`)
      .then((r) => r.json())
      .then((data) => setRestaurant(data));
  }, [id]);

  fetch(`https://pizza-restaurant-buse.onrender.com/restaurants/${id}`)
  .then((r) => r.json())
  return (
    <div>
      <h2>Welcome to:{restaurant.name}</h2>
      <h3>List of Pizzas Available in our restaurant:</h3>
      <ul>
        {restaurant.restaurant_pizzas &&
          restaurant.restaurant_pizzas.map((item) => (
            <div className='list'>
              <li key={item.pizza_id}>
              {item.pizza ? (
                <Link to={`/pizzas/${item.pizza_id}`}>{item.pizza.name}</Link>
              ) : (
                <span>No pizza information available</span>
              )}
            </li>
            </div> 
          ))}
      </ul>
    </div>
  );
}
