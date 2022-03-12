import React from "react";
import { Link } from "react-router-dom";

const Nav = ({routes}) => {

    const handLinkClick = (route) => {
        routes.map((_route) => {
            if (_route.name === route.name){
                routes.is_active = true
            }
        })
    }

    const home = routes[0]

    return (
      <header className="navbar navbar-expand-md navbar-light d-print-none">
        <div className="container-xl">
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar-menu">
            <span className="navbar-toggler-icon"></span>
          </button>
          {home &&
            <h1 className="navbar-brand navbar-brand-autodark d-none-navbar-horizontal pe-0 pe-md-3">
              <a href={home.path}>
              <img src={home.logo} width="158" height="40" alt="قطرب"
                   className="navbar-brand-image" />
              </a>
            </h1>
          }
          <div className="collapse navbar-collapse " id="navbar-menu">
              <div className="d-flex flex-column flex-md-row flex-fill align-items-stretch  align-items-md-center ">
                <ul className="navbar-nav ms-md-auto">
                    {routes && routes.map((route) => {
                        return (<li onClick={handLinkClick(route)} className={`nav-item ${route.is_active ? 'active' :''}`}>
                            <Link className="nav-link" to={route.path}>
                                <span className="nav-link-icon d-md-none d-lg-inline-block">
                                    {route.icon}
                                </span>
                                <span className="nav-link-title">
                                    {route.name}
                                </span>
                            </Link>
                        </li>);
                    })}
                </ul>
              </div>
            </div>
         </div>
      </header>
   )
}

export default Nav