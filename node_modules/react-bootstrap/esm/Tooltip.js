import classNames from 'classnames';
import * as React from 'react';
import { useBootstrapPrefix, useIsRTL } from './ThemeProvider';
import { getOverlayDirection } from './helpers';
import { jsx as _jsx } from "react/jsx-runtime";
import { jsxs as _jsxs } from "react/jsx-runtime";
const defaultProps = {
  placement: 'right'
};
const Tooltip = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  placement,
  className,
  style,
  children,
  arrowProps,
  popper: _,
  show: _2,
  ...props
}, ref) => {
  bsPrefix = useBootstrapPrefix(bsPrefix, 'tooltip');
  const isRTL = useIsRTL();
  const [primaryPlacement] = (placement == null ? void 0 : placement.split('-')) || [];
  const bsDirection = getOverlayDirection(primaryPlacement, isRTL);
  return /*#__PURE__*/_jsxs("div", {
    ref: ref,
    style: style,
    role: "tooltip",
    "x-placement": primaryPlacement,
    className: classNames(className, bsPrefix, `bs-tooltip-${bsDirection}`),
    ...props,
    children: [/*#__PURE__*/_jsx("div", {
      className: "tooltip-arrow",
      ...arrowProps
    }), /*#__PURE__*/_jsx("div", {
      className: `${bsPrefix}-inner`,
      children: children
    })]
  });
});
Tooltip.defaultProps = defaultProps;
Tooltip.displayName = 'Tooltip';
export default Tooltip;