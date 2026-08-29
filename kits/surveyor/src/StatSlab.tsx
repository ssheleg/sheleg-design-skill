export interface StatSlabProps {
  /** The counted reading, e.g. "100M+" — set at 40px/600 in the working teal. */
  value: string;
  /** The uppercase label under it, e.g. "AI answers monthly". */
  label: string;
  className?: string;
}

export function StatSlab({ value, label, className }: StatSlabProps) {
  return (
    <div className={['sv-slab', className].filter(Boolean).join(' ')}>
      <span className="sv-slab__value">{value}</span>
      <span className="sv-slab__label">{label}</span>
    </div>
  );
}
