import * as React from 'react';
import { ModalProps as BaseModalProps } from '@restart/ui/Modal';
import { BsPrefixRefForwardingComponent } from './helpers';
export declare type OffcanvasPlacement = 'start' | 'end' | 'top' | 'bottom';
export interface OffcanvasProps extends Omit<BaseModalProps, 'role' | 'renderBackdrop' | 'renderDialog' | 'transition' | 'backdrop' | 'backdropTransition'> {
    bsPrefix?: string;
    backdropClassName?: string;
    scroll?: boolean;
    placement?: OffcanvasPlacement;
}
declare const _default: BsPrefixRefForwardingComponent<"div", OffcanvasProps> & {
    Body: BsPrefixRefForwardingComponent<"div", unknown>;
    Header: React.ForwardRefExoticComponent<import("./OffcanvasHeader").OffcanvasHeaderProps & React.RefAttributes<HTMLDivElement>>;
    Title: BsPrefixRefForwardingComponent<React.ForwardRefExoticComponent<Pick<React.DetailedHTMLProps<React.HTMLAttributes<HTMLDivElement>, HTMLDivElement>, "key" | keyof React.HTMLAttributes<HTMLDivElement>> & React.RefAttributes<HTMLDivElement>>, unknown>;
};
export default _default;
