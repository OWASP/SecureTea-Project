import React from "react";

export default function Dashboard() {
    return(
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


            {/*
            <div id="dashboard-div1">
                <h1>Boom</h1>
            </div>
            <div id="dashboard-div2">
                <h1>Boom</h1>
            </div>
            <div id="dashboard-div3">
                <h1>Boom</h1>
            </div>
            <div id="dashboard-div4">
                <h1>Boom</h1>
            </div>
            */}
            
        </div>
    )
}