import classNames from 'classnames';
import * as React from 'react';
import { useBootstrapPrefix } from './ThemeProvider';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  vertical: false,
  role: 'group'
};
const ButtonGroup = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  size,
  vertical,
  className,
  // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
  as: Component = 'div',
  ...rest
}, ref) => {
  const prefix = useBootstrapPrefix(bsPrefix, 'btn-group');
  let baseClass = prefix;
  if (vertical) baseClass = `${prefix}-vertical`;
  return /*#__PURE__*/_jsx(Component, { ...rest,
    ref: ref,
    className: classNames(className, baseClass, size && `${prefix}-${size}`)
  });
});
ButtonGroup.displayName = 'ButtonGroup';
ButtonGroup.defaultProps = defaultProps;
export default ButtonGroup;