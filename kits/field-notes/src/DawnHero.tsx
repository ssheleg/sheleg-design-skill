import type { ReactNode } from 'react';

export interface DawnHeroProps {
  /** The label above the headline — a `NumberedEyebrow` belongs here. */
  eyebrow?: ReactNode;
  /**
   * Capped at three lines by `--hero-line-cap`. Write to the cap: at 1.02
   * leading a fourth line closes into a block and the dawn stops reading.
   * Wrap the one accent phrase in `<span className="fn-hero__accent">`.
   */
  headline: ReactNode;
  /** Must end above `--dawn-5`; `--lede-max` is what keeps it short enough. */
  lede?: ReactNode;
  /** Up to three buttons. */
  actions?: ReactNode;
  /** One proof line — a figure with the name of whoever produced it. */
  proof?: ReactNode;
  className?: string;
}

/**
 * **The signature element, and it happens exactly once per page.** A dark field
 * that *resolves* into the paper rather than ending against it: eight stops
 * whose last one is `--bg` itself, so there is no seam — and therefore no
 * second dark section anywhere below it, no dark band with a hard edge, no
 * full-bleed colour block. A developer tool is expected to be dark; this one
 * opens where the reader expects a console and arrives, without a join, at the
 * document it actually is.
 *
 * **It is static.** `--hero-dawn` is a gradient, not an animation: nothing here
 * fades in, scrubs, parallaxes or renders to a canvas. Motion is not part of
 * this design system.
 *
 * The first viewport carries an eyebrow, the headline, the lede, up to three
 * buttons and one proof line. It does not carry a card, a screenshot or a
 * metric row — those start below the fold, on paper.
 */
export function DawnHero({
  eyebrow,
  headline,
  lede,
  actions,
  proof,
  className,
}: DawnHeroProps) {
  return (
    <section className={['fn-hero', className].filter(Boolean).join(' ')}>
      <div className="fn-hero__shell">
        {eyebrow}
        <h1 className="fn-hero__headline">{headline}</h1>
        {lede !== undefined && <p className="fn-hero__lede">{lede}</p>}
        {actions !== undefined && <div className="fn-hero__actions">{actions}</div>}
        {proof !== undefined && <p className="fn-hero__proof">{proof}</p>}
      </div>
    </section>
  );
}
