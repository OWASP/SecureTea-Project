import * as React from 'react';
export declare type ButtonType = 'button' | 'reset' | 'submit';
export interface AnchorOptions {
    href?: string;
    rel?: string;
    target?: string;
}
export interface UseButtonPropsOptions extends AnchorOptions {
    type?: ButtonType;
    disabled?: boolean;
    onClick?: React.EventHandler<React.MouseEvent | React.KeyboardEvent>;
    tabIndex?: number;
    tagName?: keyof JSX.IntrinsicElements;
}
export declare function isTrivialHref(href?: string): boolean;
export interface AriaButtonProps {
    type?: ButtonType | undefined;
    disabled: boolean | undefined;
    role?: 'button';
    tabIndex?: number | undefined;
    href?: string | undefined;
    target?: string | undefined;
    rel?: string | undefined;
    'aria-disabled'?: true | undefined;
    onClick?: (event: React.MouseEvent | React.KeyboardEvent) => void;
    onKeyDown?: (event: React.KeyboardEvent) => void;
}
export interface UseButtonPropsMetadata {
    tagName: React.ElementType;
}
export declare function useButtonProps({ tagName, disabled, href, target, rel, onClick, tabIndex, type, }: UseButtonPropsOptions): [AriaButtonProps, UseButtonPropsMetadata];
export interface BaseButtonProps {
    /**
     * Control the underlying rendered element directly by passing in a valid
     * component type
     */
    as?: keyof JSX.IntrinsicElements | undefined;
    /** The disabled state of the button */
    disabled?: boolean | undefined;
    /** Optionally specify an href to render a `<a>` tag styled as a button */
    href?: string | undefined;
    /** Anchor target, when rendering an anchor as a button */
    target?: string | undefined;
    rel?: string | undefined;
}
export interface ButtonProps extends BaseButtonProps, React.ComponentPropsWithoutRef<'button'> {
}
declare const Button: React.ForwardRefExoticComponent<ButtonProps & React.RefAttributes<HTMLElement>>;
export default Button;
