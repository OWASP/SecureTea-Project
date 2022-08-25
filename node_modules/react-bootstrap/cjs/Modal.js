"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _classnames = _interopRequireDefault(require("classnames"));

var _addEventListener = _interopRequireDefault(require("dom-helpers/addEventListener"));

var _canUseDOM = _interopRequireDefault(require("dom-helpers/canUseDOM"));

var _ownerDocument = _interopRequireDefault(require("dom-helpers/ownerDocument"));

var _removeEventListener = _interopRequireDefault(require("dom-helpers/removeEventListener"));

var _scrollbarSize = _interopRequireDefault(require("dom-helpers/scrollbarSize"));

var _useCallbackRef = _interopRequireDefault(require("@restart/hooks/useCallbackRef"));

var _useEventCallback = _interopRequireDefault(require("@restart/hooks/useEventCallback"));

var _useMergedRefs = _interopRequireDefault(require("@restart/hooks/useMergedRefs"));

var _useWillUnmount = _interopRequireDefault(require("@restart/hooks/useWillUnmount"));

var _transitionEnd = _interopRequireDefault(require("dom-helpers/transitionEnd"));

var React = _interopRequireWildcard(require("react"));

var _Modal = _interopRequireDefault(require("@restart/ui/Modal"));

var _BootstrapModalManager = require("./BootstrapModalManager");

var _Fade = _interopRequireDefault(require("./Fade"));

var _ModalBody = _interopRequireDefault(require("./ModalBody"));

var _ModalContext = _interopRequireDefault(require("./ModalContext"));

var _ModalDialog = _interopRequireDefault(require("./ModalDialog"));

var _ModalFooter = _interopRequireDefault(require("./ModalFooter"));

var _ModalHeader = _interopRequireDefault(require("./ModalHeader"));

var _ModalTitle = _interopRequireDefault(require("./ModalTitle"));

var _ThemeProvider = require("./ThemeProvider");

var _jsxRuntime = require("react/jsx-runtime");

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

const defaultProps = {
  show: false,
  backdrop: true,
  keyboard: true,
  autoFocus: true,
  enforceFocus: true,
  restoreFocus: true,
  animation: true,
  dialogAs: _ModalDialog.default
};
/* eslint-disable no-use-before-define, react/no-multi-comp */

function DialogTransition(props) {
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_Fade.default, { ...props,
    timeout: null
  });
}

function BackdropTransition(props) {
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_Fade.default, { ...props,
    timeout: null
  });
}
/* eslint-enable no-use-before-define */


