"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _createWithBsPrefix = _interopRequireDefault(require("./createWithBsPrefix"));

var _ThemeProvider = require("./ThemeProvider");

var _FormCheckInput = _interopRequireDefault(require("./FormCheckInput"));

var _InputGroupContext = _interopRequireDefault(require("./InputGroupContext"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const InputGroupText = (0, _createWithBsPrefix.default)('input-group-text', {
  Component: 'span'
});

const InputGroupCheckbox = props => /*#__PURE__*/(0, _jsxRuntime.jsx)(InputGroupText, {
  children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_FormCheckInput.default, {
    type: "checkbox",
    ...props
  })
});

const InputGroupRadio = props => /*#__PURE__*/(0, _jsxRuntime.jsx)(InputGroupText, {
  children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_FormCheckInput.default, {
    type: "radio",
    ...props
  })
});

/**
 *
 * @property {InputGroupText} Text
 * @property {InputGroupRadio} Radio
 * @property {InputGroupCheckbox} Checkbox
 */
const InputGroup = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  size,
  hasValidation,
  className,
  // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
  as: Component = 'div',
  ...props
}, ref) => {
  bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'input-group'); // Intentionally an empty object. Used in detecting if a dropdown
  // exists under an input group.

  const contextValue = (0, React.useMemo)(() => ({}), []);
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_InputGroupContext.default.Provider, {
    value: contextValue,
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, {
      ref: ref,
      ...props,
      className: (0, _classnames.default)(className, bsPrefix, size && `${bsPrefix}-${size}`, hasValidation && 'has-validation')
    })
  });
});
InputGroup.displayName = 'InputGroup';

var _default = Object.assign(InputGroup, {
  Text: InputGroupText,
  Radio: InputGroupRadio,
  Checkbox: InputGroupCheckbox
});

exports.default = _default;
module.exports = exports.default;