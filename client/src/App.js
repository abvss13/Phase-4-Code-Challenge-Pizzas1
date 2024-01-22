import React from 'react';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Main from './components/Main';
import RestaurantPizza from './components/RestaurantPizza';

export default function App() {
  return (
    <div>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Main/>}/>
            <Route path="/rest" element={<RestaurantPizza/>} />
          </Routes>
        </BrowserRouter>
        
      </div>
  )
}
