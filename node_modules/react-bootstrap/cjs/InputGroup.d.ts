import * as React from 'react';
import { BsPrefixProps, BsPrefixRefForwardingComponent } from './helpers';
export interface InputGroupProps extends BsPrefixProps, React.HTMLAttributes<HTMLElement> {
    size?: 'sm' | 'lg';
    hasValidation?: boolean;
}
declare const _default: BsPrefixRefForwardingComponent<"div", InputGroupProps> & {
    Text: BsPrefixRefForwardingComponent<"span", unknown>;
    Radio: (props: any) => JSX.Element;
    Checkbox: (props: any) => JSX.Element;
};
export default _default;
