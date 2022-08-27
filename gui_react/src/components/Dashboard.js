import React from "react";

class Dashboard extends React.Component {

	// Constructor
	constructor(props) {
		super(props);

		this.state = {
			items: [],
			DataisLoaded: false
		};
	}

	// ComponentDidMount is used to
	// execute the code
	componentDidMount() {
		fetch("http://127.0.0.1:8000/")
			.then((res) => res.json())
			.then((json) => {
				this.setState({
					item: json,
					DataisLoaded: true
				});
			})
	}
	render() {
		const { DataisLoaded, item } = this.state;
		if (!DataisLoaded) return <div>
			<h1 id='dashboard-main'> Please wait for some time </h1> </div> ;

		return (
		<div className = "Dashboard">
            {
                <div class='dashboard-main' id='dashboard-main'>
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-3">
                                <div class="card p-3">
                                    <div class="row no-gutters">
                                        <div class="col-md-4">
                                            <img src="img/cpu.png" class="card-img" alt="..." />
                                        </div>
                                        <div class="col-md-8">
                                            <div class="card-body">
                                            <h5 class="card-title"> {item.status} </h5>
                                                </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card p-3">
                                    <div class="row no-gutters">
                                        <div class="col-md-4">
                                            <img src="img/ram.png" class="card-img" alt="..." />
                                        </div>
                                        <div class="col-md-8">
                                            <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                                </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card p-3">
                                    <div class="row no-gutters">
                                        <div class="col-md-4">
                                            <img src="img/swap.png" class="card-img" alt="..." />
                                        </div>
                                        <div class="col-md-8">
                                            <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                                </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card p-3">
                                    <div class="row no-gutters">
                                        <div class="col-md-4">
                                            <img src="img/clock.png" class="card-img" alt="..." />
                                        </div>
                                        <div class="col-md-8">
                                            <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                                </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            }

		</div>
	);
}
}

export default Dashboard;
