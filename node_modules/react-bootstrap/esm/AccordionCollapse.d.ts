import { CollapseProps } from './Collapse';
import { BsPrefixRefForwardingComponent, BsPrefixProps } from './helpers';
export interface AccordionCollapseProps extends BsPrefixProps, CollapseProps {
    eventKey: string;
}
declare const AccordionCollapse: BsPrefixRefForwardingComponent<'div', AccordionCollapseProps>;
export default AccordionCollapse;
