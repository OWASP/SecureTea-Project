"use strict";

exports.__esModule = true;
exports.default = void 0;

var _activeElement = _interopRequireDefault(require("dom-helpers/activeElement"));

var _contains = _interopRequireDefault(require("dom-helpers/contains"));

var _canUseDOM = _interopRequireDefault(require("dom-helpers/canUseDOM"));

var _listen = _interopRequireDefault(require("dom-helpers/listen"));

var React = _interopRequireWildcard(require("react"));

var _reactDom = _interopRequireDefault(require("react-dom"));

var _useMounted = _interopRequireDefault(require("@restart/hooks/useMounted"));

var _useWillUnmount = _interopRequireDefault(require("@restart/hooks/useWillUnmount"));

var _usePrevious = _interopRequireDefault(require("@restart/hooks/usePrevious"));

var _useEventCallback = _interopRequireDefault(require("@restart/hooks/useEventCallback"));

var _ModalManager = _interopRequireDefault(require("./ModalManager"));

var _useWaitForDOMRef = _interopRequireDefault(require("./useWaitForDOMRef"));

var _useWindow = _interopRequireDefault(require("./useWindow"));

var _jsxRuntime = require("react/jsx-runtime");

const _excluded = ["show", "role", "className", "style", "children", "backdrop", "keyboard", "onBackdropClick", "onEscapeKeyDown", "transition", "backdropTransition", "autoFocus", "enforceFocus", "restoreFocus", "restoreFocusOptions", "renderDialog", "renderBackdrop", "manager", "container", "onShow", "onHide", "onExit", "onExited", "onExiting", "onEnter", "onEntering", "onEntered"];

function _getRequireWildcardCache(nodeInterop) { if (typeof WeakMap !== "function") return null; var cacheBabelInterop = new WeakMap(); var cacheNodeInterop = new WeakMap(); return (_getRequireWildcardCache = function (nodeInterop) { return nodeInterop ? cacheNodeInterop : cacheBabelInterop; })(nodeInterop); }

