import classNames from 'classnames';
import * as React from 'react';
import Anchor from '@restart/ui/Anchor';
import { useBootstrapPrefix } from './ThemeProvider';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  active: false,
  linkProps: {}
};
const BreadcrumbItem = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  active,
  children,
  className,
  // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
  as: Component = 'li',
  linkAs: LinkComponent = Anchor,
  linkProps,
  href,
  title,
  target,
  ...props
}, ref) => {
  const prefix = useBootstrapPrefix(bsPrefix, 'breadcrumb-item');
  return /*#__PURE__*/_jsx(Component, {
    ref: ref,
    ...props,
    className: classNames(prefix, className, {
      active
    }),
    "aria-current": active ? 'page' : undefined,
    children: active ? children : /*#__PURE__*/_jsx(LinkComponent, { ...linkProps,
      href: href,
      title: title,
      target: target,
      children: children
    })
  });
});
BreadcrumbItem.displayName = 'BreadcrumbItem';
BreadcrumbItem.defaultProps = defaultProps;
export default BreadcrumbItem;