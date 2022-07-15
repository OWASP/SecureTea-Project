"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var _css = _interopRequireDefault(require("dom-helpers/css"));

var _react = _interopRequireWildcard(require("react"));

var _Transition = require("react-transition-group/Transition");

var _transitionEndListener = _interopRequireDefault(require("./transitionEndListener"));

var _createChainedFunction = _interopRequireDefault(require("./createChainedFunction"));

var _triggerBrowserReflow = _interopRequireDefault(require("./triggerBrowserReflow"));

var _TransitionWrapper = _interopRequireDefault(require("./TransitionWrapper"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const MARGINS = {
  height: ['marginTop', 'marginBottom'],
  width: ['marginLeft', 'marginRight']
};

function getDefaultDimensionValue(dimension, elem) {
  const offset = `offset${dimension[0].toUpperCase()}${dimension.slice(1)}`;
  const value = elem[offset];
  const margins = MARGINS[dimension];
  return value + // @ts-ignore
  parseInt((0, _css.default)(elem, margins[0]), 10) + // @ts-ignore
  parseInt((0, _css.default)(elem, margins[1]), 10);
}

const collapseStyles = {
  [_Transition.EXITED]: 'collapse',
  [_Transition.EXITING]: 'collapsing',
  [_Transition.ENTERING]: 'collapsing',
  [_Transition.ENTERED]: 'collapse show'
};
const defaultProps = {
  in: false,
  timeout: 300,
  mountOnEnter: false,
  unmountOnExit: false,
  appear: false,
  getDimensionValue: getDefaultDimensionValue
};

const Collapse = /*#__PURE__*/_react.default.forwardRef(({
  onEnter,
  onEntering,
  onEntered,
  onExit,
  onExiting,
  className,
  children,
  dimension = 'height',
  getDimensionValue = getDefaultDimensionValue,
  ...props
}, ref) => {
  /* Compute dimension */
  const computedDimension = typeof dimension === 'function' ? dimension() : dimension;
  /* -- Expanding -- */

  const handleEnter = (0, _react.useMemo)(() => (0, _createChainedFunction.default)(elem => {
    elem.style[computedDimension] = '0';
  }, onEnter), [computedDimension, onEnter]);
  const handleEntering = (0, _react.useMemo)(() => (0, _createChainedFunction.default)(elem => {
    const scroll = `scroll${computedDimension[0].toUpperCase()}${computedDimension.slice(1)}`;
    elem.style[computedDimension] = `${elem[scroll]}px`;
  }, onEntering), [computedDimension, onEntering]);
  const handleEntered = (0, _react.useMemo)(() => (0, _createChainedFunction.default)(elem => {
    elem.style[computedDimension] = null;
  }, onEntered), [computedDimension, onEntered]);
  /* -- Collapsing -- */

  const handleExit = (0, _react.useMemo)(() => (0, _createChainedFunction.default)(elem => {
    elem.style[computedDimension] = `${getDimensionValue(computedDimension, elem)}px`;
    (0, _triggerBrowserReflow.default)(elem);
  }, onExit), [onExit, getDimensionValue, computedDimension]);
  const handleExiting = (0, _react.useMemo)(() => (0, _createChainedFunction.default)(elem => {
    elem.style[computedDimension] = null;
  }, onExiting), [computedDimension, onExiting]);
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_TransitionWrapper.default, {
    ref: ref,
    addEndListener: _transitionEndListener.default,
    ...props,
    "aria-expanded": props.role ? props.in : null,
    onEnter: handleEnter,
    onEntering: handleEntering,
    onEntered: handleEntered,
    onExit: handleExit,
    onExiting: handleExiting,
    childRef: children.ref,
    children: (state, innerProps) => /*#__PURE__*/_react.default.cloneElement(children, { ...innerProps,
      className: (0, _classnames.default)(className, children.props.className, collapseStyles[state], computedDimension === 'width' && 'collapse-horizontal')
    })
  });
}); // @ts-ignore


// @ts-ignore
Collapse.defaultProps = defaultProps;
var _default = Collapse;
exports.default = _default;
module.exports = exports.default;