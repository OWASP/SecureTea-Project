import * as React from 'react';
import { SelectCallback } from '@restart/ui/types';
import { BsPrefixProps, BsPrefixRefForwardingComponent } from './helpers';
export interface NavbarProps extends BsPrefixProps, Omit<React.HTMLAttributes<HTMLElement>, 'onSelect'> {
    variant?: 'light' | 'dark';
    expand?: boolean | string | 'sm' | 'md' | 'lg' | 'xl' | 'xxl';
    bg?: string;
    fixed?: 'top' | 'bottom';
    sticky?: 'top';
    onToggle?: (expanded: boolean) => void;
    onSelect?: SelectCallback;
    collapseOnSelect?: boolean;
    expanded?: boolean;
}
declare const _default: BsPrefixRefForwardingComponent<"nav", NavbarProps> & {
    Brand: BsPrefixRefForwardingComponent<"a", import("./NavbarBrand").NavbarBrandProps>;
    Collapse: React.ForwardRefExoticComponent<import("./NavbarCollapse").NavbarCollapseProps & React.RefAttributes<HTMLDivElement>>;
    Offcanvas: React.ForwardRefExoticComponent<Pick<import("./NavbarOffcanvas").NavbarOffcanvasProps, keyof import("./Offcanvas").OffcanvasProps> & React.RefAttributes<HTMLDivElement>>;
    Text: BsPrefixRefForwardingComponent<"span", unknown>;
    Toggle: BsPrefixRefForwardingComponent<"button", import("./NavbarToggle").NavbarToggleProps>;
};
export default _default;
