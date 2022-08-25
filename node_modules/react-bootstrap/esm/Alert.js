import classNames from 'classnames';
import * as React from 'react';
import { useUncontrolled } from 'uncontrollable';
import useEventCallback from '@restart/hooks/useEventCallback';
import Anchor from '@restart/ui/Anchor';
import { useBootstrapPrefix } from './ThemeProvider';
import Fade from './Fade';
import CloseButton from './CloseButton';
import divWithClassName from './divWithClassName';
import createWithBsPrefix from './createWithBsPrefix';
import { jsx as _jsx } from "react/jsx-runtime";
import { jsxs as _jsxs } from "react/jsx-runtime";
const DivStyledAsH4 = divWithClassName('h4');
DivStyledAsH4.displayName = 'DivStyledAsH4';
const AlertHeading = createWithBsPrefix('alert-heading', {
  Component: DivStyledAsH4
});
const AlertLink = createWithBsPrefix('alert-link', {
  Component: Anchor
});
const defaultProps = {
  variant: 'primary',
  show: true,
  transition: Fade,
  closeLabel: 'Close alert'
};
const Alert = /*#__PURE__*/React.forwardRef((uncontrolledProps, ref) => {
  const {
    bsPrefix,
    show,
    closeLabel,
    closeVariant,
    className,
    children,
    variant,
    onClose,
    dismissible,
    transition,
    ...props
  } = useUncontrolled(uncontrolledProps, {
    show: 'onClose'
  });
  const prefix = useBootstrapPrefix(bsPrefix, 'alert');
  const handleClose = useEventCallback(e => {
    if (onClose) {
      onClose(false, e);
    }
  });
  const Transition = transition === true ? Fade : transition;

  const alert = /*#__PURE__*/_jsxs("div", {
    role: "alert",
    ...(!Transition ? props : undefined),
    ref: ref,
    className: classNames(className, prefix, variant && `${prefix}-${variant}`, dismissible && `${prefix}-dismissible`),
    children: [dismissible && /*#__PURE__*/_jsx(CloseButton, {
      onClick: handleClose,
      "aria-label": closeLabel,
      variant: closeVariant
    }), children]
  });

  if (!Transition) return show ? alert : null;
  return /*#__PURE__*/_jsx(Transition, {
    unmountOnExit: true,
    ...props,
    ref: undefined,
    in: show,
    children: alert
  });
});
Alert.displayName = 'Alert';
Alert.defaultProps = defaultProps;
export default Object.assign(Alert, {
  Link: AlertLink,
  Heading: AlertHeading
});