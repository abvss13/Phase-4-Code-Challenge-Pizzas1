import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import PizzasList from './PizzasList';
import Restaurant from './Restaurant';
import Home from './Home';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <p>Welcome to Sunset Pizza Palace</p>

          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/restaurants">Restaurants</Link>
              </li>
              <li>
                <Link to="/pizzas">Pizzas</Link>
              </li>
            </ul>
          </nav>

          <Routes>
            <Route path="/restaurants" element={<RestaurantList />} />
            <Route path="/pizzas" element={<PizzasList />} />
            <Route path="/" element={<Home />} />
          </Routes>
        </header>
      </div>
    </Router>
  );
}

function RestaurantList() {
  return <h2>Restaurant List</h2>;
}

export default App;
