"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _ThemeProvider = require("./ThemeProvider");

var _Dropdown = _interopRequireDefault(require("./Dropdown"));

var _NavLink = _interopRequireDefault(require("./NavLink"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const NavDropdown = /*#__PURE__*/React.forwardRef(({
  id,
  title,
  children,
  bsPrefix,
  className,
  rootCloseEvent,
  menuRole,
  disabled,
  active,
  renderMenuOnMount,
  menuVariant,
  ...props
}, ref) => {
  /* NavItem has no additional logic, it's purely presentational. Can set nav item class here to support "as" */
  const navItemPrefix = (0, _ThemeProvider.useBootstrapPrefix)(undefined, 'nav-item');
  return /*#__PURE__*/(0, _jsxRuntime.jsxs)(_Dropdown.default, {
    ref: ref,
    ...props,
    className: (0, _classnames.default)(className, navItemPrefix),
    children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_Dropdown.default.Toggle, {
      id: id,
      eventKey: null,
      active: active,
      disabled: disabled,
      childBsPrefix: bsPrefix,
      as: _NavLink.default,
      children: title
    }), /*#__PURE__*/(0, _jsxRuntime.jsx)(_Dropdown.default.Menu, {
      role: menuRole,
      renderOnMount: renderMenuOnMount,
      rootCloseEvent: rootCloseEvent,
      variant: menuVariant,
      children: children
    })]
  });
});
NavDropdown.displayName = 'NavDropdown';

var _default = Object.assign(NavDropdown, {
  Item: _Dropdown.default.Item,
  ItemText: _Dropdown.default.ItemText,
  Divider: _Dropdown.default.Divider,
  Header: _Dropdown.default.Header
});

exports.default = _default;
module.exports = exports.default;