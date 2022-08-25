"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var React = _interopRequireWildcard(require("react"));

var _propTypes = _interopRequireDefault(require("prop-types"));

var _Dropdown = _interopRequireDefault(require("./Dropdown"));

var _DropdownToggle = _interopRequireDefault(require("./DropdownToggle"));

var _DropdownMenu = _interopRequireDefault(require("./DropdownMenu"));

var _types = require("./types");

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const propTypes = {
  /**
   * An html id attribute for the Toggle button, necessary for assistive technologies, such as screen readers.
   * @type {string}
   */
  id: _propTypes.default.string,

  /** An `href` passed to the Toggle component */
  href: _propTypes.default.string,

  /** An `onClick` handler passed to the Toggle component */
  onClick: _propTypes.default.func,

  /** The content of the non-toggle Button.  */
  title: _propTypes.default.node.isRequired,

  /** Disables both Buttons  */
  disabled: _propTypes.default.bool,

  /**
   * Aligns the dropdown menu.
   *
   * _see [DropdownMenu](#dropdown-menu-props) for more details_
   *
   * @type {"start"|"end"|{ sm: "start"|"end" }|{ md: "start"|"end" }|{ lg: "start"|"end" }|{ xl: "start"|"end"}|{ xxl: "start"|"end"} }
   */
  align: _types.alignPropType,

  /** An ARIA accessible role applied to the Menu component. When set to 'menu', The dropdown */
  menuRole: _propTypes.default.string,

  /** Whether to render the dropdown menu in the DOM before the first time it is shown */
  renderMenuOnMount: _propTypes.default.bool,

  /**
   *  Which event when fired outside the component will cause it to be closed.
   *
   * _see [DropdownMenu](#dropdown-menu-props) for more details_
   */
  rootCloseEvent: _propTypes.default.string,

  /**
   * Menu color variant.
   *
   * Omitting this will use the default light color.
   */
  menuVariant: _propTypes.default.oneOf(['dark']),

  /** @ignore */
  bsPrefix: _propTypes.default.string,

  /** @ignore */
  variant: _propTypes.default.string,

  /** @ignore */
  size: _propTypes.default.string
};
/**
 * A convenience component for simple or general use dropdowns. Renders a `Button` toggle and all `children`
 * are passed directly to the default `Dropdown.Menu`. This component accepts all of
 * [`Dropdown`'s props](#dropdown-props).
 *
 * _All unknown props are passed through to the `Dropdown` component._ Only
 * the Button `variant`, `size` and `bsPrefix` props are passed to the toggle,
 * along with menu-related props are passed to the `Dropdown.Menu`
 */

const DropdownButton = /*#__PURE__*/React.forwardRef(({
  title,
  children,
  bsPrefix,
  rootCloseEvent,
  variant,
  size,
  menuRole,
  renderMenuOnMount,
  disabled,
  href,
  id,
  menuVariant,
  ...props
}, ref) => /*#__PURE__*/(0, _jsxRuntime.jsxs)(_Dropdown.default, {
  ref: ref,
  ...props,
  children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_DropdownToggle.default, {
    id: id,
    href: href,
    size: size,
    variant: variant,
    disabled: disabled,
    childBsPrefix: bsPrefix,
    children: title
  }), /*#__PURE__*/(0, _jsxRuntime.jsx)(_DropdownMenu.default, {
    role: menuRole,
    renderOnMount: renderMenuOnMount,
    rootCloseEvent: rootCloseEvent,
    variant: menuVariant,
    children: children
  })]
}));
DropdownButton.displayName = 'DropdownButton';
DropdownButton.propTypes = propTypes;
var _default = DropdownButton;
exports.default = _default;
module.exports = exports.default;