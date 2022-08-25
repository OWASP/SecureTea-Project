import classNames from 'classnames';
import * as React from 'react';
import { useBootstrapPrefix, useIsRTL } from './ThemeProvider';
import PopoverHeader from './PopoverHeader';
import PopoverBody from './PopoverBody';
import { getOverlayDirection } from './helpers';
import { jsx as _jsx } from "react/jsx-runtime";
import { jsxs as _jsxs } from "react/jsx-runtime";
const defaultProps = {
  placement: 'right'
};
const Popover = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  placement,
  className,
  style,
  children,
  body,
  arrowProps,
  popper: _,
  show: _1,
  ...props
}, ref) => {
  const decoratedBsPrefix = useBootstrapPrefix(bsPrefix, 'popover');
  const isRTL = useIsRTL();
  const [primaryPlacement] = (placement == null ? void 0 : placement.split('-')) || [];
  const bsDirection = getOverlayDirection(primaryPlacement, isRTL);
  return /*#__PURE__*/_jsxs("div", {
    ref: ref,
    role: "tooltip",
    style: style,
    "x-placement": primaryPlacement,
    className: classNames(className, decoratedBsPrefix, primaryPlacement && `bs-popover-${bsDirection}`),
    ...props,
    children: [/*#__PURE__*/_jsx("div", {
      className: "popover-arrow",
      ...arrowProps
    }), body ? /*#__PURE__*/_jsx(PopoverBody, {
      children: children
    }) : children]
  });
});
Popover.defaultProps = defaultProps;
export default Object.assign(Popover, {
  Header: PopoverHeader,
  Body: PopoverBody,
  // Default popover offset.
  // https://github.com/twbs/bootstrap/blob/5c32767e0e0dbac2d934bcdee03719a65d3f1187/js/src/popover.js#L28
  POPPER_OFFSET: [0, 8]
});