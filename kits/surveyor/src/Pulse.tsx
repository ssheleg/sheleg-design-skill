export interface PulseProps {
  /** Accessible label for what is live; the dot alone says nothing. */
  label?: string;
  className?: string;
}

/** The live marker — the page's one loop, at most one per viewport. */
export function Pulse({ label = 'Live', className }: PulseProps) {
  return (
    <span className={['sv-pulse', className].filter(Boolean).join(' ')} role="status" aria-label={label}>
      <i className="sv-pulse__dot" />
      <i className="sv-pulse__ring" aria-hidden="true" />
    </span>
  );
}
