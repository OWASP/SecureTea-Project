import * as React from 'react';
export declare const DEFAULT_BREAKPOINTS: string[];
export interface ThemeContextValue {
    prefixes: Record<string, string>;
    breakpoints: string[];
    dir?: string;
}
export interface ThemeProviderProps extends Partial<ThemeContextValue> {
    children: React.ReactNode;
}
declare const Consumer: React.Consumer<ThemeContextValue>;
declare function ThemeProvider({ prefixes, breakpoints, dir, children, }: ThemeProviderProps): JSX.Element;
declare namespace ThemeProvider {
    var propTypes: any;
}
export declare function useBootstrapPrefix(prefix: string | undefined, defaultPrefix: string): string;
export declare function useBootstrapBreakpoints(): string[];
export declare function useIsRTL(): boolean;
declare function createBootstrapComponent(Component: any, opts: any): React.ForwardRefExoticComponent<{
    bsPrefix?: string | undefined;
} & React.RefAttributes<any>>;
export { createBootstrapComponent, Consumer as ThemeConsumer };
export default ThemeProvider;
