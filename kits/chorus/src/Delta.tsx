export interface DeltaProps {
  /** The signed change, already formatted: "0.48%", "12". */
  value: string;
  direction: 'up' | 'down';
  /** `dark` picks the on-slab ladder; the mint does not exist on paper. */
  surface?: 'paper' | 'dark';
  className?: string;
}

export function Delta({ value, direction, surface = 'paper', className }: DeltaProps) {
  return (
    <span
      className={['ch-delta', `ch-delta--${direction}`, `ch-delta--${surface}`, className]
        .filter(Boolean)
        .join(' ')}
    >
      <span aria-hidden="true" className="ch-delta__arrow">
        {direction === 'up' ? '\u2191' : '\u2193'}
      </span>
      <span className="ch-delta__value">{value}</span>
      <span className="ch-delta__sr">{direction === 'up' ? 'up' : 'down'}</span>
    </span>
  );
}
