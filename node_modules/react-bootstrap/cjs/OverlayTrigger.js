"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _contains = _interopRequireDefault(require("dom-helpers/contains"));

var React = _interopRequireWildcard(require("react"));

var _useTimeout = _interopRequireDefault(require("@restart/hooks/useTimeout"));

var _warning = _interopRequireDefault(require("warning"));

var _uncontrollable = require("uncontrollable");

var _useMergedRefs = _interopRequireDefault(require("@restart/hooks/useMergedRefs"));

var _Overlay = _interopRequireDefault(require("./Overlay"));

var _safeFindDOMNode = _interopRequireDefault(require("./safeFindDOMNode"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

function normalizeDelay(delay) {
  return delay && typeof delay === 'object' ? delay : {
    show: delay,
    hide: delay
  };
} // Simple implementation of mouseEnter and mouseLeave.
// React's built version is broken: https://github.com/facebook/react/issues/4251
// for cases when the trigger is disabled and mouseOut/Over can cause flicker
// moving from one child element to another.


function handleMouseOverOut( // eslint-disable-next-line @typescript-eslint/no-shadow
handler, args, relatedNative) {
  const [e] = args;
  const target = e.currentTarget;
  const related = e.relatedTarget || e.nativeEvent[relatedNative];

  if ((!related || related !== target) && !(0, _contains.default)(target, related)) {
    handler(...args);
  }
}

const defaultProps = {
  defaultShow: false,
  trigger: ['hover', 'focus']
};

function OverlayTrigger({
  trigger,
  overlay,
  children,
  popperConfig = {},
  show: propsShow,
  defaultShow = false,
  onToggle,
  delay: propsDelay,
  placement,
  flip = placement && placement.indexOf('auto') !== -1,
  ...props
}) {
  const triggerNodeRef = (0, React.useRef)(null);
  const mergedRef = (0, _useMergedRefs.default)(triggerNodeRef, children.ref);
  const timeout = (0, _useTimeout.default)();
  const hoverStateRef = (0, React.useRef)('');
  const [show, setShow] = (0, _uncontrollable.useUncontrolledProp)(propsShow, defaultShow, onToggle);
  const delay = normalizeDelay(propsDelay);
  const {
    onFocus,
    onBlur,
    onClick
  } = typeof children !== 'function' ? React.Children.only(children).props : {};

  const attachRef = r => {
    mergedRef((0, _safeFindDOMNode.default)(r));
  };

  const handleShow = (0, React.useCallback)(() => {
    timeout.clear();
    hoverStateRef.current = 'show';

    if (!delay.show) {
      setShow(true);
      return;
    }

    timeout.set(() => {
      if (hoverStateRef.current === 'show') setShow(true);
    }, delay.show);
  }, [delay.show, setShow, timeout]);
  const handleHide = (0, React.useCallback)(() => {
    timeout.clear();
    hoverStateRef.current = 'hide';

    if (!delay.hide) {
      setShow(false);
      return;
    }

    timeout.set(() => {
      if (hoverStateRef.current === 'hide') setShow(false);
    }, delay.hide);
  }, [delay.hide, setShow, timeout]);
  const handleFocus = (0, React.useCallback)((...args) => {
    handleShow();
    onFocus == null ? void 0 : onFocus(...args);
  }, [handleShow, onFocus]);
  const handleBlur = (0, React.useCallback)((...args) => {
    handleHide();
    onBlur == null ? void 0 : onBlur(...args);
  }, [handleHide, onBlur]);
  const handleClick = (0, React.useCallback)((...args) => {
    setShow(!show);
    onClick == null ? void 0 : onClick(...args);
  }, [onClick, setShow, show]);
  const handleMouseOver = (0, React.useCallback)((...args) => {
    handleMouseOverOut(handleShow, args, 'fromElement');
  }, [handleShow]);
  const handleMouseOut = (0, React.useCallback)((...args) => {
    handleMouseOverOut(handleHide, args, 'toElement');
  }, [handleHide]);
  const triggers = trigger == null ? [] : [].concat(trigger);
  const triggerProps = {
    ref: attachRef
  };

  if (triggers.indexOf('click') !== -1) {
    triggerProps.onClick = handleClick;
  }

  if (triggers.indexOf('focus') !== -1) {
    triggerProps.onFocus = handleFocus;
    triggerProps.onBlur = handleBlur;
  }

  if (triggers.indexOf('hover') !== -1) {
    process.env.NODE_ENV !== "production" ? (0, _warning.default)(triggers.length > 1, '[react-bootstrap] Specifying only the `"hover"` trigger limits the visibility of the overlay to just mouse users. Consider also including the `"focus"` trigger so that touch and keyboard only users can see the overlay as well.') : void 0;
    triggerProps.onMouseOver = handleMouseOver;
    triggerProps.onMouseOut = handleMouseOut;
  }

  return /*#__PURE__*/(0, _jsxRuntime.jsxs)(_jsxRuntime.Fragment, {
    children: [typeof children === 'function' ? children(triggerProps) : /*#__PURE__*/(0, React.cloneElement)(children, triggerProps), /*#__PURE__*/(0, _jsxRuntime.jsx)(_Overlay.default, { ...props,
      show: show,
      onHide: handleHide,
      flip: flip,
      placement: placement,
      popperConfig: popperConfig,
      target: triggerNodeRef.current,
      children: overlay
    })]
  });
}

OverlayTrigger.defaultProps = defaultProps;
var _default = OverlayTrigger;
exports.default = _default;
module.exports = exports.default;