import React from "react";
import Dashboard from "./components/Dashboard";
import Navbar from "./components/Navbar";
import Test from "./components/Test";
import Login from "./components/Login";

import Cookies from "universal-cookie";

// const browser_cookies = new Cookies();

class App extends React.Component {

    render() {
        
        //var id_cookie = browser_cookies.get("id");
        //console.log(id_cookie);

        if (true) {
            return(
                <div>
                    <Navbar />
                    <Login />
                </div>
            )
        }
    }

}

export default App;
