import React from "react";

import Cookies from 'universal-cookie';
import { Redirect } from "react-router-dom";

const cookies = new Cookies();

class Signin extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      url: '',
      isloggedin: false
    };
    
    this.handleNameChange;
    this.handleEmailChange;
    this.handleUrlChange;
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    console.log('A email was submitted: ' + this.state.username);
    console.log('A password was submitted: ' + this.state.password);
    console.log('A url was submitted: ' + this.state.url);

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        "username": this.state.username,
        "password": this.state.password
      })
    };

    fetch(
      this.state.url + "userlogin/", requestOptions
      )
        .then((res) => res.json())
        .then((json) => {
            this.setState({
              network_devices: json,
              DataisLoaded: true
            });
            console.log(json["cookie"]);
            cookies.remove("cookie");
            cookies.remove("url");
            cookies.set("cookie", json["cookie"]);
            cookies.set("url", this.state.url);
            this.state.isloggedin = true;
        })
    event.preventDefault();
  }

  handleNameChange = (event) => {
    this.setState({username: event.target.value});
  }

  handleEmailChange = (event) => {
    this.setState({password: event.target.value});
  }

  handleUrlChange = (event) => {
    this.setState({url: event.target.value});
  }

  render () {
    const { isloggedin } = this.state



    if (!isloggedin) {

      return (
        <>
          <main class="main-content  mt-0 signin-bg">
          <div class="page-header align-items-start min-vh-100">
            <span class="mask bg-gradient-dark opacity-6"></span>
            <div class="container my-auto pt-5">
              <div class="row mt-5">
                <div class="col-lg-6 col-md-8 col-12 mx-auto">
                  <div class="card z-index-0 fadeIn3 fadeInBottom">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                      <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                        <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Sign in</h4>
                      </div>
                    </div>
                    <div class="card-body">
                      <form role="form" class="text-start" onSubmit={this.handleSubmit}>
                        <div class="input-group input-group-outline my-2">
                          <input type="username" class="form-control" placeholder="Username" value={this.state.username} onChange={this.handleNameChange} />
                        </div>
                        <div class="input-group input-group-outline mb-2">
                          <input type="password" class="form-control" placeholder="Password" value={this.state.password} onChange={this.handleEmailChange} />
                        </div>
                        <div class="input-group input-group-outline mb-2">
                          <input type="url" class="form-control" placeholder="URL" value={this.state.url} onChange={this.handleUrlChange} />
                        </div>
                      
                        <div class="text-center signin-btn">
                          <button type="submit" class="text-white btn bg-gradient-info w-100 my-4 mb-2" value="Submit">Sign In</button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
              <div className="row mx-auto mt-5">
              <div className="col-lg-6 col-md-8 col-12 mx-auto">
              </div>
              </div>
            </div>
  
          </div>
        </main>
      </>
    );
  

      
    } else {

      return(
        <div>
          <h2> Logged In. Redirecting to Dashboard</h2>
          <meta http-equiv="refresh" content="0; url=http://127.0.0.1:3000/admin/dashboard" />

        </div>
        
      )
      
    }
    
  }

}

export default Signin;
