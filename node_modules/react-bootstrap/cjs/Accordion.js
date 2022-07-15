"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var React = _interopRequireWildcard(require("react"));

var _uncontrollable = require("uncontrollable");

var _ThemeProvider = require("./ThemeProvider");

var _AccordionBody = _interopRequireDefault(require("./AccordionBody"));

var _AccordionButton = _interopRequireDefault(require("./AccordionButton"));

var _AccordionCollapse = _interopRequireDefault(require("./AccordionCollapse"));

var _AccordionContext = _interopRequireDefault(require("./AccordionContext"));

var _AccordionHeader = _interopRequireDefault(require("./AccordionHeader"));

var _AccordionItem = _interopRequireDefault(require("./AccordionItem"));

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const Accordion = /*#__PURE__*/React.forwardRef((props, ref) => {
  const {
    // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
    as: Component = 'div',
    activeKey,
    bsPrefix,
    className,
    onSelect,
    flush,
    alwaysOpen,
    ...controlledProps
  } = (0, _uncontrollable.useUncontrolled)(props, {
    activeKey: 'onSelect'
  });
  const prefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'accordion');
  const contextValue = (0, React.useMemo)(() => ({
    activeEventKey: activeKey,
    onSelect,
    alwaysOpen
  }), [activeKey, onSelect, alwaysOpen]);
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_AccordionContext.default.Provider, {
    value: contextValue,
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(Component, {
      ref: ref,
      ...controlledProps,
      className: (0, _classnames.default)(className, prefix, flush && `${prefix}-flush`)
    })
  });
});
Accordion.displayName = 'Accordion';

var _default = Object.assign(Accordion, {
  Button: _AccordionButton.default,
  Collapse: _AccordionCollapse.default,
  Item: _AccordionItem.default,
  Header: _AccordionHeader.default,
  Body: _AccordionBody.default
});

exports.default = _default;
module.exports = exports.default;