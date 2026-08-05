export interface ActBadgeProps {
  /** The act's position. Rendered zero-padded to two digits — "02". */
  index: number;
  /** The act's name. Rendered upper-case: "CONTROL". */
  name: string;
  className?: string;
}

export function ActBadge({ index, name, className }: ActBadgeProps) {
  const padded = String(Math.max(Math.trunc(index), 0)).padStart(2, '0');
  return (
    <span className={['ic-act', className].filter(Boolean).join(' ')}>
      <span className="ic-act__index">{padded}</span>
      <span className="ic-act__sep" aria-hidden="true">
        /
      </span>
      <span className="ic-act__name">{name}</span>
    </span>
  );
}
