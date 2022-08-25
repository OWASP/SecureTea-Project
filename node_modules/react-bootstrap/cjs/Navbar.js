"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _SelectableContext = _interopRequireDefault(require("@restart/ui/SelectableContext"));

var _uncontrollable = require("uncontrollable");

var _createWithBsPrefix = _interopRequireDefault(require("./createWithBsPrefix"));

var _NavbarBrand = _interopRequireDefault(require("./NavbarBrand"));

var _NavbarCollapse = _interopRequireDefault(require("./NavbarCollapse"));

var _NavbarToggle = _interopRequireDefault(require("./NavbarToggle"));

var _NavbarOffcanvas = _interopRequireDefault(require("./NavbarOffcanvas"));

var _ThemeProvider = require("./ThemeProvider");

var _NavbarContext = _interopRequireDefault(require("./NavbarContext"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const NavbarText = (0, _createWithBsPrefix.default)('navbar-text', {
  Component: 'span'
});
const defaultProps = {
  expand: true,
  variant: 'light',
  collapseOnSelect: false
};
const Navbar = /*#__PURE__*/React.forwardRef((props, ref) => {
  const {
    bsPrefix: initialBsPrefix,
    expand,
    variant,
    bg,
    fixed,
    sticky,
    className,
    // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
    as: Component = 'nav',
    expanded,
    onToggle,
    onSelect,
    collapseOnSelect,
    ...controlledProps
  } = (0, _uncontrollable.useUncontrolled)(props, {
    expanded: 'onToggle'
  });
  const bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(initialBsPrefix, 'navbar');
  const handleCollapse = (0, React.useCallback)((...args) => {
    onSelect == null ? void 0 : onSelect(...args);

    if (collapseOnSelect && expanded) {
      onToggle == null ? void 0 : onToggle(false);
    }
  }, [onSelect, collapseOnSelect, expanded, onToggle]); // will result in some false positives but that seems better
  // than false negatives. strict `undefined` check allows explicit
  // "nulling" of the role if the user really doesn't want one

  if (controlledProps.role === undefined && Component !== 'nav') {
    controlledProps.role = 'navigation';
  }

  let expandClass = `${bsPrefix}-expand`;
  if (typeof expand === 'string') expandClass = `${expandClass}-${expand}`;
  const navbarContext = (0, React.useMemo)(() => ({
    onToggle: () => onToggle == null ? void 0 : onToggle(!expanded),
    bsPrefix,
    expanded: !!expanded,
    expand
  }), [bsPrefix, expanded, expand, onToggle]);
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_NavbarContext.default.Provider, {
    value: navbarContext,
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_SelectableContext.default.Provider, {
      value: handleCollapse,
      children: /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, {
        ref: ref,
        ...controlledProps,
        className: (0, _classnames.default)(className, bsPrefix, expand && expandClass, variant && `${bsPrefix}-${variant}`, bg && `bg-${bg}`, sticky && `sticky-${sticky}`, fixed && `fixed-${fixed}`)
      })
    })
  });
});
Navbar.defaultProps = defaultProps;
Navbar.displayName = 'Navbar';

var _default = Object.assign(Navbar, {
  Brand: _NavbarBrand.default,
  Collapse: _NavbarCollapse.default,
  Offcanvas: _NavbarOffcanvas.default,
  Text: NavbarText,
  Toggle: _NavbarToggle.default
});

exports.default = _default;
module.exports = exports.default;