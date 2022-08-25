import * as React from 'react';
import { EventKey, SelectCallback } from './types';
declare const SelectableContext: React.Context<SelectCallback | null>;
export declare const makeEventKey: (eventKey?: EventKey | null | undefined, href?: string | null) => string | null;
export default SelectableContext;
