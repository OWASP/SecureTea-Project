import React from "react";
import Dashboard from "./components/Dashboard";
import Navbar from "./components/Navbar";
import Test from "./components/Test";


export default function App() {
    return(
        <div className="container">
            <h1>Boom</h1>
            <Navbar />
            <br /><br />
            <Test />
        </div>
    )
}