const Modal = /*#__PURE__*/React.forwardRef(({
  bsPrefix,
  className,
  style,
  dialogClassName,
  contentClassName,
  children,
  dialogAs: Dialog,
  'aria-labelledby': ariaLabelledby,
  'aria-describedby': ariaDescribedby,
  'aria-label': ariaLabel,

  /* BaseModal props */
  show,
  animation,
  backdrop,
  keyboard,
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
  const [modalStyle, setStyle] = (0, React.useState)({});
  const [animateStaticModal, setAnimateStaticModal] = (0, React.useState)(false);
  const waitingForMouseUpRef = (0, React.useRef)(false);
  const ignoreBackdropClickRef = (0, React.useRef)(false);
  const removeStaticModalAnimationRef = (0, React.useRef)(null);
  const [modal, setModalRef] = (0, _useCallbackRef.default)();
  const mergedRef = (0, _useMergedRefs.default)(ref, setModalRef);
  const handleHide = (0, _useEventCallback.default)(onHide);
  const isRTL = (0, _ThemeProvider.useIsRTL)();
  bsPrefix = (0, _ThemeProvider.useBootstrapPrefix)(bsPrefix, 'modal');
  const modalContext = (0, React.useMemo)(() => ({
    onHide: handleHide
  }), [handleHide]);

  function getModalManager() {
    if (propsManager) return propsManager;
    return (0, _BootstrapModalManager.getSharedManager)({
      isRTL
    });
  }

  function updateDialogStyle(node) {
    if (!_canUseDOM.default) return;
    const containerIsOverflowing = getModalManager().getScrollbarWidth() > 0;
    const modalIsOverflowing = node.scrollHeight > (0, _ownerDocument.default)(node).documentElement.clientHeight;
    setStyle({
      paddingRight: containerIsOverflowing && !modalIsOverflowing ? (0, _scrollbarSize.default)() : undefined,
      paddingLeft: !containerIsOverflowing && modalIsOverflowing ? (0, _scrollbarSize.default)() : undefined
    });
  }

  const handleWindowResize = (0, _useEventCallback.default)(() => {
    if (modal) {
      updateDialogStyle(modal.dialog);
    }
  });
  (0, _useWillUnmount.default)(() => {
    (0, _removeEventListener.default)(window, 'resize', handleWindowResize);
    removeStaticModalAnimationRef.current == null ? void 0 : removeStaticModalAnimationRef.current();
  }); // We prevent the modal from closing during a drag by detecting where the
  // the click originates from. If it starts in the modal and then ends outside
  // don't close.

  const handleDialogMouseDown = () => {
    waitingForMouseUpRef.current = true;
  };

  const handleMouseUp = e => {
    if (waitingForMouseUpRef.current && modal && e.target === modal.dialog) {
      ignoreBackdropClickRef.current = true;
    }

    waitingForMouseUpRef.current = false;
  };

  const handleStaticModalAnimation = () => {
    setAnimateStaticModal(true);
    removeStaticModalAnimationRef.current = (0, _transitionEnd.default)(modal.dialog, () => {
      setAnimateStaticModal(false);
    });
  };

  const handleStaticBackdropClick = e => {
    if (e.target !== e.currentTarget) {
      return;
    }

    handleStaticModalAnimation();
  };

  const handleClick = e => {
    if (backdrop === 'static') {
      handleStaticBackdropClick(e);
      return;
    }

    if (ignoreBackdropClickRef.current || e.target !== e.currentTarget) {
      ignoreBackdropClickRef.current = false;
      return;
    }

    onHide == null ? void 0 : onHide();
  };

  const handleEscapeKeyDown = e => {
    if (!keyboard && backdrop === 'static') {
      // Call preventDefault to stop modal from closing in restart ui,
      // then play our animation.
      e.preventDefault();
      handleStaticModalAnimation();
    } else if (keyboard && onEscapeKeyDown) {
      onEscapeKeyDown(e);
    }
  };

  const handleEnter = (node, isAppearing) => {
    if (node) {
      updateDialogStyle(node);
    }

    onEnter == null ? void 0 : onEnter(node, isAppearing);
  };

  const handleExit = node => {
    removeStaticModalAnimationRef.current == null ? void 0 : removeStaticModalAnimationRef.current();
    onExit == null ? void 0 : onExit(node);
  };

  const handleEntering = (node, isAppearing) => {
    onEntering == null ? void 0 : onEntering(node, isAppearing); // FIXME: This should work even when animation is disabled.

    (0, _addEventListener.default)(window, 'resize', handleWindowResize);
  };

  const handleExited = node => {
    if (node) node.style.display = ''; // RHL removes it sometimes

    onExited == null ? void 0 : onExited(node); // FIXME: This should work even when animation is disabled.

    (0, _removeEventListener.default)(window, 'resize', handleWindowResize);
  };

  const renderBackdrop = (0, React.useCallback)(backdropProps => /*#__PURE__*/(0, _jsxRuntime.jsx)("div", { ...backdropProps,
    className: (0, _classnames.default)(`${bsPrefix}-backdrop`, backdropClassName, !animation && 'show')
  }), [animation, backdropClassName, bsPrefix]);
  const baseModalStyle = { ...style,
    ...modalStyle
  }; // If `display` is not set to block, autoFocus inside the modal fails
  // https://github.com/react-bootstrap/react-bootstrap/issues/5102

  baseModalStyle.display = 'block';

  const renderDialog = dialogProps => /*#__PURE__*/(0, _jsxRuntime.jsx)("div", {
    role: "dialog",
    ...dialogProps,
    style: baseModalStyle,
    className: (0, _classnames.default)(className, bsPrefix, animateStaticModal && `${bsPrefix}-static`),
    onClick: backdrop ? handleClick : undefined,
    onMouseUp: handleMouseUp,
    "aria-label": ariaLabel,
    "aria-labelledby": ariaLabelledby,
    "aria-describedby": ariaDescribedby,
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(Dialog, { ...props,
      onMouseDown: handleDialogMouseDown,
      className: dialogClassName,
      contentClassName: contentClassName,
      children: children
    })
  });

  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_ModalContext.default.Provider, {
    value: modalContext,
    children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_Modal.default, {
      show: show,
      ref: mergedRef,
      backdrop: backdrop,
      container: container,
      keyboard: true // Always set true - see handleEscapeKeyDown
      ,
      autoFocus: autoFocus,
      enforceFocus: enforceFocus,
      restoreFocus: restoreFocus,
      restoreFocusOptions: restoreFocusOptions,
      onEscapeKeyDown: handleEscapeKeyDown,
      onShow: onShow,
      onHide: onHide,
      onEnter: handleEnter,
      onEntering: handleEntering,
      onEntered: onEntered,
      onExit: handleExit,
      onExiting: onExiting,
      onExited: handleExited,
      manager: getModalManager(),
      transition: animation ? DialogTransition : undefined,
      backdropTransition: animation ? BackdropTransition : undefined,
      renderBackdrop: renderBackdrop,
      renderDialog: renderDialog
    })
  });
});
Modal.displayName = 'Modal';
Modal.defaultProps = defaultProps;

var _default = Object.assign(Modal, {
  Body: _ModalBody.default,
  Header: _ModalHeader.default,
  Title: _ModalTitle.default,
  Footer: _ModalFooter.default,
  Dialog: _ModalDialog.default,
  TRANSITION_DURATION: 300,
  BACKDROP_TRANSITION_DURATION: 150
});

exports.default = _default;
module.exports = exports.default;