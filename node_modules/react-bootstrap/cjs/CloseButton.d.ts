import * as React from 'react';
export declare type CloseButtonVariant = 'white';
export interface CloseButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: CloseButtonVariant;
}
declare const CloseButton: React.ForwardRefExoticComponent<CloseButtonProps & React.RefAttributes<HTMLButtonElement>>;
export default CloseButton;
