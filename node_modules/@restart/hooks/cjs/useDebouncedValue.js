"use strict";

exports.__esModule = true;
exports.default = void 0;

var _react = require("react");

var _useDebouncedState2 = _interopRequireDefault(require("./useDebouncedState"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

/**
 * Debounce a value change by a specified number of milliseconds. Useful
 * when you want need to trigger a change based on a value change, but want
 * to defer changes until the changes reach some level of infrequency.
 *
 * @param value
 * @param delayMs
 * @returns
 */
function useDebouncedValue(value, delayMs) {
  if (delayMs === void 0) {
    delayMs = 500;
  }

  var _useDebouncedState = (0, _useDebouncedState2.default)(value, delayMs),
      debouncedValue = _useDebouncedState[0],
      setDebouncedValue = _useDebouncedState[1];

  (0, _react.useDebugValue)(debouncedValue);
  (0, _react.useEffect)(function () {
    setDebouncedValue(value);
  }, [value, delayMs]);
  return debouncedValue;
}

var _default = useDebouncedValue;
exports.default = _default;