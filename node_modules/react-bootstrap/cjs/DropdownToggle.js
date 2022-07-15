"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _DropdownToggle = require("@restart/ui/DropdownToggle");

var _DropdownContext = _interopRequireDefault(require("@restart/ui/DropdownContext"));

var _useMergedRefs = _interopRequireDefault(require("@restart/hooks/useMergedRefs"));

var _Button = _interopRequireDefault(require("./Button"));

var _InputGroupContext = _interopRequireDefault(require("./InputGroupContext"));

var _ThemeProvider = require("./ThemeProvider");

var _useWrappedRefWithWarning = _interopRequireDefault(require("./useWrappedRefWithWarning"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const DropdownToggle = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  split,
  className,
  childBsPrefix,
  // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
  as: Component = _Button.default,
  ...props
}, ref) => {
  const prefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'dropdown-toggle');
  const dropdownContext = (0, React.useContext)(_DropdownContext.default);
  const isInputGroup = (0, React.useContext)(_InputGroupContext.default);

  if (childBsPrefix !== undefined) {
    props.bsPrefix = childBsPrefix;
  }

  const [toggleProps] = (0, _DropdownToggle.useDropdownToggle)();
  toggleProps.ref = (0, _useMergedRefs.default)(toggleProps.ref, (0, _useWrappedRefWithWarning.default)(ref, 'DropdownToggle')); // This intentionally forwards size and variant (if set) to the
  // underlying component, to allow it to render size and style variants.

  return /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, {
    className: (0, _classnames.default)(className, prefix, split && `${prefix}-split`, !!isInputGroup && (dropdownContext == null ? void 0 : dropdownContext.show) && 'show'),
    ...toggleProps,
    ...props
  });
});
DropdownToggle.displayName = 'DropdownToggle';
var _default = DropdownToggle;
exports.default = _default;
module.exports = exports.default;