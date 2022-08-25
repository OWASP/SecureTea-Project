import * as React from 'react';
import { BsPrefixProps } from './helpers';
export declare type AspectRatio = '1x1' | '4x3' | '16x9' | '21x9' | string;
export interface RatioProps extends BsPrefixProps, React.HTMLAttributes<HTMLDivElement> {
    children: React.ReactChild;
    aspectRatio?: AspectRatio | number;
}
declare const Ratio: React.ForwardRefExoticComponent<RatioProps & React.RefAttributes<HTMLDivElement>>;
export default Ratio;
