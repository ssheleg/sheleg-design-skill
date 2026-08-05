export interface SourcedNumberProps {
  /** The figure itself, already formatted: `2.1bn`, `41%`, `£1.4m`. */
  value: string;
  /**
   * Where it came from — publication, year, cut. **Required**: an unsourced
   * figure on an investor slide is a liability, so it is not a prop you can
   * forget.
   */
  source: string;
  /** What the figure measures. Sits above it in mono uppercase. */
  label?: string;
  className?: string;
}

/** The figure, with its source in mono directly beneath it. */
export function SourcedNumber({ value, source, label, className }: SourcedNumberProps) {
  return (
    <figure className={['br-figure', className].filter(Boolean).join(' ')}>
      {label !== undefined && <span className="br-figure__label">{label}</span>}
      <span className="br-figure__value">{value}</span>
      <figcaption className="br-figure__source">{source}</figcaption>
    </figure>
  );
}
