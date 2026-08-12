import type { ReactNode } from 'react';

export interface InstrumentProps {
  /** The reading's subject line — an id, a request, a device. */
  title?: string;
  /** The mono micro-label stating a condition about the data itself. */
  badge?: string;
  /**
   * The alarm state: the instrument re-skins itself dark because of what it
   * DETECTED, never because a user asked for dark. Wiring this to a theme
   * toggle or to prefers-color-scheme destroys the pack's one idea.
   */
  alarm?: boolean;
  children: ReactNode;
  className?: string;
}

export function Instrument({ title, badge, alarm = false, children, className }: InstrumentProps) {
  return (
    <section
      className={['ds-instrument', className].filter(Boolean).join(' ')}
      data-state={alarm ? 'alarm' : undefined}
    >
      {(title !== undefined || badge !== undefined) && (
        <header className="ds-instrument__head">
          {title !== undefined && <span className="ds-instrument__title">{title}</span>}
          {badge !== undefined && <span className="ds-badge">{badge}</span>}
        </header>
      )}
      <div className="ds-instrument__grid">{children}</div>
    </section>
  );
}
