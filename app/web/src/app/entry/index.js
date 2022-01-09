import React from "react";
import ReactDOM from "react-dom";

import Nav from "../components/nav/nav"
import Home from "../pages/home/home"
import "./entry.css";



const App = () => {

  return(
    <>
    <Nav />
    <Home />
    </>
  );

}


const Index = () => {
  return(
    <div className="App">
      <App/>
    </div>
  );
}



ReactDOM.render(<Index />, document.getElementById("root"));