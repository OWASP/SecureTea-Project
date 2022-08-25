import { useEffect, useDebugValue } from 'react';
import useDebouncedState from './useDebouncedState';
/**
 * Debounce a value change by a specified number of milliseconds. Useful
 * when you want need to trigger a change based on a value change, but want
 * to defer changes until the changes reach some level of infrequency.
 *
 * @param value
 * @param delayMs
 * @returns
 */

function useDebouncedValue(value, delayMs) {
  if (delayMs === void 0) {
    delayMs = 500;
  }

  var _useDebouncedState = useDebouncedState(value, delayMs),
      debouncedValue = _useDebouncedState[0],
      setDebouncedValue = _useDebouncedState[1];

  useDebugValue(debouncedValue);
  useEffect(function () {
    setDebouncedValue(value);
  }, [value, delayMs]);
  return debouncedValue;
}

export default useDebouncedValue;