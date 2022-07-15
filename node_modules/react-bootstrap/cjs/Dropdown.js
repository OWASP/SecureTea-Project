"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _Dropdown = _interopRequireDefault(require("@restart/ui/Dropdown"));

var _uncontrollable = require("uncontrollable");

var _useEventCallback = _interopRequireDefault(require("@restart/hooks/useEventCallback"));

var _DropdownContext = _interopRequireDefault(require("./DropdownContext"));

var _DropdownItem = _interopRequireDefault(require("./DropdownItem"));

var _DropdownMenu = _interopRequireWildcard(require("./DropdownMenu"));

var _DropdownToggle = _interopRequireDefault(require("./DropdownToggle"));

var _InputGroupContext = _interopRequireDefault(require("./InputGroupContext"));

var _ThemeProvider = require("./ThemeProvider");

var _createWithBsPrefix = _interopRequireDefault(require("./createWithBsPrefix"));

var _types = require("./types");

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const DropdownHeader = (0, _createWithBsPrefix.default)('dropdown-header', {
  defaultProps: {
    role: 'heading'
  }
});
const DropdownDivider = (0, _createWithBsPrefix.default)('dropdown-divider', {
  Component: 'hr',
  defaultProps: {
    role: 'separator'
  }
});
const DropdownItemText = (0, _createWithBsPrefix.default)('dropdown-item-text', {
  Component: 'span'
});
const defaultProps = {
  navbar: false,
  align: 'start',
  autoClose: true
};
const Dropdown = /*#__PURE__*/React.forwardRef((pProps, ref) => {
  const {
    bsPrefix,
    drop,
    show,
    className,
    align,
    onSelect,
    onToggle,
    focusFirstItemOnShow,
    // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
    as: Component = 'div',
    navbar: _4,
    autoClose,
    ...props
  } = (0, _uncontrollable.useUncontrolled)(pProps, {
    show: 'onToggle'
  });
  const isInputGroup = (0, React.useContext)(_InputGroupContext.default);
  const prefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'dropdown');
  const isRTL = (0, _ThemeProvider.useIsRTL)();

  const isClosingPermitted = source => {
    // autoClose=false only permits close on button click
    if (autoClose === false) return source === 'click'; // autoClose=inside doesn't permit close on rootClose

    if (autoClose === 'inside') return source !== 'rootClose'; // autoClose=outside doesn't permit close on select

    if (autoClose === 'outside') return source !== 'select';
    return true;
  };

  const handleToggle = (0, _useEventCallback.default)((nextShow, meta) => {
    if (meta.originalEvent.currentTarget === document && (meta.source !== 'keydown' || meta.originalEvent.key === 'Escape')) meta.source = 'rootClose';
    if (isClosingPermitted(meta.source)) onToggle == null ? void 0 : onToggle(nextShow, meta);
  });
  const alignEnd = align === 'end';
  const placement = (0, _DropdownMenu.getDropdownMenuPlacement)(alignEnd, drop, isRTL);
  const contextValue = (0, React.useMemo)(() => ({
    align,
    drop,
    isRTL
  }), [align, drop, isRTL]);
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_DropdownContext.default.Provider, {
    value: contextValue,
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_Dropdown.default, {
      placement: placement,
      show: show,
      onSelect: onSelect,
      onToggle: handleToggle,
      focusFirstItemOnShow: focusFirstItemOnShow,
      itemSelector: `.${prefix}-item:not(.disabled):not(:disabled)`,
      children: isInputGroup ? props.children : /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, { ...props,
        ref: ref,
        className: (0, _classnames.default)(className, show && 'show', (!drop || drop === 'down') && prefix, drop === 'up' && 'dropup', drop === 'end' && 'dropend', drop === 'start' && 'dropstart')
      })
    })
  });
});
Dropdown.displayName = 'Dropdown';
Dropdown.defaultProps = defaultProps;

var _default = Object.assign(Dropdown, {
  Toggle: _DropdownToggle.default,
  Menu: _DropdownMenu.default,
  Item: _DropdownItem.default,
  ItemText: DropdownItemText,
  Divider: DropdownDivider,
  Header: DropdownHeader
});

exports.default = _default;
module.exports = exports.default;