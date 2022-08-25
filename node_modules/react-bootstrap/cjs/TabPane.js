"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _SelectableContext = _interopRequireDefault(require("@restart/ui/SelectableContext"));

var _TabContext = _interopRequireDefault(require("@restart/ui/TabContext"));

var _TabPanel = require("@restart/ui/TabPanel");

var _ThemeProvider = require("./ThemeProvider");

var _Fade = _interopRequireDefault(require("./Fade"));

var _getTabTransitionComponent = _interopRequireDefault(require("./getTabTransitionComponent"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const TabPane = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  transition,
  ...props
}, ref) => {
  const [{
    className,
    // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
    as: Component = 'div',
    ...rest
  }, {
    isActive,
    onEnter,
    onEntering,
    onEntered,
    onExit,
    onExiting,
    onExited,
    mountOnEnter,
    unmountOnExit,
    transition: Transition = _Fade.default
  }] = (0, _TabPanel.useTabPanel)({ ...props,
    transition: (0, _getTabTransitionComponent.default)(transition)
  });
  const prefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'tab-pane'); // We provide an empty the TabContext so `<Nav>`s in `<TabPanel>`s don't
  // conflict with the top level one.

  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_TabContext.default.Provider, {
    value: null,
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_SelectableContext.default.Provider, {
      value: null,
      children: /*#__PURE__*/(0, _jsxRuntime.jsx)(Transition, {
        in: isActive,
        onEnter: onEnter,
        onEntering: onEntering,
        onEntered: onEntered,
        onExit: onExit,
        onExiting: onExiting,
        onExited: onExited,
        mountOnEnter: mountOnEnter,
        unmountOnExit: unmountOnExit,
        children: /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, { ...rest,
          ref: ref,
          className: (0, _classnames.default)(className, prefix, isActive && 'active')
        })
      })
    })
  });
});
TabPane.displayName = 'TabPane';
var _default = TabPane;
exports.default = _default;
module.exports = exports.default;