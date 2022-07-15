"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = exports.Prev = exports.Next = exports.Last = exports.First = exports.Ellipsis = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _Anchor = _interopRequireDefault(require("@restart/ui/Anchor"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

/* eslint-disable react/no-multi-comp */
const defaultProps = {
  active: false,
  disabled: false,
  activeLabel: '(current)'
};
const PageItem = /*#__PURE__*/React.forwardRef(({
  active,
  disabled,
  className,
  style,
  activeLabel,
  children,
  ...props
}, ref) => {
  const Component = active || disabled ? 'span' : _Anchor.default;
  return /*#__PURE__*/(0, _jsxRuntime.jsx)("li", {
    ref: ref,
    style: style,
    className: (0, _classnames.default)(className, 'page-item', {
      active,
      disabled
    }),
    children: /*#__PURE__*/(0, _jsxRuntime.jsxs)(Component, {
      className: "page-link",
      disabled: disabled,
      ...props,
      children: [children, active && activeLabel && /*#__PURE__*/(0, _jsxRuntime.jsx)("span", {
        className: "visually-hidden",
        children: activeLabel
      })]
    })
  });
});
PageItem.defaultProps = defaultProps;
PageItem.displayName = 'PageItem';
var _default = PageItem;
exports.default = _default;

function createButton(name, defaultValue, label = name) {
  const Button = /*#__PURE__*/React.forwardRef(({
    children,
    ...props
  }, ref) => /*#__PURE__*/(0, _jsxRuntime.jsxs)(PageItem, { ...props,
    ref: ref,
    children: [/*#__PURE__*/(0, _jsxRuntime.jsx)("span", {
      "aria-hidden": "true",
      children: children || defaultValue
    }), /*#__PURE__*/(0, _jsxRuntime.jsx)("span", {
      className: "visually-hidden",
      children: label
    })]
  }));
  Button.displayName = name;
  return Button;
}

const First = createButton('First', '«');
exports.First = First;
const Prev = createButton('Prev', '‹', 'Previous');
exports.Prev = Prev;
const Ellipsis = createButton('Ellipsis', '…', 'More');
exports.Ellipsis = Ellipsis;
const Next = createButton('Next', '›');
exports.Next = Next;
const Last = createButton('Last', '»');
exports.Last = Last;