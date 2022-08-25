"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _useEventCallback = _interopRequireDefault(require("@restart/hooks/useEventCallback"));

var _ThemeProvider = require("./ThemeProvider");

var _CloseButton = _interopRequireDefault(require("./CloseButton"));

var _ToastContext = _interopRequireDefault(require("./ToastContext"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const defaultProps = {
  closeLabel: 'Close',
  closeButton: true
};
const ToastHeader = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  closeLabel,
  closeVariant,
  closeButton,
  className,
  children,
  ...props
}, ref) => {
  bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'toast-header');
  const context = (0, React.useContext)(_ToastContext.default);
  const handleClick = (0, _useEventCallback.default)(e => {
    context == null ? void 0 : context.onClose == null ? void 0 : context.onClose(e);
  });
  return /*#__PURE__*/(0, _jsxRuntime.jsxs)("div", {
    ref: ref,
    ...props,
    className: (0, _classnames.default)(bsPrefix, className),
    children: [children, closeButton && /*#__PURE__*/(0, _jsxRuntime.jsx)(_CloseButton.default, {
      "aria-label": closeLabel,
      variant: closeVariant,
      onClick: handleClick,
      "data-dismiss": "toast"
    })]
  });
});
ToastHeader.displayName = 'ToastHeader';
ToastHeader.defaultProps = defaultProps;
var _default = ToastHeader;
exports.default = _default;
module.exports = exports.default;