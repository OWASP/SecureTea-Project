"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var React = _interopRequireWildcard(require("react"));

var _useBreakpoint = _interopRequireDefault(require("@restart/hooks/useBreakpoint"));

var _classnames = _interopRequireDefault(require("classnames"));

var _ThemeProvider = require("./ThemeProvider");

var _Offcanvas = _interopRequireDefault(require("./Offcanvas"));

var _NavbarContext = _interopRequireDefault(require("./NavbarContext"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const NavbarOffcanvas = /*#__PURE__*/React.forwardRef(({
  className,
  bsPrefix,
  backdrop,
  backdropClassName,
  keyboard,
  scroll,
  placement,
  autoFocus,
  enforceFocus,
  restoreFocus,
  restoreFocusOptions,
  onShow,
  onHide,
  onEscapeKeyDown,
  onEnter,
  onEntering,
  onEntered,
  onExit,
  onExiting,
  onExited,
  ...props
}, ref) => {
  const context = (0, React.useContext)(_NavbarContext.default);
  bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'offcanvas');
  const hasExpandProp = typeof (context == null ? void 0 : context.expand) === 'string';
  const shouldExpand = (0, _useBreakpoint.default)(hasExpandProp ? context.expand : 'xs', 'up');
  return hasExpandProp && shouldExpand ? /*#__PURE__*/(0, _jsxRuntime.jsx)("div", {
    ref: ref,
    ...props,
    className: (0, _classnames.default)(className, bsPrefix, `${bsPrefix}-${placement}`)
  }) : /*#__PURE__*/(0, _jsxRuntime.jsx)(_Offcanvas.default, {
    ref: ref,
    show: !!(context != null && context.expanded),
    bsPrefix: bsPrefix,
    backdrop: backdrop,
    backdropClassName: backdropClassName,
    keyboard: keyboard,
    scroll: scroll,
    placement: placement,
    autoFocus: autoFocus,
    enforceFocus: enforceFocus,
    restoreFocus: restoreFocus,
    restoreFocusOptions: restoreFocusOptions,
    onShow: onShow,
    onHide: onHide,
    onEscapeKeyDown: onEscapeKeyDown,
    onEnter: onEnter,
    onEntering: onEntering,
    onEntered: onEntered,
    onExit: onExit,
    onExiting: onExiting,
    onExited: onExited,
    ...props
  });
});
NavbarOffcanvas.displayName = 'NavbarOffcanvas';
var _default = NavbarOffcanvas;
exports.default = _default;
module.exports = exports.default;