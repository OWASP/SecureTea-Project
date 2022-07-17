import React from "react"

export default function MainNavbar(){
    return(
        <div class="mainnavbar">
            <nav id="main-navbar" class="navbar navbar-expand-lg navbar-light bg-white fixed-top">

                <div class="container-fluid">

                <button class="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#sidebarMenu"
                aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
                <i class="fas fa-bars"></i>
                </button>

                {/* <!-- Brand --> */}
                <a class="navbar-brand" href="#test">
                <img src="https://owasp.org/assets/images/logo.png" height="50" alt="OWASP Logo"
                    loading="lazy" />
                </a>
                {/* <!-- Search form --> */}
                <form class="d-none d-md-flex input-group w-auto my-auto">
                <input autocomplete="on" type="search" class="form-control rounded"
                    placeholder='Search (ctrl + "/" to focus)' style={{ 'min-width':`225px` }} />
                <span class="input-group-text border-0"><i class="fas fa-search"></i></span>
                </form>

                {/* <!-- Right links --> */}
                <ul class="navbar-nav ms-auto d-flex flex-row">
                {/* <!-- Notification dropdown --> */}
                <li class="nav-item dropdown">
                    <a class="nav-link me-3 me-lg-0 dropdown-toggle hidden-arrow" href="#test" id="navbarDropdownMenuLink"
                    role="button" data-mdb-toggle="dropdown" aria-expanded="false">
                        <i class="fas fa-bell"></i>
                        <span class="badge rounded-pill badge-notification bg-danger">1</span>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownMenuLink">
                        <li><a class="dropdown-item" href="#test">Some news</a></li>
                        <li><a class="dropdown-item" href="#test">Another news</a></li>
                        <li><a class="dropdown-item" href="#test">Something else here</a></li>
                    </ul>
                </li>

                {/* <!-- Icon --> */}
                <li class="nav-item">
                    <a class="nav-link me-3 me-lg-0" href="#test">
                    <i class="fas fa-fill-drip"></i>
                    </a>
                </li>
                {/* <!-- Icon --> */}
                <li class="nav-item me-3 me-lg-0">
                    <a class="nav-link" href="#test">
                    <i class="fab fa-github"></i>
                    </a>
                </li>

                {/*<!-- Avatar --> */}
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle hidden-arrow d-flex align-items-center" href="#test"
                    id="navbarDropdownMenuLink" role="button" data-mdb-toggle="dropdown" aria-expanded="false">
                    <img src="https://owasp.org/assets/images/logo.png" class="rounded-circle"
                    height="22" alt="Avatar" loading="lazy" />
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownMenuLink">
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
                {/* <!-- Container wrapper --> */}
            </nav>
        </div>
    )
}