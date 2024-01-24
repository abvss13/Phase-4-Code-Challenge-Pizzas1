import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function RestaurantPizzaForm() {
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [pizzaId, setPizzaId] = useState("");
  const [restaurantId, setRestaurantId] = useState("");
  const [price, setPrice] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const newRestaurantPizza = {
      price: parseFloat(price), 
      pizza_id: parseInt(pizzaId),
      restaurant_id: parseInt(restaurantId),
    };
    fetch('https://pizza-restaurant-buse.onrender.com/restaurant_pizzas', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newRestaurantPizza),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('New RestaurantPizza added:', data);
        setPizzaId("");
        setRestaurantId("");
        setPrice("");

        navigate('/');
      })
      .catch((error) => {
        console.error('Error adding RestaurantPizza:', error);
      });
  };

  useEffect(() => {
    fetch("https://pizza-restaurant-buse.onrender.com/restaurants")
      .then((r) => r.json())
      .then((data) => setRestaurants(data))
      .catch((error) => console.error('Error fetching restaurants:', error));
  }, []);

  useEffect(() => {
    fetch("https://pizza-restaurant-buse.onrender.com/pizzas")
      .then((r) => r.json())
      .then((data) => setPizzas(data))
      .catch((error) => console.error('Error fetching pizzas:', error));
  }, []);

  return (
    <div>
      <h2>Add New RestaurantPizza</h2>
      <form onSubmit={handleSubmit}>
        <label className='form-label'>
          Pizza:
          <select className="form-select" value={pizzaId} onChange={(e) => setPizzaId(e.target.value)}>
            <option value="">Select Pizza</option>
            {pizzas.length > 0 &&
              pizzas.map((pizza) => (
                <option key={pizza.id} value={pizza.id}>
                  {pizza.name}
                </option>
              ))}
          </select>
        </label>
        <br />

        <label className='form-label'>
          Restaurant:
          <select className='form-select'
            value={restaurantId}
            onChange={(e) => setRestaurantId(e.target.value)}
          >
            <option value="">Select Restaurant</option>
            {restaurants.length > 0 &&
              restaurants.map((restaurant) => (
                <option key={restaurant.id} value={restaurant.id}>
                  {restaurant.name}
                </option>
              ))}
          </select>
        </label>
        <br />

        <label className='form-label'>
          Price:
          <input
            className='form-input'
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          />
        </label>
        <br />

        <button type="submit" className='form-button'>Add RestaurantPizza</button>
      </form>
    </div>
  );
}
