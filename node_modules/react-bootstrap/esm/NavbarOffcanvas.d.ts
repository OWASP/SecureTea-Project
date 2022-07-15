import * as React from 'react';
import { OffcanvasProps } from './Offcanvas';
export declare type NavbarOffcanvasProps = Omit<OffcanvasProps, 'show'>;
declare const NavbarOffcanvas: React.ForwardRefExoticComponent<Pick<NavbarOffcanvasProps, keyof OffcanvasProps> & React.RefAttributes<HTMLDivElement>>;
export default NavbarOffcanvas;
