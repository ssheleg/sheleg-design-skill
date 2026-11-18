export interface WaitingProps {
  /** The line before the cursor, in the reader's words. */
  label: string;
  className?: string;
}

/** The loader: a mono caps line ending in a block cursor that blinks on two steps. */
export function Waiting({ label, className }: WaitingProps) {
  return (
    <p className={['ph-waiting', className].filter(Boolean).join(' ')} role="status">
      {label}
      <span className="ph-waiting__cursor" aria-hidden="true" />
    </p>
  );
}
