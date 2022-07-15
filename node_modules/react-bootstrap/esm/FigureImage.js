import classNames from 'classnames';
import * as React from 'react';
import Image, { propTypes as imagePropTypes } from './Image';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  fluid: true
};
const FigureImage = /*#__PURE__*/React.forwardRef(({
  className,
  ...props
}, ref) => /*#__PURE__*/_jsx(Image, {
  ref: ref,
  ...props,
  className: classNames(className, 'figure-img')
}));
FigureImage.displayName = 'FigureImage';
FigureImage.propTypes = imagePropTypes;
FigureImage.defaultProps = defaultProps;
export default FigureImage;