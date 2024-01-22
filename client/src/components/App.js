import { Routes, Route } from "react-router-dom";
import Header from "./Header";
import Home from "./Home";
import Hero from "./Hero";
import HeroPowerForm from "./HeroPowerForm";
import Power from "./Power";
import PowerEditForm from "./PowerEditForm";

function App() {
  return (
    <>
      <Header />
      <main>
        <Routes>
          <Route path="/heroes/:id" element={<Hero />} />
          <Route path="/hero_powers/new" element={<HeroPowerForm />} />
          <Route path="/powers/:id/edit" element={<PowerEditForm />} />
          <Route path="/powers/:id" element={<Power />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </main>
    </>
  );
}

export default App;
