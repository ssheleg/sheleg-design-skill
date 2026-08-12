import type { ReactNode } from 'react';

/** The nine categories measured on the reference. `step` is the neutral. */
export type Category =
  | 'reply'
  | 'newsletter'
  | 'marketing'
  | 'calendar'
  | 'notification'
  | 'cold'
  | 'team'
  | 'urgent'
  | 'step';

export interface CategoryChipProps {
  category: Category;
  /**
   * The label word, and it is required rather than optional on purpose: the hue
   * alone cannot carry the category. The reference's own inks leave the worst
   * deuteranopic pair 4.42 ΔE apart against a floor of 10, and deriving them to
   * clear WCAG AA drops that pair to 1.24 — so a reader with deuteranopia cannot
   * tell Marketing from Notification by colour either way. The word is the
   * channel; the hue reinforces it.
   */
  children: ReactNode;
  className?: string;
}

/**
 * The pack's signature element: two nested chips. The outer carries the deeper
 * tint pair at radius 8px, the inner the paler pair at 7px, one pixel inside its
 * parent — the step the reference itself uses.
 */
export function CategoryChip({ category, children, className }: CategoryChipProps) {
  return (
    <span
      className={['pg-cat', `pg-cat--${category}`, className].filter(Boolean).join(' ')}
    >
      <span className="pg-cat__inner">{children}</span>
    </span>
  );
}
