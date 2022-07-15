import * as React from 'react';
import { DropdownProps } from './Dropdown';
import { DropdownMenuVariant } from './DropdownMenu';
import { BsPrefixRefForwardingComponent } from './helpers';
export interface NavDropdownProps extends Omit<DropdownProps, 'title'> {
    title: React.ReactNode;
    disabled?: boolean;
    active?: boolean;
    menuRole?: string;
    renderMenuOnMount?: boolean;
    rootCloseEvent?: 'click' | 'mousedown';
    menuVariant?: DropdownMenuVariant;
}
declare const _default: BsPrefixRefForwardingComponent<"div", NavDropdownProps> & {
    Item: BsPrefixRefForwardingComponent<import("@restart/ui/esm/types").DynamicRefForwardingComponent<React.ForwardRefExoticComponent<import("@restart/ui/esm/Button").ButtonProps & React.RefAttributes<HTMLElement>>, import("@restart/ui/esm/DropdownItem").DropdownItemProps>, import("./DropdownItem").DropdownItemProps>;
    ItemText: BsPrefixRefForwardingComponent<"span", unknown>;
    Divider: BsPrefixRefForwardingComponent<"hr", unknown>;
    Header: BsPrefixRefForwardingComponent<"div", unknown>;
};
export default _default;
