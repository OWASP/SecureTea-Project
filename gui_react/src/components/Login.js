import React from "react";
import Cookies from "universal-cookie";

const browser_cookies = new Cookies();

class Login extends React.Component {
    render() {
        var id_cookie = browser_cookies.get("id");
        console.log(id_cookie)
        return(
            <h1>Login.js</h1>
        )
    }
}

export default Login;