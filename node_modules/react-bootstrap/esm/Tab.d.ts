import PropTypes from 'prop-types';
import * as React from 'react';
import { TabPaneProps } from './TabPane';
export interface TabProps extends Omit<TabPaneProps, 'title'> {
    title: React.ReactNode;
    disabled?: boolean;
    tabClassName?: string;
    tabAttrs?: Record<string, any>;
}
declare const _default: React.FC<TabProps> & {
    Container: {
        ({ transition, ...props }: import("./TabContainer").TabContainerProps): JSX.Element;
        propTypes: {
            id: PropTypes.Requireable<string>;
            transition: PropTypes.Requireable<boolean | PropTypes.ReactComponentLike>;
            mountOnEnter: PropTypes.Requireable<boolean>;
            unmountOnExit: PropTypes.Requireable<boolean>;
            generateChildId: PropTypes.Requireable<(...args: any[]) => any>;
            onSelect: PropTypes.Requireable<(...args: any[]) => any>;
            activeKey: PropTypes.Requireable<string | number>;
        };
        displayName: string;
    };
    Content: import("./helpers").BsPrefixRefForwardingComponent<"div", unknown>;
    Pane: import("./helpers").BsPrefixRefForwardingComponent<"div", TabPaneProps>;
};
export default _default;
