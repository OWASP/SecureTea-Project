import classNames from 'classnames';
import * as React from 'react';
import { useBootstrapPrefix } from './ThemeProvider';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  role: 'toolbar'
};
const ButtonToolbar = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  ...props
}, ref) => {
  const prefix = useBootstrapPrefix(bsPrefix, 'btn-toolbar');
  return /*#__PURE__*/_jsx("div", { ...props,
    ref: ref,
    className: classNames(className, prefix)
  });
});
ButtonToolbar.displayName = 'ButtonToolbar';
ButtonToolbar.defaultProps = defaultProps;
export default ButtonToolbar;