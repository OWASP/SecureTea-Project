import classNames from 'classnames';
import useEventCallback from '@restart/hooks/useEventCallback';
import * as React from 'react';
import { useCallback, useContext, useMemo, useRef } from 'react';
import BaseModal from '@restart/ui/Modal';
import Fade from './Fade';
import OffcanvasBody from './OffcanvasBody';
import OffcanvasToggling from './OffcanvasToggling';
import ModalContext from './ModalContext';
import NavbarContext from './NavbarContext';
import OffcanvasHeader from './OffcanvasHeader';
import OffcanvasTitle from './OffcanvasTitle';
import { useBootstrapPrefix } from './ThemeProvider';
import BootstrapModalManager, { getSharedManager } from './BootstrapModalManager';
import { jsx as _jsx } from "react/jsx-runtime";
const defaultProps = {
  show: false,
  backdrop: true,
  keyboard: true,
  scroll: false,
  autoFocus: true,
  enforceFocus: true,
  restoreFocus: true,
  placement: 'start'
};

function DialogTransition(props) {
  return /*#__PURE__*/_jsx(OffcanvasToggling, { ...props
  });
}

function BackdropTransition(props) {
  return /*#__PURE__*/_jsx(Fade, { ...props
  });
}

const Offcanvas = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  children,
  'aria-labelledby': ariaLabelledby,
  placement,

  /* BaseModal props */
  show,
  backdrop,
  keyboard,
  scroll,
  onEscapeKeyDown,
  onShow,
  onHide,
  container,
  autoFocus,
  enforceFocus,
  restoreFocus,
  restoreFocusOptions,
  onEntered,
  onExit,
  onExiting,
  onEnter,
  onEntering,
  onExited,
  backdropClassName,
  manager: propsManager,
  ...props
}, ref) => {
  const modalManager = useRef();
  bsPrefix = useBootstrapPrefix(bsPrefix, 'offcanvas');
  const {
    onToggle
  } = useContext(NavbarContext) || {};
  const handleHide = useEventCallback(() => {
    onToggle == null ? void 0 : onToggle();
    onHide == null ? void 0 : onHide();
  });
  const modalContext = useMemo(() => ({
    onHide: handleHide
  }), [handleHide]);

  function getModalManager() {
    if (propsManager) return propsManager;

    if (scroll) {
      // Have to use a different modal manager since the shared
      // one handles overflow.
      if (!modalManager.current) modalManager.current = new BootstrapModalManager({
        handleContainerOverflow: false
      });
      return modalManager.current;
    }

    return getSharedManager();
  }

  const handleEnter = (node, ...args) => {
    if (node) node.style.visibility = 'visible';
    onEnter == null ? void 0 : onEnter(node, ...args);
  };

  const handleExited = (node, ...args) => {
    if (node) node.style.visibility = '';
    onExited == null ? void 0 : onExited(...args);
  };

  const renderBackdrop = useCallback(backdropProps => /*#__PURE__*/_jsx("div", { ...backdropProps,
    className: classNames(`${bsPrefix}-backdrop`, backdropClassName)
  }), [backdropClassName, bsPrefix]);

  const renderDialog = dialogProps => /*#__PURE__*/_jsx("div", {
    role: "dialog",
    ...dialogProps,
    ...props,
    className: classNames(className, bsPrefix, `${bsPrefix}-${placement}`),
    "aria-labelledby": ariaLabelledby,
    children: children
  });

  return /*#__PURE__*/_jsx(ModalContext.Provider, {
    value: modalContext,
    children: /*#__PURE__*/_jsx(BaseModal, {
      show: show,
      ref: ref,
      backdrop: backdrop,
      container: container,
      keyboard: keyboard,
      autoFocus: autoFocus,
      enforceFocus: enforceFocus && !scroll,
      restoreFocus: restoreFocus,
      restoreFocusOptions: restoreFocusOptions,
      onEscapeKeyDown: onEscapeKeyDown,
      onShow: onShow,
      onHide: handleHide,
      onEnter: handleEnter,
      onEntering: onEntering,
      onEntered: onEntered,
      onExit: onExit,
      onExiting: onExiting,
      onExited: handleExited,
      manager: getModalManager(),
      transition: DialogTransition,
      backdropTransition: BackdropTransition,
      renderBackdrop: renderBackdrop,
      renderDialog: renderDialog
    })
  });
});
Offcanvas.displayName = 'Offcanvas';
Offcanvas.defaultProps = defaultProps;
export default Object.assign(Offcanvas, {
  Body: OffcanvasBody,
  Header: OffcanvasHeader,
  Title: OffcanvasTitle
});