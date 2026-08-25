import type { ReactNode } from 'react';

export interface PanelProps {
  children: ReactNode;
  /** The micro label along the top — uppercase, tracked open. */
  label?: string;
  /** `subject` lights the panel's left and right edge. One per section. */
  emphasis?: 'plain' | 'subject';
  /** `provisional` draws the hairline dashed: a drop target, a planned step, an empty slot. */
  boundary?: 'solid' | 'provisional';
  className?: string;
}

/** The pack's signature: a zero-radius region of the sheet, ruled by a hairline. */
export function Panel({ children, label, emphasis = 'plain', boundary = 'solid', className }: PanelProps) {
  return (
    <section
      className={['ok-panel', `ok-panel--${emphasis}`, `ok-panel--${boundary}`, className]
        .filter(Boolean).join(' ')}
    >
      {label !== undefined && <span className="ok-panel__label">{label}</span>}
      <div className="ok-panel__body">{children}</div>
    </section>
  );
}
