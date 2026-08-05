import type { ReactNode } from 'react';

export interface SlideFrameProps {
  /** Renders as `[04]` in the header and as the position indicator in the footer. */
  number: number;
  /** The section this slide belongs to — `MARKET · WHY NOW`. Uppercased in CSS. */
  section: string;
  /** Footer text on the left: deck name, date, confidentiality. */
  footnote?: string;
  /** The pack allows at most one radial accent glow per slide. This is it. */
  glow?: boolean;
  children: ReactNode;
  className?: string;
}

/**
 * The canvas. Fixed 1280x720 with `overflow: hidden`, which is the pack's first
 * constraint and the reason it has no smaller type ramp to fall back on.
 */
export function SlideFrame({
  number,
  section,
  footnote,
  glow = false,
  children,
  className,
}: SlideFrameProps) {
  // `[04]`, not `[4]` — the numbers are furniture and furniture lines up.
  const padded = String(number).padStart(2, '0');
  return (
    <section
      className={['br-frame', className].filter(Boolean).join(' ')}
      aria-label={`Slide ${padded}: ${section}`}
    >
      {glow && <div className="br-frame__glow" aria-hidden="true" />}
      <header className="br-frame__header">
        <span className="br-frame__section">{`[${padded}] ${section}`}</span>
      </header>
      <div className="br-frame__body">{children}</div>
      <footer className="br-frame__footer">
        <span className="br-frame__footnote">{footnote}</span>
        <span className="br-frame__number">{padded}</span>
      </footer>
    </section>
  );
}
