import type { ReactNode } from 'react';

export interface FaqEntry {
  q: string;
  a: ReactNode;
}

export interface FaqListProps {
  entries: FaqEntry[];
  className?: string;
}

/**
 * A definition list, always open. There is deliberately no `collapsed` prop:
 * an accordion here costs the extractable answer and buys nothing.
 */
export function FaqList({ entries, className }: FaqListProps) {
  return (
    <dl className={['mp-faq', className].filter(Boolean).join(' ')}>
      {entries.map(({ q, a }) => (
        <div className="mp-faq__row" key={q}>
          <dt className="mp-faq__q">{q}</dt>
          <dd className="mp-faq__a">
            <span className="mp-faq__glyph" aria-hidden="true">└</span>
            <span>{a}</span>
          </dd>
        </div>
      ))}
    </dl>
  );
}
