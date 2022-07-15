"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _ThemeProvider = require("./ThemeProvider");

var _createWithBsPrefix = _interopRequireDefault(require("./createWithBsPrefix"));

var _divWithClassName = _interopRequireDefault(require("./divWithClassName"));

var _CardImg = _interopRequireDefault(require("./CardImg"));

var _CardHeader = _interopRequireDefault(require("./CardHeader"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const DivStyledAsH5 = (0, _divWithClassName.default)('h5');
const DivStyledAsH6 = (0, _divWithClassName.default)('h6');
const CardBody = (0, _createWithBsPrefix.default)('card-body');
const CardTitle = (0, _createWithBsPrefix.default)('card-title', {
  Component: DivStyledAsH5
});
const CardSubtitle = (0, _createWithBsPrefix.default)('card-subtitle', {
  Component: DivStyledAsH6
});
const CardLink = (0, _createWithBsPrefix.default)('card-link', {
  Component: 'a'
});
const CardText = (0, _createWithBsPrefix.default)('card-text', {
  Component: 'p'
});
const CardFooter = (0, _createWithBsPrefix.default)('card-footer');
const CardImgOverlay = (0, _createWithBsPrefix.default)('card-img-overlay');
const defaultProps = {
  body: false
};
const Card = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  bg,
  text,
  border,
  body,
  children,
  // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
  as: Component = 'div',
  ...props
}, ref) => {
  const prefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'card');
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, {
    ref: ref,
    ...props,
    className: (0, _classnames.default)(className, prefix, bg && `bg-${bg}`, text && `text-${text}`, border && `border-${border}`),
    children: body ? /*#__PURE__*/(0, _jsxRuntime.jsx)(CardBody, {
      children: children
    }) : children
  });
});
Card.displayName = 'Card';
Card.defaultProps = defaultProps;

var _default = Object.assign(Card, {
  Img: _CardImg.default,
  Title: CardTitle,
  Subtitle: CardSubtitle,
  Body: CardBody,
  Link: CardLink,
  Text: CardText,
  Header: _CardHeader.default,
  Footer: CardFooter,
  ImgOverlay: CardImgOverlay
});

exports.default = _default;
module.exports = exports.default;