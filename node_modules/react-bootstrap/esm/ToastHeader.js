import classNames from 'classnames';
import * as React from 'react';
import { useContext } from 'react';
import useEventCallback from '@restart/hooks/useEventCallback';
import { useBootstrapPrefix } from './ThemeProvider';
import CloseButton from './CloseButton';
import ToastContext from './ToastContext';
import { jsx as _jsx } from "react/jsx-runtime";
import { jsxs as _jsxs } from "react/jsx-runtime";
const defaultProps = {
  closeLabel: 'Close',
  closeButton: true
};
const ToastHeader = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  closeLabel,
  closeVariant,
  closeButton,
  className,
  children,
  ...props
}, ref) => {
  bsPrefix = useBootstrapPrefix(bsPrefix, 'toast-header');
  const context = useContext(ToastContext);
  const handleClick = useEventCallback(e => {
    context == null ? void 0 : context.onClose == null ? void 0 : context.onClose(e);
  });
  return /*#__PURE__*/_jsxs("div", {
    ref: ref,
    ...props,
    className: classNames(bsPrefix, className),
    children: [children, closeButton && /*#__PURE__*/_jsx(CloseButton, {
      "aria-label": closeLabel,
      variant: closeVariant,
      onClick: handleClick,
      "data-dismiss": "toast"
    })]
  });
});
ToastHeader.displayName = 'ToastHeader';
ToastHeader.defaultProps = defaultProps;
export default ToastHeader;