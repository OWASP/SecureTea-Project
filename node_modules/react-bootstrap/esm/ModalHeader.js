import classNames from 'classnames';
import * as React from 'react';
import { useBootstrapPrefix } from './ThemeProvider';
import AbstractModalHeader from './AbstractModalHeader';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  closeLabel: 'Close',
  closeButton: false
};
const ModalHeader = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  ...props
}, ref) => {
  bsPrefix = useBootstrapPrefix(bsPrefix, 'modal-header');
  return /*#__PURE__*/_jsx(AbstractModalHeader, {
    ref: ref,
    ...props,
    className: classNames(className, bsPrefix)
  });
});
ModalHeader.displayName = 'ModalHeader';
ModalHeader.defaultProps = defaultProps;
export default ModalHeader;