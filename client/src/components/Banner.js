
const Banner = ({ title, subtitle, imageURL }) => (
    <section class="banner">
      <div class="content">
        <h1>{title}</h1>
        <span class="call-to-action">
          {subtitle} <i class="fas fa-long-arrow-alt-right"></i>
        </span>
      </div>
      <img src={imageURL} alt="pizza" />
    </section>
  );
  
  export default Banner;
  