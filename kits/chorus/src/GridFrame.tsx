import type { ReactNode } from 'react';

export interface GridFrameProps {
  /** Draws the plus mark at each rule intersection. */
  crosshairs?: boolean;
  /** `slab` continues the same grid across the dark band. */
  surface?: 'paper' | 'slab';
  children: ReactNode;
  className?: string;
}

export function GridFrame({
  crosshairs = true,
  surface = 'paper',
  children,
  className,
}: GridFrameProps) {
  return (
    <section
      className={[
        'ch-frame',
        `ch-frame--${surface}`,
        crosshairs ? 'ch-frame--cross' : null,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      <span aria-hidden="true" className="ch-frame__rule ch-frame__rule--l" />
      <span aria-hidden="true" className="ch-frame__rule ch-frame__rule--r" />
      <div className="ch-frame__inner">{children}</div>
    </section>
  );
}
