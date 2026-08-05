export interface SourcedFigureProps {
  value: string;
  label: string;
  /** Required: on a health page an unsourced number is a liability. */
  source: string;
  className?: string;
}

/**
 * One figure from the stat row: a sans 600 numeral, a light sublabel beneath,
 * and the source the number carries with it. Sans, not serif, not mono — the
 * numbers are claims, and the serif is reserved for sentences.
 *
 * Place two to four side by side in a flex row; the 1px hairline that separates
 * them is drawn between siblings by the stylesheet, so the row itself is plain
 * layout and needs no component of its own.
 */
export function SourcedFigure({ value, label, source, className }: SourcedFigureProps) {
  return (
    <figure className={['at-figure', className].filter(Boolean).join(' ')}>
      <span className="at-figure__value">{value}</span>
      <figcaption className="at-figure__caption">
        <span className="at-figure__label">{label}</span>
        <cite className="at-figure__source">{source}</cite>
      </figcaption>
    </figure>
  );
}
