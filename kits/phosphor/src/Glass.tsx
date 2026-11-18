import type { ReactNode } from 'react';

export interface GlassProps {
  /** Mono caps title in the window's header row. */
  title?: string;
  /** Right-aligned header metadata: a member count, a channel. */
  meta?: string;
  /** Draw the two AR corner brackets (top-left, bottom-right). */
  brackets?: boolean;
  children: ReactNode;
  className?: string;
}

export function Glass({ title, meta, brackets = false, children, className }: GlassProps) {
  return (
    <section
      className={['ph-glass', brackets ? 'ph-glass--brackets' : null, className]
        .filter(Boolean)
        .join(' ')}
    >
      {(title || meta) && (
        <header className="ph-glass__head">
          {title && <span className="ph-glass__title">{title}</span>}
          {meta && <small className="ph-glass__meta">{meta}</small>}
        </header>
      )}
      <div className="ph-glass__body">{children}</div>
    </section>
  );
}
