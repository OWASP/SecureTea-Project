"use strict";

exports.__esModule = true;
exports.useDropdownItem = useDropdownItem;
exports.default = void 0;

var React = _interopRequireWildcard(require("react"));

var _useEventCallback = _interopRequireDefault(require("@restart/hooks/useEventCallback"));

var _SelectableContext = _interopRequireWildcard(require("./SelectableContext"));

var _NavContext = _interopRequireDefault(require("./NavContext"));

var _Button = _interopRequireDefault(require("./Button"));

var _DataKey = require("./DataKey");

var _jsxRuntime = require("react/jsx-runtime");

const _excluded = ["eventKey", "disabled", "onClick", "active", "as"];

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

function _objectWithoutPropertiesLoose(source, excluded) { if (source == null) return {}; var target = {}; var sourceKeys = Object.keys(source); var key, i; for (i = 0; i < sourceKeys.length; i++) { key = sourceKeys[i]; if (excluded.indexOf(key) >= 0) continue; target[key] = source[key]; } return target; }

/**
 * Create a dropdown item. Returns a set of props for the dropdown item component
 * including an `onClick` handler that prevents selection when the item is disabled
 */
function useDropdownItem({
  key,
  href,
  active,
  disabled,
  onClick
}) {
  const onSelectCtx = (0, React.useContext)(_SelectableContext.default);
  const navContext = (0, React.useContext)(_NavContext.default);
  const {
    activeKey
  } = navContext || {};
  const eventKey = (0, _SelectableContext.makeEventKey)(key, href);
  const isActive = active == null && key != null ? (0, _SelectableContext.makeEventKey)(activeKey) === eventKey : active;
  const handleClick = (0, _useEventCallback.default)(event => {
    if (disabled) return;
    onClick == null ? void 0 : onClick(event);

    if (onSelectCtx && !event.isPropagationStopped()) {
      onSelectCtx(eventKey, event);
    }
  });
  return [{
    onClick: handleClick,
    'aria-disabled': disabled || undefined,
    'aria-selected': isActive,
    [(0, _DataKey.dataAttr)('dropdown-item')]: ''
  }, {
    isActive
  }];
}

const DropdownItem = /*#__PURE__*/React.forwardRef((_ref, ref) => {
  let {
    eventKey,
    disabled,
    onClick,
    active,
    as: Component = _Button.default
  } = _ref,
      props = _objectWithoutPropertiesLoose(_ref, _excluded);

  const [dropdownItemProps] = useDropdownItem({
    key: eventKey,
    href: props.href,
    disabled,
    onClick,
    active
  });
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, Object.assign({}, props, {
    ref: ref
  }, dropdownItemProps));
});
DropdownItem.displayName = 'DropdownItem';
var _default = DropdownItem;
exports.default = _default;