function _interopRequireWildcard(obj, nodeInterop) { if (!nodeInterop && obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(nodeInterop); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _objectWithoutPropertiesLoose(source, excluded) { if (source == null) return {}; var target = {}; var sourceKeys = Object.keys(source); var key, i; for (i = 0; i < sourceKeys.length; i++) { key = sourceKeys[i]; if (excluded.indexOf(key) >= 0) continue; target[key] = source[key]; } return target; }

let manager;

function getManager(window) {
  if (!manager) manager = new _ModalManager.default({
    ownerDocument: window == null ? void 0 : window.document
  });
  return manager;
}

function useModalManager(provided) {
  const window = (0, _useWindow.default)();
  const modalManager = provided || getManager(window);
  const modal = (0, React.useRef)({
    dialog: null,
    backdrop: null
  });
  return Object.assign(modal.current, {
    add: () => modalManager.add(modal.current),
    remove: () => modalManager.remove(modal.current),
    isTopModal: () => modalManager.isTopModal(modal.current),
    setDialogRef: (0, React.useCallback)(ref => {
      modal.current.dialog = ref;
    }, []),
    setBackdropRef: (0, React.useCallback)(ref => {
      modal.current.backdrop = ref;
    }, [])
  });
}

const Modal = /*#__PURE__*/(0, React.forwardRef)((_ref, ref) => {
  let {
    show = false,
    role = 'dialog',
    className,
    style,
    children,
    backdrop = true,
    keyboard = true,
    onBackdropClick,
    onEscapeKeyDown,
    transition,
    backdropTransition,
    autoFocus = true,
    enforceFocus = true,
    restoreFocus = true,
    restoreFocusOptions,
    renderDialog,
    renderBackdrop = props => /*#__PURE__*/(0, _jsxRuntime.jsx)("div", Object.assign({}, props)),
    manager: providedManager,
    container: containerRef,
    onShow,
    onHide = () => {},
    onExit,
    onExited,
    onExiting,
    onEnter,
    onEntering,
    onEntered
  } = _ref,
      rest = _objectWithoutPropertiesLoose(_ref, _excluded);

  const container = (0, _useWaitForDOMRef.default)(containerRef);
  const modal = useModalManager(providedManager);
  const isMounted = (0, _useMounted.default)();
  const prevShow = (0, _usePrevious.default)(show);
  const [exited, setExited] = (0, React.useState)(!show);
  const lastFocusRef = (0, React.useRef)(null);
  (0, React.useImperativeHandle)(ref, () => modal, [modal]);

  if (_canUseDOM.default && !prevShow && show) {
    lastFocusRef.current = (0, _activeElement.default)();
  }

  if (!transition && !show && !exited) {
    setExited(true);
  } else if (show && exited) {
    setExited(false);
  }

  const handleShow = (0, _useEventCallback.default)(() => {
    modal.add();
    removeKeydownListenerRef.current = (0, _listen.default)(document, 'keydown', handleDocumentKeyDown);
    removeFocusListenerRef.current = (0, _listen.default)(document, 'focus', // the timeout is necessary b/c this will run before the new modal is mounted
    // and so steals focus from it
    () => setTimeout(handleEnforceFocus), true);

    if (onShow) {
      onShow();
    } // autofocus after onShow to not trigger a focus event for previous
    // modals before this one is shown.


    if (autoFocus) {
      const currentActiveElement = (0, _activeElement.default)(document);

      if (modal.dialog && currentActiveElement && !(0, _contains.default)(modal.dialog, currentActiveElement)) {
        lastFocusRef.current = currentActiveElement;
        modal.dialog.focus();
      }
    }
  });
  const handleHide = (0, _useEventCallback.default)(() => {
    modal.remove();
    removeKeydownListenerRef.current == null ? void 0 : removeKeydownListenerRef.current();
    removeFocusListenerRef.current == null ? void 0 : removeFocusListenerRef.current();

    if (restoreFocus) {
      var _lastFocusRef$current;

      // Support: <=IE11 doesn't support `focus()` on svg elements (RB: #917)
      (_lastFocusRef$current = lastFocusRef.current) == null ? void 0 : _lastFocusRef$current.focus == null ? void 0 : _lastFocusRef$current.focus(restoreFocusOptions);
      lastFocusRef.current = null;
    }
  }); // TODO: try and combine these effects: https://github.com/react-bootstrap/react-overlays/pull/794#discussion_r409954120
  // Show logic when:
  //  - show is `true` _and_ `container` has resolved

  (0, React.useEffect)(() => {
    if (!show || !container) return;
    handleShow();
  }, [show, container,
  /* should never change: */
  handleShow]); // Hide cleanup logic when:
  //  - `exited` switches to true
  //  - component unmounts;

  (0, React.useEffect)(() => {
    if (!exited) return;
    handleHide();
  }, [exited, handleHide]);
  (0, _useWillUnmount.default)(() => {
    handleHide();
  }); // --------------------------------

  const handleEnforceFocus = (0, _useEventCallback.default)(() => {
    if (!enforceFocus || !isMounted() || !modal.isTopModal()) {
      return;
    }

    const currentActiveElement = (0, _activeElement.default)();

    if (modal.dialog && currentActiveElement && !(0, _contains.default)(modal.dialog, currentActiveElement)) {
      modal.dialog.focus();
    }
  });
  const handleBackdropClick = (0, _useEventCallback.default)(e => {
    if (e.target !== e.currentTarget) {
      return;
    }

    onBackdropClick == null ? void 0 : onBackdropClick(e);

    if (backdrop === true) {
      onHide();
    }
  });
  const handleDocumentKeyDown = (0, _useEventCallback.default)(e => {
    if (keyboard && e.keyCode === 27 && modal.isTopModal()) {
      onEscapeKeyDown == null ? void 0 : onEscapeKeyDown(e);

      if (!e.defaultPrevented) {
        onHide();
      }
    }
  });
  const removeFocusListenerRef = (0, React.useRef)();
  const removeKeydownListenerRef = (0, React.useRef)();

  const handleHidden = (...args) => {
    setExited(true);
    onExited == null ? void 0 : onExited(...args);
  };

  const Transition = transition;

  if (!container || !(show || Transition && !exited)) {
    return null;
  }

  const dialogProps = Object.assign({
    role,
    ref: modal.setDialogRef,
    // apparently only works on the dialog role element
    'aria-modal': role === 'dialog' ? true : undefined
  }, rest, {
    style,
    className,
    tabIndex: -1
  });
  let dialog = renderDialog ? renderDialog(dialogProps) : /*#__PURE__*/(0, _jsxRuntime.jsx)("div", Object.assign({}, dialogProps, {
    children: /*#__PURE__*/React.cloneElement(children, {
      role: 'document'
    })
  }));

  if (Transition) {
    dialog = /*#__PURE__*/(0, _jsxRuntime.jsx)(Transition, {
      appear: true,
      unmountOnExit: true,
      in: !!show,
      onExit: onExit,
      onExiting: onExiting,
      onExited: handleHidden,
      onEnter: onEnter,
      onEntering: onEntering,
      onEntered: onEntered,
      children: dialog
    });
  }

  let backdropElement = null;

  if (backdrop) {
    const BackdropTransition = backdropTransition;
    backdropElement = renderBackdrop({
      ref: modal.setBackdropRef,
      onClick: handleBackdropClick
    });

    if (BackdropTransition) {
      backdropElement = /*#__PURE__*/(0, _jsxRuntime.jsx)(BackdropTransition, {
        appear: true,
        in: !!show,
        children: backdropElement
      });
    }
  }

  return /*#__PURE__*/(0, _jsxRuntime.jsx)(_jsxRuntime.Fragment, {
    children: /*#__PURE__*/_reactDom.default.createPortal( /*#__PURE__*/(0, _jsxRuntime.jsxs)(_jsxRuntime.Fragment, {
      children: [backdropElement, dialog]
    }), container)
  });
});
Modal.displayName = 'Modal';

var _default = Object.assign(Modal, {
  Manager: _ModalManager.default
});

exports.default = _default;