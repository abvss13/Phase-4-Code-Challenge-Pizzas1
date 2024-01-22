// properties
const Header = ({ restaurantName, menuItems }) => (
    <header>
      <div class="logo">{restaurantName}</div>
      <nav>
        <div class="menu">
          {menuItems?.map((menuItem) => (
            <p>
              <a
                class={menuItem.type === "button" && "order-button"}
                href={menuItem.link}
              >
                {menuItem.name}
              </a>
            </p>
          ))}
        </div>
      </nav>
    </header>
  );
  
  export default Header;
  