import * as React from 'react';
import { TransitionComponent } from '@restart/ui/types';
import { BsPrefixProps, BsPrefixRefForwardingComponent } from './helpers';
import { Variant } from './types';
export interface ToastProps extends BsPrefixProps, React.HTMLAttributes<HTMLElement> {
    animation?: boolean;
    autohide?: boolean;
    delay?: number;
    onClose?: (e?: React.MouseEvent | React.KeyboardEvent) => void;
    show?: boolean;
    transition?: TransitionComponent;
    bg?: Variant;
}
declare const _default: BsPrefixRefForwardingComponent<"div", ToastProps> & {
    Body: BsPrefixRefForwardingComponent<"div", unknown>;
    Header: React.ForwardRefExoticComponent<import("./ToastHeader").ToastHeaderProps & React.RefAttributes<HTMLDivElement>>;
};
export default _default;
