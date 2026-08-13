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
 * A definition list, always open. There is deliberately no `collapsed` prop: the
 * reference ships seven `dt`/`dd` pairs in served HTML and no `<details>`, and an
 * answer a crawler cannot read without running JavaScript is an answer that is
 * not there.
 */
export function FaqList({ entries, className }: FaqListProps) {
  return (
    <dl className={['ro-faq', className].filter(Boolean).join(' ')}>
      {entries.map(({ q, a }) => (
        <div className="ro-faq__row" key={q}>
          <dt className="ro-faq__q">{q}</dt>
          <dd className="ro-faq__a">{a}</dd>
        </div>
      ))}
    </dl>
  );
}
