import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, useRoutes } from "react-router-dom";

import Nav from "../components/nav/nav"
import Home from "../pages/home/home"
import Doc from "../pages/doc/doc"

import Logo from "../../assets/image/logo.jpg"
import "./entry.css";



const App = () => {
    let routes = [
      {
			path: "/",
			element: <Home />,
			icon: (<svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
						viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
						stroke-linecap="round" stroke-linejoin="round">
						<path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
						<polyline points="5 12 3 12 12 3 21 12 19 12"></polyline>
						<path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7"></path>
						<path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6"></path>
	  				</svg>),
			logo: Logo,
			name: "الرئيسية"
      },
		{
			path: "/doc",
			element: <Doc />,
			icon: (<svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
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
					</svg>),
			name:"توثيق"
      }
    ];
	let elements = useRoutes(routes)
	return(
		<>
			<Nav routes={routes}  />
			{elements}
		</>
	);

}

const Index = () => {
  return(
    <div className="App">
		<BrowserRouter>
			<App/>
		</BrowserRouter>
    </div>
  );
}



ReactDOM.render(<Index />, document.getElementById("root"));