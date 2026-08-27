export interface ThinkingDotsProps {
  /** Accessible label for the working state; the dots alone say nothing. */
  label?: string;
  className?: string;
}

export function ThinkingDots({ label = 'Working', className }: ThinkingDotsProps) {
  return (
    <span
      className={['td-thinking', className].filter(Boolean).join(' ')}
      role="status"
      aria-label={label}
    >
      <i className="td-thinking__dot" />
      <i className="td-thinking__dot" />
      <i className="td-thinking__dot" />
    </span>
  );
}
