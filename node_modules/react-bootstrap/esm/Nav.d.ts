import { NavProps as BaseNavProps } from '@restart/ui/Nav';
import { EventKey } from '@restart/ui/types';
import { BsPrefixProps, BsPrefixRefForwardingComponent } from './helpers';
export interface NavProps extends BsPrefixProps, BaseNavProps {
    navbarBsPrefix?: string;
    cardHeaderBsPrefix?: string;
    variant?: 'tabs' | 'pills';
    defaultActiveKey?: EventKey;
    fill?: boolean;
    justify?: boolean;
    navbar?: boolean;
    navbarScroll?: boolean;
}
declare const _default: BsPrefixRefForwardingComponent<"div", NavProps> & {
    Item: BsPrefixRefForwardingComponent<"div", unknown>;
    Link: BsPrefixRefForwardingComponent<"a", import("./NavLink").NavLinkProps>;
};
export default _default;
