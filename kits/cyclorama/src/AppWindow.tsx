import type { ReactNode } from 'react';

export interface AppWindowProps {
  title: string;
  /** The mono sub-line under the title: a session id, a phase, a duration. */
  meta?: string;
  /** Rendered at the window's top right — a StatusPill belongs here. */
  status?: ReactNode;
  /** The row of chips along the window's foot. */
  footer?: ReactNode;
  children: ReactNode;
  className?: string;
}

/**
 * How this pack draws product UI without breaking the page's one continuous
 * surface: a `1px var(--line)` frame at `--radius-lg` with **no fill at all**,
 * so the field cycle shows straight through it.
 *
 * Giving it a background is the single most common way to break this pack. The
 * window is a frame, not a surface — the moment it fills, the page's signature
 * stops at its border and the screenshot inside becomes a foreign object
 * pasted onto a pastel page.
 *
 * Its 12px of padding is what makes the chips inside `--radius-sm`: 16 − 12 = 4.
 */
export function AppWindow({ title, meta, status, footer, children, className }: AppWindowProps) {
  return (
    <section className={['cy-window', className].filter(Boolean).join(' ')}>
      <header className="cy-window__bar">
        <span className="cy-window__lights" aria-hidden="true">
          <i />
          <i />
          <i />
        </span>
        <span className="cy-window__titles">
          <span className="cy-window__title">{title}</span>
          {meta !== undefined && <span className="cy-window__meta">{meta}</span>}
        </span>
        {status !== undefined && <span className="cy-window__status">{status}</span>}
      </header>
      <div className="cy-window__body">{children}</div>
      {footer !== undefined && <footer className="cy-window__foot">{footer}</footer>}
    </section>
  );
}
