import contains from 'dom-helpers/contains';
import listen from 'dom-helpers/listen';
import ownerDocument from 'dom-helpers/ownerDocument';
import { useCallback, useEffect, useRef } from 'react';
import useEventCallback from '@restart/hooks/useEventCallback';
import warning from 'warning';

const noop = () => {};

function isLeftClickEvent(event) {
  return event.button === 0;
}

function isModifiedEvent(event) {
  return !!(event.metaKey || event.altKey || event.ctrlKey || event.shiftKey);
}

export const getRefTarget = ref => ref && ('current' in ref ? ref.current : ref);
const InitialTriggerEvents = {
  click: 'mousedown',
  mouseup: 'mousedown',
  pointerup: 'pointerdown'
};
/**
 * The `useClickOutside` hook registers your callback on the document that fires
 * when a pointer event is registered outside of the provided ref or element.
 *
 * @param {Ref<HTMLElement>| HTMLElement} ref  The element boundary
 * @param {function} onClickOutside
 * @param {object=}  options
 * @param {boolean=} options.disabled
 * @param {string=}  options.clickTrigger The DOM event name (click, mousedown, etc) to attach listeners on
 */

function useClickOutside(ref, onClickOutside = noop, {
  disabled,
  clickTrigger = 'click'
} = {}) {
  const preventMouseClickOutsideRef = useRef(false);
  const waitingForTrigger = useRef(false);
  const handleMouseCapture = useCallback(e => {
    const currentTarget = getRefTarget(ref);
    warning(!!currentTarget, 'ClickOutside captured a close event but does not have a ref to compare it to. ' + 'useClickOutside(), should be passed a ref that resolves to a DOM node');
    preventMouseClickOutsideRef.current = !currentTarget || isModifiedEvent(e) || !isLeftClickEvent(e) || !!contains(currentTarget, e.target) || waitingForTrigger.current;
    waitingForTrigger.current = false;
  }, [ref]);
  const handleInitialMouse = useEventCallback(e => {
    const currentTarget = getRefTarget(ref);

    if (currentTarget && contains(currentTarget, e.target)) {
      waitingForTrigger.current = true;
    }
  });
  const handleMouse = useEventCallback(e => {
    if (!preventMouseClickOutsideRef.current) {
      onClickOutside(e);
    }
  });
  useEffect(() => {
    if (disabled || ref == null) return undefined;
    const doc = ownerDocument(getRefTarget(ref)); // Store the current event to avoid triggering handlers immediately
    // https://github.com/facebook/react/issues/20074

    let currentEvent = (doc.defaultView || window).event;
    let removeInitialTriggerListener = null;

    if (InitialTriggerEvents[clickTrigger]) {
      removeInitialTriggerListener = listen(doc, InitialTriggerEvents[clickTrigger], handleInitialMouse, true);
    } // Use capture for this listener so it fires before React's listener, to
    // avoid false positives in the contains() check below if the target DOM
    // element is removed in the React mouse callback.


    const removeMouseCaptureListener = listen(doc, clickTrigger, handleMouseCapture, true);
    const removeMouseListener = listen(doc, clickTrigger, e => {
      // skip if this event is the same as the one running when we added the handlers
      if (e === currentEvent) {
        currentEvent = undefined;
        return;
      }

      handleMouse(e);
    });
    let mobileSafariHackListeners = [];

    if ('ontouchstart' in doc.documentElement) {
      mobileSafariHackListeners = [].slice.call(doc.body.children).map(el => listen(el, 'mousemove', noop));
    }

    return () => {
      removeInitialTriggerListener == null ? void 0 : removeInitialTriggerListener();
      removeMouseCaptureListener();
      removeMouseListener();
      mobileSafariHackListeners.forEach(remove => remove());
    };
  }, [ref, disabled, clickTrigger, handleMouseCapture, handleInitialMouse, handleMouse]);
}

export default useClickOutside;