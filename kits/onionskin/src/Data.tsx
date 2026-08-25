export interface DataProps {
  /** The figure. Always the monospace — a number in the sans breaks the document. */
  value: string;
  /** Its unit or suffix, one tier quieter. */
  unit?: string;
  className?: string;
}

export function Data({ value, unit, className }: DataProps) {
  return (
    <span className={['ok-data', className].filter(Boolean).join(' ')}>
      <span className="ok-data__value">{value}</span>
      {unit !== undefined && <span className="ok-data__unit">{unit}</span>}
    </span>
  );
}
