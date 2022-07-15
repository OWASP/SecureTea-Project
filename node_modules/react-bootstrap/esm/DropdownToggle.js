import classNames from 'classnames';
import * as React from 'react';
import { useContext } from 'react';
import { useDropdownToggle } from '@restart/ui/DropdownToggle';
import DropdownContext from '@restart/ui/DropdownContext';
import useMergedRefs from '@restart/hooks/useMergedRefs';
import Button from './Button';
import InputGroupContext from './InputGroupContext';
import { useBootstrapPrefix } from './ThemeProvider';
import useWrappedRefWithWarning from './useWrappedRefWithWarning';
import { jsx as _jsx } from "react/jsx-runtime";
const DropdownToggle = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  split,
  className,
  childBsPrefix,
  // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
  as: Component = Button,
  ...props
}, ref) => {
  const prefix = useBootstrapPrefix(bsPrefix, 'dropdown-toggle');
  const dropdownContext = useContext(DropdownContext);
  const isInputGroup = useContext(InputGroupContext);

  if (childBsPrefix !== undefined) {
    props.bsPrefix = childBsPrefix;
  }

  const [toggleProps] = useDropdownToggle();
  toggleProps.ref = useMergedRefs(toggleProps.ref, useWrappedRefWithWarning(ref, 'DropdownToggle')); // This intentionally forwards size and variant (if set) to the
  // underlying component, to allow it to render size and style variants.

  return /*#__PURE__*/_jsx(Component, {
    className: classNames(className, prefix, split && `${prefix}-split`, !!isInputGroup && (dropdownContext == null ? void 0 : dropdownContext.show) && 'show'),
    ...toggleProps,
    ...props
  });
});
DropdownToggle.displayName = 'DropdownToggle';
export default DropdownToggle;