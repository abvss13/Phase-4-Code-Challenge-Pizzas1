import {useEffect, useState} from 'react'
import { Link, useParams } from 'react-router-dom'
import './App.css';


export default function Pizza() {
  const [pizza, setPizza] = useState([])
  const { id }= useParams();

  useEffect(() => {
    fetch(`https://pizza-restaurant-buse.onrender.com/pizzas/${id}`)
    .then((r) => r.json())
    .then((data) => setPizza(data))
  },[id])
  return (
    <div>
        <div className='pizza'>
        <h2>{pizza.name}</h2>
        <p>Ingredients:{pizza.ingredients}</p>
        </div>
      <p>
        <Link to="/restaurant_pizzas/new">Add Restaurant Pizza</Link>
      </p>
    </div>
  )
}
