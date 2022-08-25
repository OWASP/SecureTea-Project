"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var React = _interopRequireWildcard(require("react"));

var _classnames = _interopRequireDefault(require("classnames"));

var _useTimeout = _interopRequireDefault(require("@restart/hooks/useTimeout"));

var _ToastFade = _interopRequireDefault(require("./ToastFade"));

var _ToastHeader = _interopRequireDefault(require("./ToastHeader"));

var _ToastBody = _interopRequireDefault(require("./ToastBody"));

var _ThemeProvider = require("./ThemeProvider");

var _ToastContext = _interopRequireDefault(require("./ToastContext"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const Toast = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  transition: Transition = _ToastFade.default,
  show = true,
  animation = true,
  delay = 5000,
  autohide = false,
  onClose,
  bg,
  ...props
}, ref) => {
  bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'toast'); // We use refs for these, because we don't want to restart the autohide
  // timer in case these values change.

  const delayRef = (0, React.useRef)(delay);
  const onCloseRef = (0, React.useRef)(onClose);
  (0, React.useEffect)(() => {
    delayRef.current = delay;
    onCloseRef.current = onClose;
  }, [delay, onClose]);
  const autohideTimeout = (0, _useTimeout.default)();
  const autohideToast = !!(autohide && show);
  const autohideFunc = (0, React.useCallback)(() => {
    if (autohideToast) {
      onCloseRef.current == null ? void 0 : onCloseRef.current();
    }
  }, [autohideToast]);
  (0, React.useEffect)(() => {
    // Only reset timer if show or autohide changes.
    autohideTimeout.set(autohideFunc, delayRef.current);
  }, [autohideTimeout, autohideFunc]);
  const toastContext = (0, React.useMemo)(() => ({
    onClose
  }), [onClose]);
  const hasAnimation = !!(Transition && animation);
  const toast = /*#__PURE__*/(0, _jsxRuntime.jsx)("div", { ...props,
    ref: ref,
    className: (0, _classnames.default)(bsPrefix, className, bg && `bg-${bg}`, !hasAnimation && (show ? 'show' : 'hide')),
    role: "alert",
    "aria-live": "assertive",
    "aria-atomic": "true"
  });
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_ToastContext.default.Provider, {
    value: toastContext,
    children: hasAnimation && Transition ? /*#__PURE__*/(0, _jsxRuntime.jsx)(Transition, {
      in: show,
      unmountOnExit: true,
      children: toast
    }) : toast
  });
});
Toast.displayName = 'Toast';

var _default = Object.assign(Toast, {
  Body: _ToastBody.default,
  Header: _ToastHeader.default
});

exports.default = _default;
module.exports = exports.default;