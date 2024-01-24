import {Routes, Route} from "react-router-dom"
import Restaurant from "./Restaurants";
import Header from './Header';
import RestaurantId from "./RestaurantId";
import Pizza from "./Pizza";
import RestaurantPizzaForm from "./RestaurantPizzaForm";
import './App.css';

function App() {
  return (
    <div className="App">
      <Header/>
      <main>
        <Routes>
          <Route path="/restaurant_pizzas/new" element={<RestaurantPizzaForm />} />
          <Route path="/pizzas/:id" element={<Pizza />} />
          <Route path="/restaurants/:id" element={<RestaurantId/>} />
          <Route path="/" element={<Restaurant />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
