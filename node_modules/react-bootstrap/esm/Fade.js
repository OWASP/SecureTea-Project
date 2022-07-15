import classNames from 'classnames';
import * as React from 'react';
import { useCallback } from 'react';
import { ENTERED, ENTERING } from 'react-transition-group/Transition';
import transitionEndListener from './transitionEndListener';
import triggerBrowserReflow from './triggerBrowserReflow';
import TransitionWrapper from './TransitionWrapper';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  in: false,
  timeout: 300,
  mountOnEnter: false,
  unmountOnExit: false,
  appear: false
};
const fadeStyles = {
  [ENTERING]: 'show',
  [ENTERED]: 'show'
};
const Fade = /*#__PURE__*/React.forwardRef(({
  className,
  children,
  transitionClasses = {},
  ...props
}, ref) => {
  const handleEnter = useCallback((node, isAppearing) => {
    triggerBrowserReflow(node);
    props.onEnter == null ? void 0 : props.onEnter(node, isAppearing);
  }, [props]);
  return /*#__PURE__*/_jsx(TransitionWrapper, {
    ref: ref,
    addEndListener: transitionEndListener,
    ...props,
    onEnter: handleEnter,
    childRef: children.ref,
    children: (status, innerProps) => /*#__PURE__*/React.cloneElement(children, { ...innerProps,
      className: classNames('fade', className, children.props.className, fadeStyles[status], transitionClasses[status])
    })
  });
});
Fade.defaultProps = defaultProps;
Fade.displayName = 'Fade';
export default Fade;