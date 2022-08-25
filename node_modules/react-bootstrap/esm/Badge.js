import classNames from 'classnames';
import * as React from 'react';
import { useBootstrapPrefix } from './ThemeProvider';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  bg: 'primary',
  pill: false
};
const Badge = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  bg,
  pill,
  text,
  className,
  as: Component = 'span',
  ...props
}, ref) => {
  const prefix = useBootstrapPrefix(bsPrefix, 'badge');
  return /*#__PURE__*/_jsx(Component, {
    ref: ref,
    ...props,
    className: classNames(className, prefix, pill && `rounded-pill`, text && `text-${text}`, bg && `bg-${bg}`)
  });
});
Badge.displayName = 'Badge';
Badge.defaultProps = defaultProps;
export default Badge;