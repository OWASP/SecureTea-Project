import classNames from 'classnames';
import * as React from 'react';
import { useBootstrapPrefix } from './ThemeProvider';
import AbstractModalHeader from './AbstractModalHeader';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  closeLabel: 'Close',
  closeButton: false
};
const OffcanvasHeader = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  ...props
}, ref) => {
  bsPrefix = useBootstrapPrefix(bsPrefix, 'offcanvas-header');
  return /*#__PURE__*/_jsx(AbstractModalHeader, {
    ref: ref,
    ...props,
    className: classNames(className, bsPrefix)
  });
});
OffcanvasHeader.displayName = 'OffcanvasHeader';
OffcanvasHeader.defaultProps = defaultProps;
export default OffcanvasHeader;