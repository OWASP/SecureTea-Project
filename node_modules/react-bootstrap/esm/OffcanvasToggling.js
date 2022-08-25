import classNames from 'classnames';
import * as React from 'react';
import { ENTERED, ENTERING, EXITING } from 'react-transition-group/Transition';
import transitionEndListener from './transitionEndListener';
import TransitionWrapper from './TransitionWrapper';
import { useBootstrapPrefix } from './ThemeProvider';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  in: false,
  mountOnEnter: false,
  unmountOnExit: false,
  appear: false
};
const transitionStyles = {
  [ENTERING]: 'show',
  [ENTERED]: 'show'
};
const OffcanvasToggling = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  children,
  ...props
}, ref) => {
  bsPrefix = useBootstrapPrefix(bsPrefix, 'offcanvas');
  return /*#__PURE__*/_jsx(TransitionWrapper, {
    ref: ref,
    addEndListener: transitionEndListener,
    ...props,
    childRef: children.ref,
    children: (status, innerProps) => /*#__PURE__*/React.cloneElement(children, { ...innerProps,
      className: classNames(className, children.props.className, (status === ENTERING || status === EXITING) && `${bsPrefix}-toggling`, transitionStyles[status])
    })
  });
});
OffcanvasToggling.defaultProps = defaultProps;
OffcanvasToggling.displayName = 'OffcanvasToggling';
export default OffcanvasToggling;