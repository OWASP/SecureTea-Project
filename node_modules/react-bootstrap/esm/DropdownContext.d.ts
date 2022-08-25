import * as React from 'react';
import { AlignType } from './types';
export declare type DropDirection = 'up' | 'start' | 'end' | 'down';
export declare type DropdownContextValue = {
    align?: AlignType;
    drop?: DropDirection;
    isRTL?: boolean;
};
declare const DropdownContext: React.Context<DropdownContextValue>;
export default DropdownContext;
