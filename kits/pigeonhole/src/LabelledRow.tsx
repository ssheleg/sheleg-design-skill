import type { ReactNode } from 'react';
import { CategoryChip, type Category } from './CategoryChip.js';

export interface LabelledRowProps {
  /** Who or what the item came from. */
  from: string;
  subject: string;
  /** The first line of the body, truncated by CSS rather than by JavaScript. */
  preview?: ReactNode;
  /** A short absolute date — never "2 days ago", which goes stale in a screenshot. */
  date?: string;
  category?: Category;
  /** The category's label word. Required whenever `category` is set. */
  categoryLabel?: string;
  unread?: boolean;
  className?: string;
}

/**
 * One row of the product, labelled — the atom this pack is built from. The
 * marketing page's set pieces are art direction; this is the part that is
 * genuinely a component, and the chip sits above the row rather than inside it,
 * which is how the reference stacks them.
 */
export function LabelledRow({
  from,
  subject,
  preview,
  date,
  category,
  categoryLabel,
  unread = false,
  className,
}: LabelledRowProps) {
  return (
    <div
      className={['pg-row', unread && 'pg-row--unread', className]
        .filter(Boolean)
        .join(' ')}
    >
      {category !== undefined && categoryLabel !== undefined && (
        <CategoryChip category={category}>{categoryLabel}</CategoryChip>
      )}
      <div className="pg-row__body">
        <div className="pg-row__head">
          <span className="pg-row__from">{from}</span>
          {date !== undefined && <span className="pg-row__date">{date}</span>}
        </div>
        <div className="pg-row__subject">{subject}</div>
        {preview !== undefined && <div className="pg-row__preview">{preview}</div>}
      </div>
    </div>
  );
}
