import React from "react";
import Dashboard from "./components/Dashboard";
import Navbar from "./components/Navbar";

export default function App() {
    return(
        <div className="container">
            <h1>Boom</h1>
            <Navbar />
            <Dashboard />
        </div>
    )
}