import type { ReactNode } from 'react';

export interface StepCardProps {
  /** Two digits, in the accent. "01", not "1". */
  step: string;
  title: string;
  children: ReactNode;
  /** Short capability chips under the copy. */
  chips?: string[];
  /** The product shot. Cropped in browser chrome on the reference, and below the fold. */
  figure?: ReactNode;
  className?: string;
}

/**
 * A numbered step: copy on the left, the product on the right. It sets
 * `container-type: inline-size`, because the split is a fact about the card's own
 * width — the same card appears full-bleed and inside a narrower column on one page.
 */
export function StepCard({ step, title, children, chips, figure, className }: StepCardProps) {
  return (
    <section className={['ro-step', className].filter(Boolean).join(' ')}>
      <div className="ro-step__body">
        <span className="ro-step__number">{step}</span>
        <h3 className="ro-step__title">{title}</h3>
        <div className="ro-step__copy">{children}</div>
        {chips !== undefined && chips.length > 0 && (
          <ul className="ro-step__chips">
            {chips.map((c) => (
              <li className="ro-step__chip" key={c}>{c}</li>
            ))}
          </ul>
        )}
      </div>
      {figure !== undefined && <div className="ro-step__figure">{figure}</div>}
    </section>
  );
}
