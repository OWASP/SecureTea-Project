import classNames from 'classnames';
import * as React from 'react';
import useEventCallback from '@restart/hooks/useEventCallback';
import { useNavItem } from '@restart/ui/NavItem';
import { makeEventKey } from '@restart/ui/SelectableContext';
import { useBootstrapPrefix } from './ThemeProvider';
import { jsx as _jsx } from "react/jsx-runtime";
const ListGroupItem = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  active,
  disabled,
  eventKey,
  className,
  variant,
  action,
  as,
  ...props
}, ref) => {
  bsPrefix = useBootstrapPrefix(bsPrefix, 'list-group-item');
  const [navItemProps, meta] = useNavItem({
    key: makeEventKey(eventKey, props.href),
    active,
    ...props
  });
  const handleClick = useEventCallback(event => {
    if (disabled) {
      event.preventDefault();
      event.stopPropagation();
      return;
    }

    navItemProps.onClick(event);
  });

  if (disabled && props.tabIndex === undefined) {
    props.tabIndex = -1;
    props['aria-disabled'] = true;
  } // eslint-disable-next-line no-nested-ternary


  const Component = as || (action ? props.href ? 'a' : 'button' : 'div');
  return /*#__PURE__*/_jsx(Component, {
    ref: ref,
    ...props,
    ...navItemProps,
    onClick: handleClick,
    className: classNames(className, bsPrefix, meta.isActive && 'active', disabled && 'disabled', variant && `${bsPrefix}-${variant}`, action && `${bsPrefix}-action`)
  });
});
ListGroupItem.displayName = 'ListGroupItem';
export default ListGroupItem;