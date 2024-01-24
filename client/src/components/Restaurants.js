 import {DeleteForever} from "@mui/icons-material"
import {useEffect, useState} from 'react';
import {Link} from "react-router-dom";
import './App.css';

export default function Restaurant() {
     const [restaurants, setRestaurants] = useState([])
    useEffect(()=> {
        fetch('https://pizza-restaurant-buse.onrender.com/restaurants')
        .then((r) => r.json())
        .then((data) => setRestaurants(data))
    },[]);
    const handleDelete = (id) => {
      fetch(`https://pizza-restaurant-buse.onrender.com/restaurants/${id}`, {
        method: 'DELETE',
      })
        .then((response) => {
          if (response.ok) {
            setRestaurants((prevRestaurants) => prevRestaurants.filter((restaurant) => restaurant.id !== id));
          } else {
            console.error('Error deleting restaurant:', response.status);
          }
        })
        .catch((error) => console.error('Error deleting restaurant:', error));
    };


  return (
    <div>
        <h2>Restaurants</h2>
        <ul>
        {restaurants.map((restaurant)=>(
            <span key ={restaurant.id}>
              <div className='list'>
               <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link>
                <span className="delete" onClick={() => handleDelete(restaurant.id)}>
                <DeleteForever/>
               </span> 
              </div>
            </span>
        ))}
        </ul> 
    </div>
  );
}
