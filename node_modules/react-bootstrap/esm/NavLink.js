import classNames from 'classnames';
import * as React from 'react';
import Anchor from '@restart/ui/Anchor';
import { useNavItem } from '@restart/ui/NavItem';
import { makeEventKey } from '@restart/ui/SelectableContext';
import { useBootstrapPrefix } from './ThemeProvider';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  disabled: false
};
const NavLink = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  as: Component = Anchor,
  active,
  eventKey,
  ...props
}, ref) => {
  bsPrefix = useBootstrapPrefix(bsPrefix, 'nav-link');
  const [navItemProps, meta] = useNavItem({
    key: makeEventKey(eventKey, props.href),
    active,
    ...props
  });
  return /*#__PURE__*/_jsx(Component, { ...props,
    ...navItemProps,
    ref: ref,
    className: classNames(className, bsPrefix, props.disabled && 'disabled', meta.isActive && 'active')
  });
});
NavLink.displayName = 'NavLink';
NavLink.defaultProps = defaultProps;
export default NavLink;