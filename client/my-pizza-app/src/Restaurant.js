import React, { useState, useEffect } from 'react';

const apiUrl = 'http://127.0.0.1:5555';

function Restaurant({ id, name }) {
  const [details, setDetails] = useState('');
  const [showDetails, setShowDetails] = useState(true);

  useEffect(() => {
    fetch(`${apiUrl}/${id}`)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setDetails(data.details);
      });
  }, [id]);

  const toggleDetails = () => {
    setShowDetails(!showDetails);
  };

  return (
    <div onClick={toggleDetails}>
      <h3>{name}</h3>
      {showDetails && <p>{details}</p>}
    </div>
  );
}

function RestaurantDropdown({ restaurants }) {
  const [selectedRestaurant, setSelectedRestaurant] = useState(null);

  const handleRestaurantChange = (event) => {
    const selectedId = event.target.value;
    setSelectedRestaurant(selectedId);
  };

  return (
    <div>
      <label htmlFor="restaurantDropdown">Select a Restaurant: </label>
      <select id="restaurantDropdown" onChange={handleRestaurantChange}>
        <option value="">Select a restaurant</option>
        {restaurants.map(restaurant => (
          <option key={restaurant.id} value={restaurant.id}>
            {restaurant.name}
          </option>
        ))}
      </select>

      {selectedRestaurant && (
        <Restaurant id={selectedRestaurant} name={selectedRestaurant.name} />
      )}
    </div>
  );
}

export default RestaurantDropdown;
