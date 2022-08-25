"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _useEventCallback = _interopRequireDefault(require("@restart/hooks/useEventCallback"));

var _NavItem = require("@restart/ui/NavItem");

var _SelectableContext = require("@restart/ui/SelectableContext");

var _ThemeProvider = require("./ThemeProvider");

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const ListGroupItem = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  active,
  disabled,
  eventKey,
  className,
  variant,
  action,
  as,
  ...props
}, ref) => {
  bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'list-group-item');
  const [navItemProps, meta] = (0, _NavItem.useNavItem)({
    key: (0, _SelectableContext.makeEventKey)(eventKey, props.href),
    active,
    ...props
  });
  const handleClick = (0, _useEventCallback.default)(event => {
    if (disabled) {
      event.preventDefault();
      event.stopPropagation();
      return;
    }

    navItemProps.onClick(event);
  });

  if (disabled && props.tabIndex === undefined) {
    props.tabIndex = -1;
    props['aria-disabled'] = true;
  } // eslint-disable-next-line no-nested-ternary


  const Component = as || (action ? props.href ? 'a' : 'button' : 'div');
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, {
    ref: ref,
    ...props,
    ...navItemProps,
    onClick: handleClick,
    className: (0, _classnames.default)(className, bsPrefix, meta.isActive && 'active', disabled && 'disabled', variant && `${bsPrefix}-${variant}`, action && `${bsPrefix}-action`)
  });
});
ListGroupItem.displayName = 'ListGroupItem';
var _default = ListGroupItem;
exports.default = _default;
module.exports = exports.default;