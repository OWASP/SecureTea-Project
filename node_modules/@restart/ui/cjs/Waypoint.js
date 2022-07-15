"use strict";

exports.__esModule = true;
exports.default = void 0;

var _useCallbackRef = _interopRequireDefault(require("@restart/hooks/useCallbackRef"));

var React = _interopRequireWildcard(require("react"));

var _useWaypoint = _interopRequireWildcard(require("./useWaypoint"));

exports.Position = _useWaypoint.Position;

var _jsxRuntime = require("react/jsx-runtime");

const _excluded = ["renderComponent", "onPositionChange"];

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _objectWithoutPropertiesLoose(source, excluded) { if (source == null) return {}; var target = {}; var sourceKeys = Object.keys(source); var key, i; for (i = 0; i < sourceKeys.length; i++) { key = sourceKeys[i]; if (excluded.indexOf(key) >= 0) continue; target[key] = source[key]; } return target; }

const defaultRenderComponent = ref => /*#__PURE__*/(0, _jsxRuntime.jsx)("span", {
  ref: ref,
  style: {
    fontSize: 0
  }
});

/**
 * A component that tracks when it enters or leaves the viewport. Implemented
 * using IntersectionObserver, polyfill may be required for older browsers.
 */
function Waypoint(_ref) {
  let {
    renderComponent = defaultRenderComponent,
    onPositionChange
  } = _ref,
      options = _objectWithoutPropertiesLoose(_ref, _excluded);

  const [element, setElement] = (0, _useCallbackRef.default)();
  (0, _useWaypoint.default)(element, onPositionChange, options);
  return renderComponent(setElement);
}

var _default = Waypoint;
exports.default = _default;