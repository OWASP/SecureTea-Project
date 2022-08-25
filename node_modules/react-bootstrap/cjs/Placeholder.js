"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var React = _interopRequireWildcard(require("react"));

var _usePlaceholder = _interopRequireDefault(require("./usePlaceholder"));

var _PlaceholderButton = _interopRequireDefault(require("./PlaceholderButton"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const Placeholder = /*#__PURE__*/React.forwardRef(({
  as: Component = 'span',
  ...props
}, ref) => {
  const placeholderProps = (0, _usePlaceholder.default)(props);
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, { ...placeholderProps,
    ref: ref
  });
});
Placeholder.displayName = 'Placeholder';

var _default = Object.assign(Placeholder, {
  Button: _PlaceholderButton.default
});

exports.default = _default;
module.exports = exports.default;