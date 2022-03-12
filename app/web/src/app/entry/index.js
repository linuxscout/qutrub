import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, useRoutes } from "react-router-dom";

import Nav from "../components/nav/nav"
import Home from "../pages/home/home"
import Doc from "../pages/doc/doc"
import Download from "../pages/download/download";
import Projects from "../pages/projects/projects";
import Contact from "../pages/contact/contact";

import Logo from "../../assets/image/logo.jpg"
import "./entry.css";

import * as serviceWorker from './serviceWorker';



const App = () => {
    let routes = [
      {
			path: "/",
			element: <Home />,
			icon: (<svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
						viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none"
						strokeLinecap="round" strokeLinejoin="round">
						<path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
						<polyline points="5 12 3 12 12 3 21 12 19 12"></polyline>
						<path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7"></path>
						<path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6"></path>
	  				</svg>),
			logo: Logo,
			name: "الرئيسية"
      },{
			path: "/doc",
			element: <Doc />,
			icon: (<svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
						viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none"
						strokeLinecap="round" strokeLinejoin="round">
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
      },{
			path: "/download",
			element: <Download />,
			icon: (<svg
						xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
						viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none"
						strokeLinecap="round" strokeLinejoin="round"
					 >
						<path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
						<path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2"></path>
						<polyline points="7 11 12 16 17 11"></polyline>
						<line x1="12" y1="4" x2="12" y2="16"></line>
	  				 </svg>),
			name:"تحميل"
      },{
			path: "/projects",
			element: <Projects />,
			icon: (
				<svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
				viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none"
				strokeLinecap="round" strokeLinejoin="round">
				<path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
				<polyline points="12 3 20 7.5 20 16.5 12 21 4 16.5 4 7.5 12 3"></polyline>
				<line x1="12" y1="12" x2="20" y2="7.5"></line>
				<line x1="12" y1="12" x2="12" y2="21"></line>
				<line x1="12" y1="12" x2="4" y2="7.5"></line>
				</svg>
			),
			name:"مشاريع"
		},{
			path: "/contact",
			element: <Contact />,
			icon: (
				<svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
				viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none"
				strokeLinecap="round" strokeLinejoin="round">
				<path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
				<path
					d="M12 20l-3 -3h-2a3 3 0 0 1 -3 -3v-6a3 3 0 0 1 3 -3h10a3 3 0 0 1 3 3v6a3 3 0 0 1 -3 3h-2l-3 3">
				</path>
				<line x1="8" y1="9" x2="16" y2="9"></line>
				<line x1="8" y1="13" x2="14" y2="13"></line>
				</svg>
			),
			name:"اتصل بنا"
		},
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

serviceWorker.register();