import PropTypes from 'prop-types';
export declare type Variant = 'primary' | 'secondary' | 'success' | 'danger' | 'warning' | 'info' | 'dark' | 'light' | string;
export declare type ButtonVariant = Variant | 'link' | 'outline-primary' | 'outline-secondary' | 'outline-success' | 'outline-danger' | 'outline-warning' | 'outline-info' | 'outline-dark' | 'outline-light';
export declare type Color = 'primary' | 'secondary' | 'success' | 'danger' | 'warning' | 'info' | 'dark' | 'light' | 'white' | 'muted';
export declare type Placement = import('@restart/ui/usePopper').Placement;
export declare type AlignDirection = 'start' | 'end';
export declare type ResponsiveAlignProp = {
    sm: AlignDirection;
} | {
    md: AlignDirection;
} | {
    lg: AlignDirection;
} | {
    xl: AlignDirection;
} | {
    xxl: AlignDirection;
} | Record<string, AlignDirection>;
export declare type AlignType = AlignDirection | ResponsiveAlignProp;
export declare const alignPropType: PropTypes.Requireable<object | AlignDirection>;
export declare type RootCloseEvent = 'click' | 'mousedown';
export declare type GapValue = 0 | 1 | 2 | 3 | 4 | 5;
