import type { ReactNode } from 'react';

export interface ActProps {
  children: ReactNode;
  /** `page` is white, `field` the cool grey separator, `dark` the near-black act. */
  field?: 'page' | 'field' | 'dark';
  className?: string;
}

/** A full-bleed section. `dark` sets data-surface, which remaps the palette for the
 *  band only — it is a surface variant, never a document theme. */
export function Act({ children, field = 'page', className }: ActProps) {
  return (
    <section
      className={['rl-act', `rl-act--${field}`, className].filter(Boolean).join(' ')}
      data-surface={field === 'dark' ? 'dark' : undefined}
    >
      {children}
    </section>
  );
}
