import classNames from 'classnames';
import * as React from 'react';
import { useBootstrapPrefix, useBootstrapBreakpoints } from './ThemeProvider';
import createUtilityClassName, { responsivePropType } from './createUtilityClasses';
import { jsx as _jsx } from "react/jsx-runtime";
const Stack = /*#__PURE__*/React.forwardRef(({
  as: Component = 'div',
  bsPrefix,
  className,
  direction,
  gap,
  ...props
}, ref) => {
  bsPrefix = useBootstrapPrefix(bsPrefix, direction === 'horizontal' ? 'hstack' : 'vstack');
  const breakpoints = useBootstrapBreakpoints();
  return /*#__PURE__*/_jsx(Component, { ...props,
    ref: ref,
    className: classNames(className, bsPrefix, ...createUtilityClassName({
      gap,
      breakpoints
    }))
  });
});
Stack.displayName = 'Stack';
export default Stack;