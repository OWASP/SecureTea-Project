import classNames from 'classnames';
import * as React from 'react';
import { useCallback, useMemo } from 'react';
import SelectableContext from '@restart/ui/SelectableContext';
import { useUncontrolled } from 'uncontrollable';
import createWithBsPrefix from './createWithBsPrefix';
import NavbarBrand from './NavbarBrand';
import NavbarCollapse from './NavbarCollapse';
import NavbarToggle from './NavbarToggle';
import NavbarOffcanvas from './NavbarOffcanvas';
import { useBootstrapPrefix } from './ThemeProvider';
import NavbarContext from './NavbarContext';
import { jsx as _jsx } from "react/jsx-runtime";
const NavbarText = createWithBsPrefix('navbar-text', {
  Component: 'span'
});
const defaultProps = {
  expand: true,
  variant: 'light',
  collapseOnSelect: false
};
const Navbar = /*#__PURE__*/React.forwardRef((props, ref) => {
  const {
    bsPrefix: initialBsPrefix,
    expand,
    variant,
    bg,
    fixed,
    sticky,
    className,
    // Need to define the default "as" during prop destructuring to be compatible with styled-components github.com/react-bootstrap/react-bootstrap/issues/3595
    as: Component = 'nav',
    expanded,
    onToggle,
    onSelect,
    collapseOnSelect,
    ...controlledProps
  } = useUncontrolled(props, {
    expanded: 'onToggle'
  });
  const bsPrefix = useBootstrapPrefix(initialBsPrefix, 'navbar');
  const handleCollapse = useCallback((...args) => {
    onSelect == null ? void 0 : onSelect(...args);

    if (collapseOnSelect && expanded) {
      onToggle == null ? void 0 : onToggle(false);
    }
  }, [onSelect, collapseOnSelect, expanded, onToggle]); // will result in some false positives but that seems better
  // than false negatives. strict `undefined` check allows explicit
  // "nulling" of the role if the user really doesn't want one

  if (controlledProps.role === undefined && Component !== 'nav') {
    controlledProps.role = 'navigation';
  }

  let expandClass = `${bsPrefix}-expand`;
  if (typeof expand === 'string') expandClass = `${expandClass}-${expand}`;
  const navbarContext = useMemo(() => ({
    onToggle: () => onToggle == null ? void 0 : onToggle(!expanded),
    bsPrefix,
    expanded: !!expanded,
    expand
  }), [bsPrefix, expanded, expand, onToggle]);
  return /*#__PURE__*/_jsx(NavbarContext.Provider, {
    value: navbarContext,
    children: /*#__PURE__*/_jsx(SelectableContext.Provider, {
      value: handleCollapse,
      children: /*#__PURE__*/_jsx(Component, {
        ref: ref,
        ...controlledProps,
        className: classNames(className, bsPrefix, expand && expandClass, variant && `${bsPrefix}-${variant}`, bg && `bg-${bg}`, sticky && `sticky-${sticky}`, fixed && `fixed-${fixed}`)
      })
    })
  });
});
Navbar.defaultProps = defaultProps;
Navbar.displayName = 'Navbar';
export default Object.assign(Navbar, {
  Brand: NavbarBrand,
  Collapse: NavbarCollapse,
  Offcanvas: NavbarOffcanvas,
  Text: NavbarText,
  Toggle: NavbarToggle
});