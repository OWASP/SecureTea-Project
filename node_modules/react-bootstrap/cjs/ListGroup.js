"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _warning = _interopRequireDefault(require("warning"));

var _uncontrollable = require("uncontrollable");

var _Nav = _interopRequireDefault(require("@restart/ui/Nav"));

var _ThemeProvider = require("./ThemeProvider");

var _ListGroupItem = _interopRequireDefault(require("./ListGroupItem"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const ListGroup = /*#__PURE__*/React.forwardRef((props, ref) => {
  const {
    className,
    bsPrefix: initialBsPrefix,
    variant,
    horizontal,
    numbered,
    // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
    as = 'div',
    ...controlledProps
  } = (0, _uncontrollable.useUncontrolled)(props, {
    activeKey: 'onSelect'
  });
  const bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(initialBsPrefix, 'list-group');
  let horizontalVariant;

  if (horizontal) {
    horizontalVariant = horizontal === true ? 'horizontal' : `horizontal-${horizontal}`;
  }

  process.env.NODE_ENV !== "production" ? (0, _warning.default)(!(horizontal && variant === 'flush'), '`variant="flush"` and `horizontal` should not be used together.') : void 0;
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_Nav.default, {
    ref: ref,
    ...controlledProps,
    as: as,
    className: (0, _classnames.default)(className, bsPrefix, variant && `${bsPrefix}-${variant}`, horizontalVariant && `${bsPrefix}-${horizontalVariant}`, numbered && `${bsPrefix}-numbered`)
  });
});
ListGroup.displayName = 'ListGroup';

var _default = Object.assign(ListGroup, {
  Item: _ListGroupItem.default
});

exports.default = _default;
module.exports = exports.default;