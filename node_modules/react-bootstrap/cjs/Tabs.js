"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var React = _interopRequireWildcard(require("react"));

var _uncontrollable = require("uncontrollable");

var _Tabs = _interopRequireDefault(require("@restart/ui/Tabs"));

var _Nav = _interopRequireDefault(require("./Nav"));

var _NavLink = _interopRequireDefault(require("./NavLink"));

var _NavItem = _interopRequireDefault(require("./NavItem"));

var _TabContent = _interopRequireDefault(require("./TabContent"));

var _TabPane = _interopRequireDefault(require("./TabPane"));

var _ElementChildren = require("./ElementChildren");

var _getTabTransitionComponent = _interopRequireDefault(require("./getTabTransitionComponent"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const defaultProps = {
  variant: 'tabs',
  mountOnEnter: false,
  unmountOnExit: false
};

function getDefaultActiveKey(children) {
  let defaultActiveKey;
  (0, _ElementChildren.forEach)(children, child => {
    if (defaultActiveKey == null) {
      defaultActiveKey = child.props.eventKey;
    }
  });
  return defaultActiveKey;
}

function renderTab(child) {
  const {
    title,
    eventKey,
    disabled,
    tabClassName,
    tabAttrs,
    id
  } = child.props;

  if (title == null) {
    return null;
  }

  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_NavItem.default, {
    as: "li",
    role: "presentation",
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_NavLink.default, {
      as: "button",
      type: "button",
      eventKey: eventKey,
      disabled: disabled,
      id: id,
      className: tabClassName,
      ...tabAttrs,
      children: title
    })
  });
}

const Tabs = props => {
  const {
    id,
    onSelect,
    transition,
    mountOnEnter,
    unmountOnExit,
    children,
    activeKey = getDefaultActiveKey(children),
    ...controlledProps
  } = (0, _uncontrollable.useUncontrolled)(props, {
    activeKey: 'onSelect'
  });
  return /*#__PURE__*/(0, _jsxRuntime.jsxs)(_Tabs.default, {
    id: id,
    activeKey: activeKey,
    onSelect: onSelect,
    transition: (0, _getTabTransitionComponent.default)(transition),
    mountOnEnter: mountOnEnter,
    unmountOnExit: unmountOnExit,
    children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_Nav.default, { ...controlledProps,
      role: "tablist",
      as: "ul",
      children: (0, _ElementChildren.map)(children, renderTab)
    }), /*#__PURE__*/(0, _jsxRuntime.jsx)(_TabContent.default, {
      children: (0, _ElementChildren.map)(children, child => {
        const childProps = { ...child.props
        };
        delete childProps.title;
        delete childProps.disabled;
        delete childProps.tabClassName;
        delete childProps.tabAttrs;
        return /*#__PURE__*/(0, _jsxRuntime.jsx)(_TabPane.default, { ...childProps
        });
      })
    })]
  });
};

Tabs.defaultProps = defaultProps;
Tabs.displayName = 'Tabs';
var _default = Tabs;
exports.default = _default;
module.exports = exports.default;