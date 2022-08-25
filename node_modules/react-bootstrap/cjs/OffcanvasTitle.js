"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _createWithBsPrefix = _interopRequireDefault(require("./createWithBsPrefix"));

var _divWithClassName = _interopRequireDefault(require("./divWithClassName"));

const DivStyledAsH5 = (0, _divWithClassName.default)('h5');

var _default = (0, _createWithBsPrefix.default)('offcanvas-title', {
  Component: DivStyledAsH5
});

exports.default = _default;
module.exports = exports.default;