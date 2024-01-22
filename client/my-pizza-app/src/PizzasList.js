import React, { useState, useEffect } from 'react';

function PizzasList() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/pizzas')
      .then(response => response.json())
      .then(data => setPizzas(data))
      .catch(error => console.error('Error fetching pizzas:', error));
  }, []);

  return (
    <div>
      <h2>All Pizzas</h2>
      <ul>
        {pizzas.map(pizza => (
          <li key={pizza.id}>
            <strong>{pizza.name}</strong>: {pizza.ingredients}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PizzasList;
