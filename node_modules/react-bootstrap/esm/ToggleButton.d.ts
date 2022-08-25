import * as React from 'react';
import { ButtonProps } from './Button';
export declare type ToggleButtonType = 'checkbox' | 'radio';
export interface ToggleButtonProps extends Omit<ButtonProps, 'onChange' | 'type'> {
    type?: ToggleButtonType;
    name?: string;
    checked?: boolean;
    disabled?: boolean;
    onChange?: React.ChangeEventHandler<HTMLInputElement>;
    value: string | ReadonlyArray<string> | number;
    inputRef?: React.Ref<HTMLInputElement>;
}
declare const ToggleButton: React.ForwardRefExoticComponent<ToggleButtonProps & React.RefAttributes<HTMLLabelElement>>;
export default ToggleButton;
