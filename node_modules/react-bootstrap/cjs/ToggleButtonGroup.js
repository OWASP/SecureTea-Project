"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var React = _interopRequireWildcard(require("react"));

var _invariant = _interopRequireDefault(require("invariant"));

var _uncontrollable = require("uncontrollable");

var _createChainedFunction = _interopRequireDefault(require("./createChainedFunction"));

var _ElementChildren = require("./ElementChildren");

var _ButtonGroup = _interopRequireDefault(require("./ButtonGroup"));

var _ToggleButton = _interopRequireDefault(require("./ToggleButton"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const defaultProps = {
  type: 'radio',
  vertical: false
};
const ToggleButtonGroup = /*#__PURE__*/React.forwardRef((props, ref) => {
  const {
    children,
    type,
    name,
    value,
    onChange,
    ...controlledProps
  } = (0, _uncontrollable.useUncontrolled)(props, {
    value: 'onChange'
  });

  const getValues = () => value == null ? [] : [].concat(value);

  const handleToggle = (inputVal, event) => {
    if (!onChange) {
      return;
    }

    const values = getValues();
    const isActive = values.indexOf(inputVal) !== -1;

    if (type === 'radio') {
      if (!isActive && onChange) onChange(inputVal, event);
      return;
    }

    if (isActive) {
      onChange(values.filter(n => n !== inputVal), event);
    } else {
      onChange([...values, inputVal], event);
    }
  };

  !(type !== 'radio' || !!name) ? process.env.NODE_ENV !== "production" ? (0, _invariant.default)(false, 'A `name` is required to group the toggle buttons when the `type` ' + 'is set to "radio"') : invariant(false) : void 0;
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_ButtonGroup.default, { ...controlledProps,
    ref: ref,
    children: (0, _ElementChildren.map)(children, child => {
      const values = getValues();
      const {
        value: childVal,
        onChange: childOnChange
      } = child.props;

      const handler = e => handleToggle(childVal, e);

      return /*#__PURE__*/React.cloneElement(child, {
        type,
        name: child.name || name,
        checked: values.indexOf(childVal) !== -1,
        onChange: (0, _createChainedFunction.default)(childOnChange, handler)
      });
    })
  });
});
ToggleButtonGroup.defaultProps = defaultProps;

var _default = Object.assign(ToggleButtonGroup, {
  Button: _ToggleButton.default
});

exports.default = _default;
module.exports = exports.default;