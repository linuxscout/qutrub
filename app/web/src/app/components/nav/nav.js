import React from "react";

const Nav = ({home, routes}) => {

    const  handLinkClick = (route) => {
        routes.map((_route) => {
            if (_route.name === route.name){
                routes.is_active = true
            }
        })
    }

   return (
      <header className="navbar navbar-expand-md navbar-light d-print-none">
        <div className="container-xl">
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar-menu">
            <span className="navbar-toggler-icon"></span>
          </button>
          {home &&
            <h1 className="navbar-brand navbar-brand-autodark d-none-navbar-horizontal pe-0 pe-md-3">
              <a href={home.path}>
                {home.icon}
              <img src="{{ url_for('static', filename='images/logo.jpg')}}" width="158" height="40" alt="قطرب"
                    className="navbar-brand-image" />
              </a>
            </h1>
          }
          <div className="collapse navbar-collapse " id="navbar-menu">
              <div className="d-flex flex-column flex-md-row flex-fill align-items-stretch  align-items-md-center ">
                <ul className="navbar-nav ms-md-auto">
                  {routes && routes.map((route) => {
                      <li  onClick={handLinkClick(route)} className={`nav-item ${route.is_active ? 'active' :''}`}>
                      <a className="nav-link " href={route.path}>
                          <span className="nav-link-icon d-md-none d-lg-inline-block">
                              {route.icon}
                          </span>
                          <span className="nav-link-title ">
                              {route.name}
                            </span>
                      </a>
                  </li>
                  } )}

                      <li className="nav-item {% if current_page == 'home' %}active {% endif %}">
                          <a className="nav-link " href="{{ url_for('home')}} ">
                              <span className="nav-link-icon d-md-none d-lg-inline-block">
                                  <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
                                      viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                      stroke-linecap="round" stroke-linejoin="round">
                                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                      <polyline points="5 12 3 12 12 3 21 12 19 12"></polyline>
                                      <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7"></path>
                                      <path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6"></path>
                                  </svg>
                              </span>
                              <span className="nav-link-title ">
                                  الرئيسية
                              </span>
                          </a>
                      </li>
                      <li className="nav-item {% if current_page == 'doc' %}active {% endif %}">
                          <a className="nav-link" href="{{ url_for('doc')}}">
                              <span className="nav-link-icon d-md-none d-lg-inline-block">
                                  <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
                                      viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                      stroke-linecap="round" stroke-linejoin="round">
                                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                      <path d="M14 3v4a1 1 0 0 0 1 1h4"></path>
                                      <path
                                          d="M17 21h-10a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2z">
                                      </path>
                                      <line x1="9" y1="9" x2="10" y2="9"></line>
                                      <line x1="9" y1="13" x2="15" y2="13"></line>
                                      <line x1="9" y1="17" x2="15" y2="17"></line>
                                  </svg>
                              </span>
                              <span className="nav-link-title">
                                  توثيق
                              </span>
                          </a>
                      </li>
                      <li className="nav-item {% if current_page == 'download' %}active {% endif %} ">
                          <a className="nav-link " href="{{url_for('download')}}">
                              <span className="nav-link-icon d-md-none d-lg-inline-block">
                                  <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
                                      viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                      stroke-linecap="round" stroke-linejoin="round">
                                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                      <path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2"></path>
                                      <polyline points="7 11 12 16 17 11"></polyline>
                                      <line x1="12" y1="4" x2="12" y2="16"></line>
                                  </svg>
                              </span>
                              <span className="nav-link-title ">
                                  تحميل
                              </span>
                          </a>
                      </li>
                      <li className="nav-item {% if current_page == 'projects' %}active {% endif %} ">
                          <a className="nav-link " href="{{url_for('projects')}}">
                              <span className="nav-link-icon d-md-none d-lg-inline-block">
                                  <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
                                      viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                      stroke-linecap="round" stroke-linejoin="round">
                                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                      <polyline points="12 3 20 7.5 20 16.5 12 21 4 16.5 4 7.5 12 3"></polyline>
                                      <line x1="12" y1="12" x2="20" y2="7.5"></line>
                                      <line x1="12" y1="12" x2="12" y2="21"></line>
                                      <line x1="12" y1="12" x2="4" y2="7.5"></line>
                                  </svg>
                              </span>
                              <span className="nav-link-title ">
                                  مشاريع
                              </span>
                          </a>
                      </li>
                      <li className="nav-item {% if current_page == 'contact' %}active {% endif %}">
                          <a className="nav-link " href="{{url_for('contact')}}">
                              <span className="nav-link-icon d-md-none d-lg-inline-block">
                                  <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
                                      viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                      stroke-linecap="round" stroke-linejoin="round">
                                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                      <path
                                          d="M12 20l-3 -3h-2a3 3 0 0 1 -3 -3v-6a3 3 0 0 1 3 -3h10a3 3 0 0 1 3 3v6a3 3 0 0 1 -3 3h-2l-3 3">
                                      </path>
                                      <line x1="8" y1="9" x2="16" y2="9"></line>
                                      <line x1="8" y1="13" x2="14" y2="13"></line>
                                  </svg>
                              </span>
                              <span className="nav-link-title ">
                                  اتصل بنا
                          </span>
                      </a>
                    </li>
                </ul>
              </div>
            </div>
         </div>
      </header>
   )
}

export default Nav