import type { ReactNode } from 'react';

export interface IndustryColumnProps {
  /** The pill label above the column — the only naming this pack does itself. */
  label: string;
  /**
   * The marks. Pass real logotypes at their own aspect ratios: a roster that has
   * been normalised to one optical weight stops reading as a roster and starts
   * reading as a decoration.
   */
  children: ReactNode;
  className?: string;
}

/**
 * The pack's signature element: a pill-labelled column of other companies' marks,
 * divided from its neighbours by a hairline. Six across at 1440, three at 768, two
 * below — and the divider survives every step, because the divider is what makes it
 * a wall rather than a pile.
 *
 * It sets `container-type: inline-size`, so the rows inside answer to the column's
 * own width rather than to the viewport: the same column is dropped into grids of
 * three different widths on one page.
 */
export function IndustryColumn({ label, children, className }: IndustryColumnProps) {
  return (
    <div className={['ro-col', className].filter(Boolean).join(' ')}>
      <span className="ro-col__label">{label}</span>
      <div className="ro-col__marks">{children}</div>
    </div>
  );
}
