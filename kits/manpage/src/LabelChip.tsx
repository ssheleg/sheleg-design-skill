import type { ReactNode } from 'react';

export interface LabelChipProps {
  children: ReactNode;
  /**
   * The heading level this chip *is*. The chip is not a decoration above a
   * heading — it is the heading, so it must carry a real level.
   * Pass `null` only for the rare non-sectioning eyebrow.
   */
  level?: 2 | 3 | null;
  className?: string;
}

export function LabelChip({ children, level = 2, className }: LabelChipProps) {
  const chip = (
    <span className={['mp-label', level === null ? className : undefined]
      .filter(Boolean)
      .join(' ')}
    >
      {children}
    </span>
  );
  if (level === null) return chip;
  const Tag = `h${level}` as 'h2' | 'h3';
  return <Tag className={['mp-label__head', className].filter(Boolean).join(' ')}>{chip}</Tag>;
}
