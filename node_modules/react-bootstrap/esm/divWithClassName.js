import * as React from 'react';
import classNames from 'classnames';
import { jsx as _jsx } from "react/jsx-runtime";
export default (className => /*#__PURE__*/React.forwardRef((p, ref) => /*#__PURE__*/_jsx("div", { ...p,
  ref: ref,
  className: classNames(p.className, className)
})));