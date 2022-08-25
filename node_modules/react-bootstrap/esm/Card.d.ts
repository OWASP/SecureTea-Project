import * as React from 'react';
import { BsPrefixProps, BsPrefixRefForwardingComponent } from './helpers';
import { Color, Variant } from './types';
export interface CardProps extends BsPrefixProps, React.HTMLAttributes<HTMLElement> {
    bg?: Variant;
    text?: Color;
    border?: Variant;
    body?: boolean;
}
declare const _default: BsPrefixRefForwardingComponent<"div", CardProps> & {
    Img: BsPrefixRefForwardingComponent<"img", import("./CardImg").CardImgProps>;
    Title: BsPrefixRefForwardingComponent<React.ForwardRefExoticComponent<Pick<React.DetailedHTMLProps<React.HTMLAttributes<HTMLDivElement>, HTMLDivElement>, "key" | keyof React.HTMLAttributes<HTMLDivElement>> & React.RefAttributes<HTMLDivElement>>, unknown>;
    Subtitle: BsPrefixRefForwardingComponent<React.ForwardRefExoticComponent<Pick<React.DetailedHTMLProps<React.HTMLAttributes<HTMLDivElement>, HTMLDivElement>, "key" | keyof React.HTMLAttributes<HTMLDivElement>> & React.RefAttributes<HTMLDivElement>>, unknown>;
    Body: BsPrefixRefForwardingComponent<"div", unknown>;
    Link: BsPrefixRefForwardingComponent<"a", unknown>;
    Text: BsPrefixRefForwardingComponent<"p", unknown>;
    Header: BsPrefixRefForwardingComponent<"div", import("./CardHeader").CardHeaderProps>;
    Footer: BsPrefixRefForwardingComponent<"div", unknown>;
    ImgOverlay: BsPrefixRefForwardingComponent<"div", unknown>;
};
export default _default;
