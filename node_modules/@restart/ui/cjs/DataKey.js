"use strict";

exports.__esModule = true;
exports.dataAttr = dataAttr;
exports.dataProp = dataProp;
exports.PROPERTY_PREFIX = exports.ATTRIBUTE_PREFIX = void 0;
const ATTRIBUTE_PREFIX = `data-rr-ui-`;
exports.ATTRIBUTE_PREFIX = ATTRIBUTE_PREFIX;
const PROPERTY_PREFIX = `rrUi`;
exports.PROPERTY_PREFIX = PROPERTY_PREFIX;

function dataAttr(property) {
  return `${ATTRIBUTE_PREFIX}${property}`;
}

function dataProp(property) {
  return `${PROPERTY_PREFIX}${property}`;
}