import PropTypes from 'prop-types';
import * as React from 'react';
import classNames from 'classnames';
import { jsx as _jsx } from "react/jsx-runtime";
const propTypes = {
  'aria-label': PropTypes.string,
  onClick: PropTypes.func,

  /**
   * Render different color variant for the button.
   *
   * Omitting this will render the default dark color.
   */
  variant: PropTypes.oneOf(['white'])
};
const defaultProps = {
  'aria-label': 'Close'
};
const CloseButton = /*#__PURE__*/React.forwardRef(({
  className,
  variant,
  ...props
}, ref) => /*#__PURE__*/_jsx("button", {
  ref: ref,
  type: "button",
  className: classNames('btn-close', variant && `btn-close-${variant}`, className),
  ...props
}));
CloseButton.displayName = 'CloseButton';
CloseButton.propTypes = propTypes;
CloseButton.defaultProps = defaultProps;
export default CloseButton;