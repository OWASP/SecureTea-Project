"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _ThemeProvider = require("./ThemeProvider");

var _Collapse = _interopRequireDefault(require("./Collapse"));

var _AccordionContext = _interopRequireWildcard(require("./AccordionContext"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const AccordionCollapse = /*#__PURE__*/React.forwardRef(({
  as: Component = 'div',
  bsPrefix,
  className,
  children,
  eventKey,
  ...props
}, ref) => {
  const {
    activeEventKey
  } = (0, React.useContext)(_AccordionContext.default);
  bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'accordion-collapse');
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_Collapse.default, {
    ref: ref,
    in: (0, _AccordionContext.isAccordionItemSelected)(activeEventKey, eventKey),
    ...props,
    className: (0, _classnames.default)(className, bsPrefix),
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, {
      children: React.Children.only(children)
    })
  });
});
AccordionCollapse.displayName = 'AccordionCollapse';
var _default = AccordionCollapse;
exports.default = _default;
module.exports = exports.default;