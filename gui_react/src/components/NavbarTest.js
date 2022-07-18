import React from "react";

export default function Navbartest() {
    return(
        <div class="navbar-test">
            <nav
                id="sidebarMenu"
                class="collapse d-lg-block sidebar collapse bg-white"
                >

                <div class="position-sticky">
                    <div class="list-group list-group-flush mx-3 mt-4">
                        <a
                        href="#test"
                        class="list-group-item list-group-item-action py-2 ripple"
                        aria-current="true"
                        >
                        <i class="fas fa-tachometer-alt fa-fw me-3"></i>
                            <span>Main dashboard</span>
                        </a>
                    </div>
                </div>
            </nav>
        </div>
    )
}

