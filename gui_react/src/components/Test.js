import React from "react";
import Cookies from "universal-cookie";

const browser_cookies = new Cookies();

class Test extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
    }

    // http://127.0.0.1:8000/

    // https://jsonplaceholder.typicode.com/users/1

    componentDidMount() {
        fetch('http://127.0.0.1:8000/')
        .then((res) => res.json())
        .then(json => {
            this.setState({
                isLoaded: true,
                item: json, 
            })
        });

    }

    render() {

        browser_cookies.set("id", "testid", { path: '/' });

        var {isLoaded, item} = this.state;

        if (!isLoaded) {
            return <div>Loading Data ... </div>
        }

        else{
            return (
                <div className="App">
                    <h1>{item.status} </h1>
                </div>
            )
        }

        
    }
}

export default Test;
