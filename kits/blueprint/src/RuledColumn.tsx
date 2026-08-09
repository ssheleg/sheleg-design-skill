import type { ReactNode } from 'react';

export interface RuledColumnProps {
  children: ReactNode;
  className?: string;
}

/**
 * The content column with its two 1px vertical rules, in `--line-strong`,
 * running the section's full height at `--column-max`.
 *
 * They are the layout made visible, and they are why the page reads as a sheet
 * rather than as a container with a max-width. Below 1024px they collapse to
 * the viewport edges; below 768px they are removed entirely, because two rules
 * 16px in from the screen edge read as a rendering error.
 */
export function RuledColumn({ children, className }: RuledColumnProps) {
  return (
    <div className={['bp-column', className].filter(Boolean).join(' ')}>
      <span className="bp-column__rule bp-column__rule--l" aria-hidden="true" />
      <div className="bp-column__inner">{children}</div>
      <span className="bp-column__rule bp-column__rule--r" aria-hidden="true" />
    </div>
  );
}
