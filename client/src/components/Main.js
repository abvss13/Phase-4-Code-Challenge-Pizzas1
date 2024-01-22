import Header from "./Header";
import Banner from "./Banner";
import img from "../assets/pizza.avif"
import Restaurant from "./Restaurant";




function Main() {
  return (
    <div className="container app">
      <Header restaurantName="Available Restaurants" />
      <Restaurant/>
      <Banner
        title="Fast food, made fresh, right to your door"
        subtitle="Explore Our Menu"
        imageURL= {img}
      />
    </div>
  );
}

export default Main;
