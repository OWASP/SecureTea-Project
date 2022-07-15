import * as React from 'react';
import { DropdownProps as BaseDropdownProps } from '@restart/ui/Dropdown';
import { DropDirection } from './DropdownContext';
import { BsPrefixProps, BsPrefixRefForwardingComponent } from './helpers';
import { AlignType } from './types';
export interface DropdownProps extends BaseDropdownProps, BsPrefixProps, Omit<React.HTMLAttributes<HTMLElement>, 'onSelect' | 'children'> {
    drop?: DropDirection;
    align?: AlignType;
    flip?: boolean;
    focusFirstItemOnShow?: boolean | 'keyboard';
    navbar?: boolean;
    autoClose?: boolean | 'outside' | 'inside';
}
declare const _default: BsPrefixRefForwardingComponent<"div", DropdownProps> & {
    Toggle: BsPrefixRefForwardingComponent<"button", import("./DropdownToggle").DropdownToggleProps>;
    Menu: BsPrefixRefForwardingComponent<"div", import("./DropdownMenu").DropdownMenuProps>;
    Item: BsPrefixRefForwardingComponent<import("@restart/ui/esm/types").DynamicRefForwardingComponent<React.ForwardRefExoticComponent<import("@restart/ui/esm/Button").ButtonProps & React.RefAttributes<HTMLElement>>, import("@restart/ui/Dropdown").DropdownItemProps>, import("./DropdownItem").DropdownItemProps>;
    ItemText: BsPrefixRefForwardingComponent<"span", unknown>;
    Divider: BsPrefixRefForwardingComponent<"hr", unknown>;
    Header: BsPrefixRefForwardingComponent<"div", unknown>;
};
export default _default;
