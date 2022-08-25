import React from "react";

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
        .then(res => {
            this.setState({
                isLoaded: true,
                items: res, 
            })
        });

    }

    render() {

        var {isLoaded, items} = this.state;

        if (!isLoaded) {
            return <div>Loading Data ... </div>
        }

        else{
            return (
                <div className="App">
                    Data has been delivered


                </div>
            )
        }

        
    }
}

export default Test;
