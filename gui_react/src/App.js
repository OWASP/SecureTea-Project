import React from "react";
import SideNavbar from "./components/SideNavbar";
import MainNavbar from "./components/MainNavbar";

export default function App() {
    return(
        <div className="container">
            <h1>Boom</h1>
            <SideNavbar />
            <MainNavbar />
        </div>
    )
}