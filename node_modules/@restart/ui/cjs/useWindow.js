"use strict";

exports.__esModule = true;
exports.default = useWindow;
exports.WindowProvider = void 0;

var _react = require("react");

var _canUseDOM = _interopRequireDefault(require("dom-helpers/canUseDOM"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

const Context = /*#__PURE__*/(0, _react.createContext)(_canUseDOM.default ? window : undefined);
const WindowProvider = Context.Provider;
/**
 * The document "window" placed in React context. Helpful for determining
 * SSR context, or when rendering into an iframe.
 *
 * @returns the current window
 */

exports.WindowProvider = WindowProvider;

function useWindow() {
  return (0, _react.useContext)(Context);
}