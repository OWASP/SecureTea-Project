import React from "react";

export default function Navbar() {
    return(
        <div class='full-navbar'>
            {/*<!-- Sidebar -->*/}
            <nav id="sidebarMenu" class="collapse d-lg-block sidebar collapse bg-white">
                <div class="position-sticky">
                <div class="list-group list-group-flush mx-3 mt-4">
                    <a
                    href="#test"
                    class="list-group-item list-group-item-action py-2 ripple"
                    aria-current="true"
                    >
                    <i class="fas fa-tachometer-alt fa-fw me-3"></i><span>Dashboard</span>
                    </a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-lock fa-fw me-3"></i><span>Storage</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-lock fa-fw me-3"></i><span>Processes</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-lock fa-fw me-3"></i><span>Last Login</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-lock fa-fw me-3"></i><span>Processes</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-lock fa-fw me-3"></i><span>Nettwork</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-lock fa-fw me-3"></i><span>Security</span></a>
                    

                    {/*}
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-chart-line fa-fw me-3"></i><span>Analytics</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple">
                    <i class="fas fa-chart-pie fa-fw me-3"></i><span>SEO</span>
                    </a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-chart-bar fa-fw me-3"></i><span>Orders</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-globe fa-fw me-3"></i><span>International</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-building fa-fw me-3"></i><span>Partners</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-calendar fa-fw me-3"></i><span>Calendar</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-users fa-fw me-3"></i><span>Users</span></a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-money-bill fa-fw me-3"></i><span>Sales</span></a>
                    */}

                </div>
                </div>
            </nav>
            {/*<!-- Sidebar -->*/}

            {/*<!-- Navbar -->*/}
            <nav id="main-navbar" class="navbar navbar-expand-lg navbar-light bg-white fixed-top">
                {/*<!-- Container wrapper -->*/}
                <div class="container-fluid">
                {/*<!-- Toggle button -->*/}
                <button
                    class="navbar-toggler"
                    type="button"
                    data-mdb-toggle="collapse"
                    data-mdb-target="#testsidebarMenu"
                    aria-controls="sidebarMenu"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <i class="fas fa-bars"></i>
                </button>

                {/*<!-- Brand -->*/}
                <a class="navbar-brand" href="#test">
                    <img
                    src="https://owasp.org/assets/images/logo.png"
                    height="50"
                    alt="OWASP Logo"
                    loading="lazy"
                    />
                </a>
                {/*<!-- Search form -->*/}
                <form class="d-none d-md-flex input-group w-auto my-auto">
                    <input
                    autocomplete="off"
                    type="search"
                    class="form-control rounded"
                    placeholder='Search (ctrl + "/" to focus)'
                    style={{"min-width": "225px"}}
                    />
                    <span class="input-group-text border-0"><i class="fas fa-search"></i></span>
                </form>

                {/*<!-- Right links -->*/}
                <ul class="navbar-nav ms-auto d-flex flex-row">
                    {/*<!-- Notification dropdown -->*/}
                    <div class="container-fluid">
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#testnavbarNavDarkDropdown" aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNavDarkDropdown">
                        <ul class="navbar-nav">
                            <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#test" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Notifications
                            </a>
                            <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDarkDropdownMenuLink">
                                <li><a class="dropdown-item" href="#test">List</a></li>
                                <li><a class="dropdown-item" href="#test">Of</a></li>
                                <li><a class="dropdown-item" href="#test">Notifications</a></li>
                            </ul>
                            </li>
                        </ul>
                        </div>
                    </div>

                    {/*<!-- Profile dropdown -->*/}
                    <div class="container-fluid">
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#testnavbarNavDarkDropdown" aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNavDarkDropdown">
                        <ul class="navbar-nav">
                            <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#test" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <img src="https://picsum.photos/50" class="profile-photo" alt="profile" />
                            </a>
                            <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarProfileDarkDropdownMenuLink">
                                <li><a class="dropdown-item" href="#test">Logout</a></li>
                                <li><a class="dropdown-item" href="#test">Reset password</a></li>
                            </ul>
                            </li>
                        </ul>
                        </div>
                    </div>
                </ul>
                </div>
                {/*<!-- Container wrapper -->*/}
            </nav>
        </div>
    )
}