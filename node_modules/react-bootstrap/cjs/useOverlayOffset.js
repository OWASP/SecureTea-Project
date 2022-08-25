"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = useOverlayOffset;

var _react = require("react");

var _hasClass = _interopRequireDefault(require("dom-helpers/hasClass"));

var _ThemeProvider = require("./ThemeProvider");

var _Popover = _interopRequireDefault(require("./Popover"));

// This is meant for internal use.
// This applies a custom offset to the overlay if it's a popover.
function useOverlayOffset(customOffset) {
  const overlayRef = (0, _react.useRef)(null);
  const popoverClass = (0, _ThemeProvider.useBootstrapPrefix)(undefined, 'popover');
  const offset = (0, _react.useMemo)(() => ({
    name: 'offset',
    options: {
      offset: () => {
        if (overlayRef.current && (0, _hasClass.default)(overlayRef.current, popoverClass)) {
          return customOffset || _Popover.default.POPPER_OFFSET;
        }

        return customOffset || [0, 0];
      }
    }
  }), [customOffset, popoverClass]);
  return [overlayRef, [offset]];
}

module.exports = exports.default;