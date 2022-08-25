"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _ThemeProvider = require("./ThemeProvider");

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const defaultProps = {
  aspectRatio: '1x1'
};

function toPercent(num) {
  if (num <= 0 || num > 100) return '100%';
  if (num < 1) return `${num * 100}%`;
  return `${num}%`;
}

const Ratio = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  children,
  aspectRatio,
  style,
  ...props
}, ref) => {
  bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'ratio');
  const isCustomRatio = typeof aspectRatio === 'number';
  return /*#__PURE__*/(0, _jsxRuntime.jsx)("div", {
    ref: ref,
    ...props,
    style: { ...style,
      ...(isCustomRatio && {
        '--bs-aspect-ratio': toPercent(aspectRatio)
      })
    },
    className: (0, _classnames.default)(bsPrefix, className, !isCustomRatio && `${bsPrefix}-${aspectRatio}`),
    children: React.Children.only(children)
  });
});
Ratio.defaultProps = defaultProps;
var _default = Ratio;
exports.default = _default;
module.exports = exports.default;