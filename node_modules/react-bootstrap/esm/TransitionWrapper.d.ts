import React from 'react';
import Transition, { TransitionProps, TransitionStatus } from 'react-transition-group/Transition';
export declare type TransitionWrapperProps = TransitionProps & {
    childRef?: React.Ref<unknown>;
    children: React.ReactElement | ((status: TransitionStatus, props: Record<string, unknown>) => React.ReactNode);
};
declare const TransitionWrapper: React.ForwardRefExoticComponent<(Pick<import("react-transition-group/Transition").TimeoutProps<undefined> & {
    childRef?: React.Ref<unknown> | undefined;
    children: React.ReactElement<any, string | React.JSXElementConstructor<any>> | ((status: TransitionStatus, props: Record<string, unknown>) => React.ReactNode);
}, keyof import("react-transition-group/Transition").TimeoutProps<undefined>> | Pick<import("react-transition-group/Transition").EndListenerProps<undefined> & {
    childRef?: React.Ref<unknown> | undefined;
    children: React.ReactElement<any, string | React.JSXElementConstructor<any>> | ((status: TransitionStatus, props: Record<string, unknown>) => React.ReactNode);
}, keyof import("react-transition-group/Transition").EndListenerProps<undefined>>) & React.RefAttributes<Transition<any>>>;
export default TransitionWrapper;
