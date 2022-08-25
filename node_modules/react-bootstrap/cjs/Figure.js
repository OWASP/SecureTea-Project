"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _createWithBsPrefix = _interopRequireDefault(require("./createWithBsPrefix"));

var _FigureImage = _interopRequireDefault(require("./FigureImage"));

var _FigureCaption = _interopRequireDefault(require("./FigureCaption"));

const Figure = (0, _createWithBsPrefix.default)('figure', {
  Component: 'figure'
});

var _default = Object.assign(Figure, {
  Image: _FigureImage.default,
  Caption: _FigureCaption.default
});

exports.default = _default;
module.exports = exports.default;