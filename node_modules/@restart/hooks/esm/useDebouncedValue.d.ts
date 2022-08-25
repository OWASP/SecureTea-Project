/**
 * Debounce a value change by a specified number of milliseconds. Useful
 * when you want need to trigger a change based on a value change, but want
 * to defer changes until the changes reach some level of infrequency.
 *
 * @param value
 * @param delayMs
 * @returns
 */
declare function useDebouncedValue<TValue>(value: TValue, delayMs?: number): TValue;
export default useDebouncedValue;
