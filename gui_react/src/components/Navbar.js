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
                    <i class="fas fa-tachometer-alt fa-fw me-3"></i><span>Main dashboard</span>
                    </a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple active">
                    <i class="fas fa-chart-area fa-fw me-3"></i><span>Webiste traffic</span>
                    </a>
                    <a href="#test" class="list-group-item list-group-item-action py-2 ripple"
                    ><i class="fas fa-lock fa-fw me-3"></i><span>Password</span></a>
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
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDarkDropdown" aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNavDarkDropdown">
                        <ul class="navbar-nav">
                            <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Dropdown
                            </a>
                            <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDarkDropdownMenuLink">
                                <li><a class="dropdown-item" href="#">Action</a></li>
                                <li><a class="dropdown-item" href="#">Another action</a></li>
                                <li><a class="dropdown-item" href="#">Something else here</a></li>
                            </ul>
                            </li>
                        </ul>
                        </div>
                    </div>

                    {/*<!-- Icon -->*/}
                    <li class="nav-item">
                    <a class="nav-link me-3 me-lg-0" href="#test">
                        <i class="fas fa-fill-drip"></i>
                    </a>
                    </li>
                    {/*<!-- Icon -->*/}
                    <li class="nav-item me-3 me-lg-0">
                    <a class="nav-link" href="#test">
                        <i class="fab fa-github"></i>
                    </a>
                    </li>

                    {/*<!-- Icon dropdown -->*/}
                    <li class="nav-item dropdown">
                    <a
                        class="nav-link me-3 me-lg-0 dropdown-toggle hidden-arrow"
                        href="#test"
                        id="navbarDropdown"
                        role="button"
                        data-mdb-toggle="dropdown"
                        aria-expanded="false"
                    >
                        <i class="flag-united-kingdom flag m-0"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                        <li>
                        <a class="dropdown-item" href="#test"
                            ><i class="flag-united-kingdom flag"></i>English
                            <i class="fa fa-check text-success ms-2"></i>
                        </a>
                        </li>
                        <li><hr class="dropdown-divider" /></li>
                        <li>
                        <a class="dropdown-item" href="#test"><i class="flag-poland flag"></i>Polski</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test"><i class="flag-china flag"></i>中文</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test"><i class="flag-japan flag"></i>日本語</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test"><i class="flag-germany flag"></i>Deutsch</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test"><i class="flag-france flag"></i>Français</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test"><i class="flag-spain flag"></i>Español</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test"><i class="flag-russia flag"></i>Русский</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test"><i class="flag-portugal flag"></i>Português</a>
                        </li>
                    </ul>
                    </li>

                    {/*<!-- Avatar -->*/}
                    <li class="nav-item dropdown">
                    <a
                        class="nav-link dropdown-toggle hidden-arrow d-flex align-items-center"
                        href="#test"
                        id="navbarDropdownMenuLink"
                        role="button"
                        data-mdb-toggle="dropdown"
                        aria-expanded="false"
                    >
                        <img
                        src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (31).webp"
                        class="rounded-circle"
                        height="22"
                        alt="Avatar"
                        loading="lazy"
                        />
                    </a>
                    <ul
                        class="dropdown-menu dropdown-menu-end"
                        aria-labelledby="navbarDropdownMenuLink"
                    >
                        <li>
                        <a class="dropdown-item" href="#test">My profile</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test">Settings</a>
                        </li>
                        <li>
                        <a class="dropdown-item" href="#test">Logout</a>
                        </li>
                    </ul>
                    </li>
                </ul>
                </div>
                {/*<!-- Container wrapper -->*/}
            </nav>
        </div>
    )
}